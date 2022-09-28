#!/bin/bash
set -e
sudo -u ec2-user -i <<'EOF'
# PARAMETERS
ENVIRONMENT=python3
source /home/ec2-user/anaconda3/bin/activate "$ENVIRONMENT"
pip install glom
pip install --upgrade boto3 
pip install --upgrade awscli
pip install --upgrade redshift_connector
pip install sqlalchemy
pip install sqlalchemy-redshift
pip install ipython-sql
source /home/ec2-user/anaconda3/bin/deactivate
wget https://raw.githubusercontent.com/aws-samples/amazon-redshift-streaming-workshop/asean-roadshow/assets/scripts/redshift_lab.ipynb -P /home/ec2-user/SageMaker/
wget https://raw.githubusercontent.com/aws-samples/amazon-redshift-streaming-workshop/asean-roadshow/assets/scripts/redshift_completed.ipynb -P /home/ec2-user/SageMaker/
EOF