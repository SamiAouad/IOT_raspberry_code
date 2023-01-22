import requests
import cv2
import json
import base64
import os
import schedule
import time

URL = 'http://192.168.238.179:5000/api/V1.0.0/'

def get_images(t):
    token_file = open("./data/token.json")
    token = json.load(token_file)
    try:
       result = requests.get(URL + "devices/sync/rasp",  headers={"Authorization": "Bearer " + token})
    except:
       print("server is unreachable")
       return
    users = result.json()["data"]
    
    for user in users:
        os.remove('data/nfc_ids.json')
        with open('data/nfc_ids.json', 'a') as f:
            f.write(user["badgeId"] + "\n")
        with open("./data/images/"+user["id"]+".jpg", "wb") as fh:
            fh.write(base64.decodebytes(bytes(user["image"], "utf-8")))


schedule.every().day.at("00:56").do(get_images,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
