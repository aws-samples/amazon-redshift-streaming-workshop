package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"os"
	"strings"
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

var client *kgo.Client

func main() {

	MSK_TOPIC_NAME := "consignment_stream_msk"

	// open arn.txt and read msk serverless cluster arn
	msk_serverless_arn_byte, err := ioutil.ReadFile("arn.txt")
	if err != nil {
		log.Println("Couldn't load arn file: ", err)
		os.Exit(1)
	}
	msk_serverless_arn := fmt.Sprintf("%s", msk_serverless_arn_byte)
	msk_serverless_arn = strings.TrimSuffix(msk_serverless_arn, "\n")
	log.Printf("|%s|\n", msk_serverless_arn)

	// get broker
	mySession := session.Must(session.NewSession())
	creds := credentials.NewCredentials(&ec2rolecreds.EC2RoleProvider{Client: ec2metadata.New(mySession), ExpiryWindow: 5 * time.Minute})
	mySession.Config.Credentials = creds
	svc := kafka.New(mySession, aws.NewConfig().WithRegion("us-west-2"))
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
			// log.Println("Access key", val.AccessKeyID)
			// log.Println("Secret key", val.SecretAccessKey)
			// log.Println("SessionToken", val.SessionToken)

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

	// produce 1,000,000 msg to topic

}
