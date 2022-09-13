#!/bin/bash
unset password
prompt="Enter Redshift admin password:"
while IFS= read -p "$prompt" -r -s -n 1 char
do
    if [[ $char == $'\0' ]]
    then
        break
    fi
    prompt='*'
    password+="$char"
done
aws secretsmanager create-secret \
    --name REDSHIFT_PASSWORD \
    --description "Redshift password" \
    --secret-string "{\"username\":\"admin\",\"password\":\"$password\"}"
sudo npm install -g aws-cdk@latest
git clone https://github.com/aws-samples/amazon-redshift-streaming-workshop --branch asean-roadshow
cd amazon-redshift-streaming-workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk deploy --all --require-approval never
