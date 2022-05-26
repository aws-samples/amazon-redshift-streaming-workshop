
# Welcome to your CDK Python project!

Login to the AWS Console.

Open Cloudshell

Clone this git repository

Create a virtualenv:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```


Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Check the stacks and resources that CDK will deploy

```
$ cdk diff
```

Deploy all stacks

```
$ cdk deploy --all
```