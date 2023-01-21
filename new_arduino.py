#!/usr/bin/env python3
import serial
import time
import socketio
from time import sleep

key = 1234

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')
    sio.emit('initial_connection', {'device': {
        'id': '4ed3309b-61c2-47d9-a69e-112c4d8164d9',
        'name': 'Raspberry Pi'
    }})



@sio.event
def disconnect():
    print('disconnected from server')

try:
   sio.connect('http://localhost:5000')
   sleep(2)
   sio.emit('get_clients')

   sio.wait()
except:
    pass


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()
    opened = False
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').rstrip()
            except UnicodeDecodeError:
                line = ser.readline().decode('utf-8').rstrip()
            if line.isdigit() and not opened:
                challenge = int(line)
                print("received challenge: ", challenge)
                password = ((challenge + key) * 1574) % 99
                print("secret is:", password)
                message = str(password) + "\n"
                ser.write(bytes(message, encoding='utf8'))
            elif line:
                print(line)
                if line == "opened":
                    opened = True
                elif line == "closed":
                    opened = False
                    break
