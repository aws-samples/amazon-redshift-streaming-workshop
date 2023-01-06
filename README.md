
# Amazon Redshift Streaming Workshop

Most organisations today agree that data is one of their most important asset and that the ability to act on timely data, sets data-driven organisations apart from their peers. However getting access to real-time data used to require significant investment in terms of acquiring new software or in hiring specialised engineering teams. The new Amazon Redshift streaming ingestion feature aims to democratise streaming analytics with its low-cost and minimal technical skill requirements as it is primarily defined using SQL.

In this workshop, we will build a near-realtime logistics dashboard using [Amazon Redshift](https://aws.amazon.com/redshift/)  and [Amazon Managed Grafana](https://aws.amazon.com/grafana/). Our example will be an operational dashboard for a logistics company that provides situational awareness and augmented intelligence for their operations team. From this dashboard, the team can see the current state of their consignments and their logistics fleet based on events that happened only a few seconds ago. It also shows the consignment delay predictions of a Redshift ML model that helps then proactively respond to disruptions before it even happens.

![dashboard](./images/dashboard.png)


**Solution Overview**

This solution is composed of the following components and the provisioning of resources will be automated using the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/):

- Multiple streaming data sources are simulated through Python code running in our serverless compute service, [AWS Lambda](https://aws.amazon.com/lambda/).

- The streaming events are captured by [Amazon Kinesis Data Stream](https://aws.amazon.com/kinesis/data-streams/) which is a highly scalable serverless streaming data service. 

- We will then use the Amazon Redshift streaming feature to process and store the streaming data and Redshift ML to predict the likelihood of a consignment getting delayed.

- [AWS Step Functions](https://aws.amazon.com/step-functions) will be used for serverless workflow orchestration.

- Followed by a consumption layer built on Amazon Managed Grafana where we can visualise the insights and even generate alerts through [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) for our operations team. 




### Infrastructure Provisioning using CDK and Cloudshell

The AWS Cloud Development Kit (AWS CDK) is an open-source project that allows you to define your cloud infrastructure using familiar programming languages. It leverages high level constructs to represent AWS components to simplify the build process. In this blog, we used Python to define the cloud infrastructure due to its familiarity to many data and analytics professionals.

The project has the following prerequisites:

- An [AWS account](https://console.aws.amazon.com/console/home)

- Amazon Linux 2 with [AWS CDK](https://aws.amazon.com/getting-started/guides/setup-cdk/module-two/), [Docker CLI](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html) and Python3 installed. Alternatively, setting up an [AWS Cloud9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html) will satisfy this requirement.

- Note: In order for you to run this code you will need elevated privileges into the AWS account you are using.

Clone Github repository and install python dependencies.

```bash
git clone https://github.com/aws-samples/amazon-redshift-streaming-workshop --branch blog

cd amazon-redshift-streaming-workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Bootstrap CDK. This will set-up the resources required by CDK to deploy into the AWS account. This step is only required if you have not used CDK in the deployment account and region

```bash
cdk bootstrap
```

Deploy all stacks. The entire deployment time will take 10-15 minutes.

```bash
cdk deploy IngestionStack
cdk deploy RedshiftStack
cdk deploy StepFunctionStack
```


### Connecting to the Redshift Cluster 

Login to the Redshift Query Editor v2 and connect to the redshift cluster using the drop down arrow next to the cluster name.

https://console.aws.amazon.com/sqlworkbench/home

![image-20220601100354395](./images/image-20220601100354395.png)

Specify cluster credentials. Select **Temporary credentials** as the authentication mechanism.

Database: **dev**

User name: **rsstream_user**

Click **Create connection**

<img src="./images/image-20220601100630463.png" alt="image-20220601100630463" style="zoom:50%;" />



Create an external schema to establish connection between the Redshift cluster and the Kinesis data stream. 

```sql
CREATE EXTERNAL SCHEMA kinesis_schema
FROM KINESIS
IAM_ROLE default;
```

![image-20220601101019956](./images/image-20220601101019956.png)

Create a materialized view to parse data in the kinesis data stream, customer_stream. In this case, the whole payload is ingested as is and stored using the super data type in Redshift.

```sql
CREATE MATERIALIZED VIEW customer_stream AS
SELECT ApproximateArrivalTimestamp,
JSON_PARSE(from_varbyte(Data, 'utf-8')) as customer_data
FROM kinesis_schema.customer_stream
WHERE is_utf8(Data) AND is_valid_json(from_varbyte(Data, 'utf-8'));
```

Note: highlight the block of SQL code that you need to run in the Query Editor.

![image-20220601101137670](./images/image-20220601101137670.png)



Refresh the materialized views. This is where the actual data ingestion happens. Data gets loaded from the kinesis data stream into Amazon S3 without having to stage it first in S3.

```sql
REFRESH MATERIALIZED VIEW customer_stream;
```

We can now query the data in the customer_stream using standard select statement.

```
SELECT * FROM customer_stream;
```

![image-20220601101309371](./images/image-20220601101309371.png)

If we like to know the distribution of our customers across different states, we can easily unpack the contents of the JSON payload using the [PartiQL](https://partiql.org/) syntax.

```sql
SELECT count(1), customer_data.STATE::VARCHAR
FROM customer_stream
GROUP BY customer_data.STATE;
```

![image-20220601101418301](./images/image-20220601101418301.png)

Now let us ingest data from the order_stream. Let us create a materialized view that unpacks the data within the order stream.

```sql
CREATE MATERIALIZED VIEW order_stream AS
SELECT ApproximateArrivalTimestamp,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'consignmentid', true)::BIGINT as consignmentid,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'timestamp', true)::VARCHAR(50) as order_timestamp,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_address', true)::VARCHAR(100) as delivery_address,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_state', true)::VARCHAR(50) as delivery_state,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'origin_address', true)::VARCHAR(100) as origin_address,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'origin_state', true)::VARCHAR(50) as origin_state,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delay_probability', true)::VARCHAR(10) as delay_probability,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'days_to_deliver', true)::INT as days_to_deliver,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_distance', true)::FLOAT as delivery_distance,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'userid', true)::INT as userid,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'revenue', true)::FLOAT as revenue,
JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'cost', true)::FLOAT as cost
FROM kinesis_schema.order_stream
WHERE is_utf8(Data) AND is_valid_json(from_varbyte(Data, 'utf-8'));
```

Let us refresh the materialized view.

```sql
REFRESH MATERIALIZED VIEW order_stream;
```

And query the data within the view

```sql
SELECT * FROM order_stream;
```

We can query the most recent transactions that have been ingested into Redshift using this select statement

```sql
SELECT current_timestamp, current_timestamp-ApproximateArrivalTimestamp as time_diff, * FROM order_stream
order by ApproximateArrivalTimestamp desc limit 10;
```

![image-20220601101704387](./images/image-20220601101704387.png)

We can also join the data between the two streams and do more in depth analysis on our customer and order data. For example, we like to know what is the busiest consignment route on the state level.

```sql
SELECT os.delivery_state, cs.customer_data.state::VARCHAR as origin_state, count(1)
FROM customer_stream cs
INNER JOIN order_stream os ON cs.customer_data.userid::INT = os.userid
GROUP BY os.delivery_state, cs.customer_data.state::VARCHAR
ORDER BY count(1) desc
```

![image-20220601101807687](./images/image-20220601101807687.png)



Create user redshift_data_api_user for Grafana integration. Note: We need to use this specific user, 'redshift_data_api_user' as this is used for the IAM integration between Redshift and Managed Grafana.

```sql
CREATE USER redshift_data_api_user PASSWORD '<specify your own password>';
```

We can now grant select access to this specific user.

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA PUBLIC TO redshift_data_api_user;
```



