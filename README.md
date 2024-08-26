# keep2anylist

Sync a Google Keep note with AnyList.

After Google [Dropped API support](https://help.anylist.com/articles/google-assistant-overview/) for 3rd party list apps, using AnyList was such a part of my workflow that I wanted to figure out how to pull Google Keep items and move them to AnyList.

There are two parts to this app - one gets details from a specified Google Keep list (keep-get/getKeep.py), and the other adds items to a specified AnyList app (anylist-post/index.js). I intend to put these in two AWS Lambda functions, run getKeep.py periodically (probably every hour), and make a POST request to the anylist function, so the code isn't exactly the same on Lambda but should get most of the way there. The Keep list is then cleared out.

Uses two unofficial apps (thanks!):

- https://github.com/kiwiz/gkeepapi
- https://github.com/codetheweb/anylist

# Requirements

Python 3.10
Node 18

# Setup

Initialise submodules:

```bash
git submodule update --init
```

# Libraries to install:

## Python

```bash
python3.10 -m pip install boto3 gkeepapi python-dotenv "urllib3<2"
```

# Tips

I have this public in case anybody else wants to see how this works and get it working for themselves.
I have added some notes (see `lambda/README.md`) so it makes a little bit of sense. See the `lambda` directory for how the Lambda Functions can be structured.
The rest of the code is here as reference, but at one point I just started programming in the AWS console and left this repo as-is.

Please create a PR or issue if you have any questions or need clarification 😊

## Lambda Setup

For Python, create a zip deployment package with these instructions: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-dependencies

In summary - install the packages using `pip install --target ...`, zip these files and the main getKeep.py script, and upload this to Lambda.
