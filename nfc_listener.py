import nfc
import requests
import json
import RPi.GPIO as GPIO
import time
import sys
URL = 'http://192.168.238.179:5000/api/V1.0.0/'

CTR = 7
A = 8
B = 9
C = 10
D = 11
BUZ = 4


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(CTR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(A,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(B,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(C,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(D,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(BUZ,GPIO.OUT)

def beep_on():
        GPIO.output(BUZ,GPIO.HIGH)
def beep_off():
        GPIO.output(BUZ,GPIO.LOW)

def local_nfc(tag_id):
    file = open("data/nfc_ids.json") 
    data = json.load(file)
    for element in data['id']:
        if element == tag_id:
            return True
    return False

def on_startup(targets):
    print("Listening for NFC tags...")
    return targets

def on_connect(tag):
    print("Tag detected:")
    print("ID: " + str(tag.identifier.hex()))
    print("Type: " + tag.type)
    try:
        file = open("data/token.json")
        token = json.load(file)
        response = requests.post(URL + "devices/nfc-badge",headers={"Authorization": "Bearer " + token}, json={'badgeId': str(tag.identifier.hex())}, timeout=5)
        result = response.content
    except requests.exceptions.RequestException as e:
        result = local_nfc(str(tag.identifier.hex()))
        print(result)
    if result:
       exec(open('arduino_accept.py').read())
    else:
       exec(open('arduino_refuse.py').read())

clf = nfc.ContactlessFrontend('usb')
while True:
   test = clf.connect(rdwr={'on-connect': on_connect}, device='/dev/bus/usb/001/007')