**(Optional Step) No Action Required**

Refreshing the Materialized views using Step Functions

As part of the CDK deployment, we also provisioned a Step Function that will regularly refresh the materialized views on a 10-20 second interval. You can opt to inspect this Step Function by looking at the Step Function console. 

https://console.aws.amazon.com/states/home?region=us-east-1

![image-20220530180606214](./images/image-20220530180606214.png)



You can also check the Redshift Queries console to validate time interval between refreshes.

https://us-east-1.console.aws.amazon.com/redshiftv2/home?region=us-east-1#queries

![image-20220601102552452](./images/image-20220601102552452.png)



### Creating a Grafana dashboard on Redshift streaming data 

Note: This section is not compatible with accounts created using AWS Event Engine (due to SSO restrictions)

Here is a relevant [blog](https://aws.amazon.com/blogs/mt/amazon-managed-grafana-getting-started/) that talks about how to get started with Amazon Managed Grafana. 

Go to the Amazon Managed Grafana console:

https://us-east-1.console.aws.amazon.com/grafana/home?region=us-east-1

Click on **Create workspace**.

![image-20220530180941106](./images/image-20220530180941106.png)

Specify a workspace name: **redshift_streaming_workspace**

<img src="./images/image-20220601103241863.png" alt="image-20220601103241863" style="zoom:50%;" />

Select **AWS Single Sign-On** as the authentication method and click on **Create user**.

<img src="./images/image-20220601103404934.png" alt="image-20220601103404934" style="zoom:50%;" />

Specify user details and click **Create user**

<img src="./images/image-20220601103538765.png" alt="image-20220601103538765" style="zoom: 50%;" />

The user will receive an email to accept invitation to AWS SSO.

![image-20220601103906448](./images/image-20220601103906448.png)

Accepting the invitation will prompt for the user to specify a password.

<img src="./images/image-20220601104031456.png" alt="image-20220601104031456" style="zoom: 40%;" />



Click **Next**

<img src="./images/image-20220601104211596.png" alt="image-20220601104211596" style="zoom:50%;" />



On Service managed permission settings, select **Amazon Redshift** as a datasource and select **Amazon SNS** as a notification channel.

<img src="./images/image-20220601104510191.png" alt="image-20220601104510191" style="zoom:50%;" />

Review workspace creation settings and click on **Create workspace**.

Once the workspace is created, we will need to assign the SSO user to have access to the Grafana workspace. Click on **Assign new user or group**.

![image-20220601105429528](./images/image-20220601105429528.png)

Select the user we created and click **Assign users and groups**.

![image-20220601105541755](./images/image-20220601105541755.png)

Elevate the privileges of the user from viewer to **admin** and go back to the workspace screen.

![image-20220601105708129](./images/image-20220601105708129.png)

Click on the **Grafana workspace URL link**.

![image-20220601105850286](./images/image-20220601105850286.png)



Click on **Sign in with AWS SSO**

Enter **username**

Enter **password**

<img src="./images/image-20220601110210714.png" alt="image-20220601110210714" style="zoom:40%;" />

You should now be logged in to the Amazon Managed Grafana dashboard.

Click on the **AWS** side tab and select **Data sources**.

![image-20220601111620412](./images/image-20220601111620412.png)

Select the **Redshift** service. Select **US East (N. Virginia)** region. Select the cluster we provisioned as part of this workshop and click on **Add 1 data source**.

![image-20220601111747182](./images/image-20220601111747182.png)

Click **Go to settings**

![image-20220601111913721](./images/image-20220601111913721.png)

Rename datasource to **Redshift Streaming**

Set Database User to **redshift_data_api_user**. Click on **Save & test**.

<img src="./images/image-20220601121543957.png" alt="image-20220601121543957" style="zoom:50%;" />

Now let us import the pre-built dashboard. Click on the **+** side menu and click **Import**.

<img src="./images/image-20220601121846321.png" alt="image-20220601121846321" style="zoom:50%;" />

Copy and paste the contents of the [dashboard.json](https://raw.githubusercontent.com/aws-samples/amazon-redshift-streaming-workshop/main/dashboard.json) file into the Import via panel json textbox. Click Load.

<img src="./images/image-20220601123118745.png" alt="image-20220601123118745" style="zoom:50%;" />

Click **Import**.

<img src="./images/image-20220601123243439.png" alt="image-20220601123243439" style="zoom:50%;" />

Now we have the Logistics Dashboard on Amazon Managed Grafana. This dashboard refreshes every 5 seconds and runs a query against the materialized views that we previously created in Amazon Redshift.

![image-20220601123345968](./images/image-20220601123345968.png)



### Clean up

This is to delete all resources created as part of this workshop.

Go back to AWS CloudShell

https://us-east-1.console.aws.amazon.com/cloudshell/home?region=us-east-1

Go to working directory

```
cd amazon-redshift-streaming-workshop
```

Activate python virtual environment

```
source .venv/bin/activate
```

Destroy resources

```
cdk destroy --all
```

![image-20220601162314757](./images/image-20220601162314757.png)
