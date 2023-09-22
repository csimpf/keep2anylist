import sys
import os
import datetime
import boto3
import json

from dotenv import load_dotenv

import gkeepapi

import json

def lambda_handler(event, context):
    # load_dotenv() # Locally
    
    keep = gkeepapi.Keep()
    success = keep.login(os.environ["GOOGLE_USERNAME"], os.environ["GOOGLE_APP_PASSWORD"])
    
    # keep.find returns a generator - use next(gnotes) to get the first in the list
    gnotes = keep.find(query=os.environ["KEEP_LIST_NAME"])
    
    shopping_note = next(gnotes)
    
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # shopping_note.text = shopping_note.text + "\n Last update:"+ curr_date
    # print(dir(shopping_note.items[0]))
    
    # item_list = shopping_note.text[:shopping_note.text.index("Last update:")].split('\n')[:-1]
    
    if len(shopping_note.items) == 0:
        return {
            'statusCode': 200,
            'body': "No items to sync, done"
        }
    
    # send item_list to lambda to update AnyList
    list_to_send = []
    
    for item in shopping_note.items:
        list_to_send.append(item.text.title())
    
    print("Going to send this to AnyList:")
    print(','.join(list_to_send))
    
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='NodeJSLambda',
        Payload='{"items": ' + json.dumps(list_to_send) + '}'
    )
    
    response_payload = json.load(response['Payload'])
    
    print(response_payload)
    
    if response_payload['statusCode'] == 200:
        print("Payload Success! Removing from Keep")
        for item in shopping_note.items:
            item.delete()
        keep.sync()
    else:
        print("Payload Failure")
        print(response_payload)
    
    
    return {
        'statusCode': 200,
        'body': "Sync Complete"
    }
    