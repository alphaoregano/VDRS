# Importing all necessary libraries 
import cv2 
import os
import time
import urllib
import numpy as np
import ssl
import threading, time, sys
from os import path
import requests
import base64
import json
import importlib
from multiprocessing.pool import ThreadPool

mod = ''
func = ''
#country = 'us'

#--------------------------------OpenALPR.py------------------------------------------

def recog(name, country):
    
    IMAGE_PATH = name
    #print('Reading: ' + name)
    SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    
    print("Sending: " + name)
    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country='+country+'&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)
    
    mydict = json.dumps(r.json(), indent=2)
    
    d = json.loads(mydict)
    vehicles = []
    #print(d)
    try:
        for i in range(0,len(d["results"])):
                '''
                print("Details for: " + name)
                print("Car#" + str(i+1))
                print("Plate No: " + d["results"][i]["plate"])
                print("Color: " + d["results"][i]["vehicle"]["color"][0]["name"])
                print("Make: " + d["results"][i]["vehicle"]["make"][0]["name"])
                print("Body Type: " + d["results"][i]["vehicle"]["body_type"][0]["name"])
                print("Year: " + d["results"][i]["vehicle"]["year"][0]["name"])
                print("Model: " + d["results"][i]["vehicle"]["make_model"][0]["name"])
                print("\n")
                '''
                
                vehicles.append((d["results"][i]["plate"],
                                 d["results"][i]["vehicle"]["make"][0]["name"],
                                 d["results"][i]["vehicle"]["body_type"][0]["name"],
                                 d["results"][i]["vehicle"]["year"][0]["name"],
                                 d["results"][i]["vehicle"]["make_model"][0]["name"]))
    except KeyError:
        print('')
    import os
    #if os.path.exists(name):
    #  os.remove(name)
    global mod
    global func
    fun = getattr(mod, func)
    fun(vehicles)

#--------------------------------livecaresys.py------------------------------------------


def livecaresysfunc(url, delay, m, fun, country):
    global mod
    global func
    func = fun
    mod = importlib.import_module(m)
    x = []
    cam = cv2.VideoCapture(0)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
      
    try: 
        if not os.path.exists('data'): 
            os.makedirs('data') 
      
    except OSError: 
        print ('Error: Creating directory of data') 

    currentframe = 0
    j = 0
    r = requests.get(url, auth=('user', 'password'), stream=True)

    if(r.status_code == 200):
        byte = bytes()
        for chunk in r.iter_content(chunk_size=1024):
            byte += chunk
            a = byte.find(b'\xff\xd8')
            b = byte.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = byte[a:b+2]
                byte = byte[b+2:]
                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                x.append(0)
                name = './data/frame' + str(currentframe) + '.jpg'
                #print ('Creating...' + name)

                cv2.imwrite(name, frame)

                x[j] = threading.Thread(target = recog, args=(name,country,))
                x[j].start()
                currentframe += 1
                time.sleep(delay)

    else:
        print("Received unexpected status code {}".format(r.status_code))
    
      
    cam.release() 
    cv2.destroyAllWindows()
