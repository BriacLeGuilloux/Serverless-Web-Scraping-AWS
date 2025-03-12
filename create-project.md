## Intialiser un projet cdk
"""sh
cdk init app --language python
npm install -g aws-cdk
"""

## source.bat
script that activates your virtual environment


## requirements.txt
Deploy the dependencies for the CDK application
construct is for building in aws


## requirements-dev.txt
Unit testing of CDK code

## cdk.json
Contains some general configuration

## app.py
This is the entry point for our stack. It initial.
You only have one app.py
app.synth() generate the infrastructure in the cloud

## .gitignore
Ignore some files when pushing to github


# unit is the test folder
__init__.py :
test_stock_notifier_stack.py: it confirms whether it creates a ressource.


# folder: stockerNotifier
it inherit the name of the projet
## stock_notifier_stack.py
stack is a building block



## Create local environments
"""sh
source .venv/bin/activate
"""

## Install cdk dependecies
"""
pip install -r requirements.txt
"""

## Connect to AWS account admin
"""
aws configure
"""


## Create some file in S3 to deploy cdk code
"""
cdk bootstrap
"""

## synthesize the CloudFormation template for this code.
"""
cdk synth
""" sh

## Deploy

""" sh
cdk deploy
"""




