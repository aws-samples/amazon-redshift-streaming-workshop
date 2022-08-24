#!/bin/bash
sudo npm install -g aws-cdk@latest
git clone https://github.com/aws-samples/amazon-redshift-streaming-workshop --branch asean-roadshow
cd amazon-redshift-streaming-workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap
cdk deploy --all --require-approval never