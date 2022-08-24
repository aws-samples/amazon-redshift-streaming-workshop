# ASEAN Roadshow Workshop



In this hands-on session, we will show how easy it is to build a serverless analytics solution using AWS. We will create a logistics dashboard using Amazon Quicksight to provide augmented intelligence and situational awareness for a logistics operations team. It connects to Amazon Redshift Serverless, a modern cloud data warehouse which unifies both near-realtime and historical data for easy analysis.



![image-20220601123345968](./assets/images/image-20220601123345968.png)



### 1 Infrastructure Provisioning using and Cloudshell

Note: This workshop will work for any AWS region where AWS Cloudshell is available. However the workshop's instructions will be using the us-east-1 region (This can also be deployed in regions without Cloudshell but will require additional steps to provision an EC2 Linux deployment instance.) 

Note: In order for you to run this code you will need elevated privileges into the AWS account you are using.

1.1 Login to the AWS Console.

https://console.aws.amazon.com/console/home

1.2 Open Cloudshell

https://console.aws.amazon.com/cloudshell/home

1.3 Download install script

```bash
wget https://raw.githubusercontent.com/aws-samples/amazon-redshift-streaming-workshop/asean-roadshow/assets/scripts/install.sh
```

1.4 Run installation script

```
sh install.sh
```

1.5 Enter Redshift admin password. 

Note: Passwords must be at least 8 chars, and contain at least one uppercase letter, one lowercase letter, and one number. Take note of this password as this will be used throughout the workshop. (i.e. Password123)





