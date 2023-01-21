import requests
import json
import os
import platform
import numpy as np
URL = 'http://192.168.238.179:5000/api/V1.0.0/'

def get_credentials(hostname):
    result = requests.post(URL + "devices", json={'name': hostname+str(np.random.randint(1000, size=1)[0])})
    if result.status_code == 200:
        data = result.json()
        print(result)
        with open('data/device.json', 'w') as f:
            json.dump(data["device"], f)
        with open('data/admin.json', 'w') as f:
            json.dump(data["admin"], f)
    else:
        print ("An error has occured on the server")
        exit()
        
def get_token(email, password):
    result = requests.post(URL + "users/login", json={"email": email, "password": password})
    if result.status_code == 200:
        data = result.json()
        with open('data/token.json', 'w') as f:
            json.dump(data["token"], f)
    
    
    
    
if not os.path.exists("data/admin.json"):
    print("machine not registered")
    device_name = platform.node()
    get_credentials(device_name)
    print ("./data/device.json and ./data/admin.json created")

if not os.path.exists("data/token.json") :
    print("no token found")
    file = open("data/admin.json") 
    data = json.load(file)
    get_token(data['email'], data['password'])
    print("./data/token.json created")
