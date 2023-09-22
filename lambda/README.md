# Code in the Lambda Functions

The `/lambda` directory is here to show the code that can be used in a Lambda Function. I used the other files to get started and for testing, but eventually wrote everything else in AWS.

You'll need some familiarity with Lambda functions and AWS to get this done.

# Requirements

## Layers

AWS `Layers` must be created and uploaded to each function for using the external libraries.

### Python (Keep)

Install the following packages to a local directory with:

```
pip install --target ./python boto3 gkeepapi python-dotenv "urllib3<2"
```

Then create a zip file with the results to look like this:

```
python-lambda-layer.zip
└── python
    ├── __pycache__
    ├── bin
    ├── botocore
    ├── charset_normalizer
    ...
```

### NodeJS (AnyList)

Install the `dotenv` and `anylist` packages. Then create a zip file with results to look like this:

```
nodejs-lambda-layer.zip
└── nodejs
    └── node_modules
        ├── @sindresorhus
        ├── @szmarczak
        ├── @types
        ├── ansi-regex
        ├── anylist
        ...
```

## Environment Variables

The following environment variables are required:

```
# Python
KEEP_LIST_NAME
GOOGLE_USERNAME
GOOGLE_APP_PASSWORD

# NodeJS
ANYLIST_LIST_NAME
ANYLIST_USERNAME
ANYLIST_PASSWORD
```

Store them securely, like in AWS Secrets manager. See https://github.com/kiwiz/gkeepapi and https://github.com/codetheweb/anylist for usage.

## Azure Roles

For the Python Lambda to POST to the NodeJS Lambda, you'll need to add an AWS role to do so (Through IAM).
Here is the policy granted to the Python Lambda:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:[...]:NodeJSLambda"
        }
    ]
}

The key is that it needs `InvokeFunction` permissions on the NodeJS Lambda resource.
```
