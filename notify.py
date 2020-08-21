import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def get_response(number,color,make):
    x="Vehicle with number "+number+" and color "+color+" made by "+make+" has been spotted at Nagpada Signal."
    response = sendPostRequest(URL, 'EON386947EGSUZ4VEMIL8AWQX8RQW6UH', 'FB2K25JVMFPEM310', 'stage', '8104150837', 'usaidh99@gmail.com', x)

##"""
##  Note:-
##    you must provide apikey, secretkey, usetype, mobile, senderid and message values
##    and then requst to api
##"""
##

#view rawsmsind_python_sendcampaign_post.py hosted





