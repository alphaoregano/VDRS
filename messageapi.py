import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'




# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':EON386947EGSUZ4VEMIL8AWQX8RQW6UH,
  'secret':FB2K25JVMFPEM310,
  'usetype':useType,
  'phone': 8355996202,
  'message':textMessage,
  'senderid':usaidh99@gmail.com
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print response.text



<?php
//post
$url="https://www.sms4india.com/api/v1/sendCampaign";
$message = urlencode("message-text");// urlencode your message
$curl = curl_init();
curl_setopt($curl, CURLOPT_POST, 1);// set post data to true
curl_setopt($curl, CURLOPT_POSTFIELDS, "apikey=[povided-api-key]&secret=[provided-secret-key]&usetype=[stage or prod]&phone=[to-mobile]&senderid=[active-sender-id]&message=[$message]");// post data
// query parameter values must be given without squarebrackets.
 // Optional Authentication:
curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
$result = curl_exec($curl);
curl_close($curl);
echo $result;
?>
