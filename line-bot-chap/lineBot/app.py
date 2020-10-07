import json, os, logging
from RandomWordGenerator import RandomWord
from requests import post

rw = RandomWord(max_word_size = 6)
rwgenerated = rw.generate()
accessToken = os.environ['ACCESS TOKEN']

def reply(accessToken, replyToken):
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {Authorization: 'Bearer '+ accessToken}
    data = {
    "replyToken":replyToken,
    "messages":[
        {
            "type":"text",
            "text":rwgenerated
        }
    ]}
    return post(url = url, headers = headers, data = data)

def answer(event, context):


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
