package main

import (
	"context"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds"
	"github.com/aws/aws-sdk-go/aws/ec2metadata"
	"github.com/aws/aws-sdk-go/aws/session"

	"github.com/aws/aws-sdk-go/service/kafka"

	"github.com/twmb/franz-go/pkg/kadm"
	"github.com/twmb/franz-go/pkg/kgo"

	sasl_aws "github.com/twmb/franz-go/pkg/sasl/aws"
)

type MSKRecord struct {
	Consignmentid       int     `json:"consignmentid"`
	Consignment_date    string  `json:"consignment_date"`
	Destination_address string  `json:"destination_address"`
	Destination_state   string  `json:"destination_state"`
	Destination_lat     float32 `json:"destination_lat"`
	Destination_long    float32 `json:"destination_long"`
	Origin_address      string  `json:"origin_address"`
	Origin_state        string  `json:"origin_state"`
	Origin_lat          float32 `json:"origin_lat"`
	Origin_long         float32 `json:"origin_long"`
	Userid              int     `json:"userid"`
	Delivery_date       string  `json:"delivery_date"`
	Days_to_deliver     int     `json:"days_to_deliver"`
	Revenue             int     `json:"revenue"`
	Cost                int     `json:"cost"`
}

var client *kgo.Client

func main() {

	MSK_CLUSTER_NAME := "workshop-cluster"
	MSK_TOPIC_NAME := "consignment_stream_msk"
	PRODUCE_RECORD_NUM := 100000
	SLEEP_TIME := 0.3

	// get msk cluster list & broker
	mySession := session.Must(session.NewSession())
	creds := credentials.NewCredentials(&ec2rolecreds.EC2RoleProvider{Client: ec2metadata.New(mySession), ExpiryWindow: 5 * time.Minute})
	mySession.Config.Credentials = creds
	svc := kafka.New(mySession, aws.NewConfig().WithRegion("us-west-2"))

	cluster_list, err := svc.ListClustersV2(&kafka.ListClustersV2Input{})
	if err != nil {
		log.Printf("ListClusterV2 returns error... %+v\n", err)
		os.Exit(1)
	}

	msk_serverless_arn := ""
	for _, cluster_info := range cluster_list.ClusterInfoList {
		// log.Printf("looking %v\n", cluster_info)
		if *(cluster_info.ClusterName) == MSK_CLUSTER_NAME {
			log.Printf("GOTCHA...\n%v\n", cluster_info)
			msk_serverless_arn = *(cluster_info.ClusterArn)
		}
	}
	if msk_serverless_arn == "" {
		log.Printf("Couldn't find workshop msk serverless cluster\n")
		os.Exit(1)
	}

	// msk_serverless_arn := *(cluster_list.ClusterInfoList[0].ClusterArn)
	log.Printf("Got MSK Serverless cluster arn : %s\n", msk_serverless_arn)

	msk_bootstrap_brokers, err := svc.GetBootstrapBrokers(&kafka.GetBootstrapBrokersInput{ClusterArn: aws.String(msk_serverless_arn)})
	if err != nil {
		log.Printf("GetBootstrapBrokers returns error... %+v\n", err)
		os.Exit(1)
	}

	msk_broker_string := msk_bootstrap_brokers.BootstrapBrokerStringSaslIam
	log.Printf("MSK Serverless broker: %s\n", *msk_broker_string)

	// create topic
	// create tlsDialer
	tlsDialer := &tls.Dialer{NetDialer: &net.Dialer{Timeout: 5 * time.Second}}

	// set client option
	opts := []kgo.Opt{
		kgo.SeedBrokers(strings.Split(*msk_broker_string, ",")...), // broker
		kgo.SASL(sasl_aws.ManagedStreamingIAM(func(ctx context.Context) (sasl_aws.Auth, error) {

			// create session
			sess := session.Must(session.NewSession())
			// force to use EC2RoleProvider for IAM auth
			creds := credentials.NewCredentials(&ec2rolecreds.EC2RoleProvider{Client: ec2metadata.New(sess), ExpiryWindow: 5 * time.Minute})
			sess.Config.Credentials = creds
			// get credentials
			val, err := creds.GetWithContext(ctx)

			if err != nil {
				log.Println("failed to get credentials :( :(", err.Error())
				return sasl_aws.Auth{}, err
			}
			log.Println("got credentials", val.ProviderName)

			return sasl_aws.Auth{
				AccessKey:    val.AccessKeyID,
				SecretKey:    val.SecretAccessKey,
				SessionToken: val.SessionToken,
				UserAgent:    "franz-go/creds_test/v1.0.0",
			}, nil
		})),
		kgo.Dialer(tlsDialer.DialContext),
	}

	// create client
	client, err = kgo.NewClient(opts...)
	if err != nil {
		log.Fatal(err)
	}

	defer client.Close()

	// create admin client
	kadmin := kadm.NewClient(client)

	// get topic list
	topics, err := kadmin.ListTopics(context.Background(), MSK_TOPIC_NAME)
	if err != nil {
		log.Println("failed to list topics", err)
	}

	// log topic list
	log.Println("Topics: ", topics)

	// if there's no topic, create it
	if !topics.Has(MSK_TOPIC_NAME) {
		resps, err := kadmin.CreateTopics(context.Background(), 3, 2, nil, MSK_TOPIC_NAME)
		if err != nil {
			log.Fatal("create topic invocation failed", err)
		}

		resp, err := resps.On(MSK_TOPIC_NAME, nil)
		if err != nil {
			log.Fatal(err)
		}
		if resp.Err != nil {
			log.Fatal(err)
		}

	} else {
		log.Println("topic already exists", MSK_TOPIC_NAME)
	}

	// periodically produce msgs to topic
	_rseed := rand.NewSource(time.Now().UnixNano())
	_rd := rand.New(_rseed)
	ctx := context.Background()
	var wg sync.WaitGroup

	for _idx := 1; _idx <= PRODUCE_RECORD_NUM; _idx++ {
		days_to_deliver := _rd.Intn(5) + 2
		mean_distance := 10 + (days_to_deliver * 100)
		rev := _rd.Intn(mean_distance/6-mean_distance/18) + mean_distance/6
		_v := &MSKRecord{
			Consignmentid:       _idx,
			Consignment_date:    time.Now().UTC().Format("2006-01-02T15:04:05-0700"),
			Destination_address: "address " + strconv.Itoa(_rd.Intn(100000)),
			Destination_state:   fmt.Sprintf("%0d", _rd.Intn(20)),
			Destination_lat:     _rd.Float32()*6.2 - 37.643,
			Destination_long:    _rd.Float32()*8.3 + 141.224,
			Origin_address:      "address " + strconv.Itoa(_rd.Intn(100000)),
			Origin_state:        fmt.Sprintf("%0d", _rd.Intn(20)),
			Origin_lat:          _rd.Float32()*6.2 - 37.643,
			Origin_long:         _rd.Float32()*8.3 + 141.224,
			Userid:              _rd.Intn(15521),
			Delivery_date:       time.Now().AddDate(0, 0, days_to_deliver).UTC().Format("2006-01-02T15:04:05-0700"),
			Days_to_deliver:     days_to_deliver,
			Revenue:             rev,
			Cost:                rev - (int(_rd.Float32()*float32(rev)) / 2),
		}

		// produce(_idx, _v)
		_jbytearr, err := json.Marshal(_v)
		if err != nil {
			fmt.Println(err)
			return
		}
		wg.Add(1)
		record := &kgo.Record{Topic: MSK_TOPIC_NAME, Value: _jbytearr}
		client.Produce(ctx, record, func(_ *kgo.Record, err error) {
			defer wg.Done()
			if err != nil {
				log.Println("Producer error: %v\n", err)
			}
		})

		time.Sleep(time.Duration(SLEEP_TIME*float64(1000)) * time.Millisecond)
	}

	wg.Wait()

}
