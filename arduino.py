#!/usr/bin/env python3
import serial
import time
import socketio
from time import sleep 

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
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
    ser.reset_input_buffer()
    failed = 0
    code = -1
    ser.write(b"This is a key\n")
    while failed < 5:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            code = int(line)
            if not line:
                continue
            if code == -1:
                failed += 1
                print("invalid key")
                ser.write(b"This is key\n")
            elif code == 1:
                print ("the door has opened")
                try:
                   sio.emit("door_opened")
                except:
                   pass
                continue
            elif code == 0:
                print ("the door has closed")
                break
            else:
                print("an error has occured")
                ser.write(b"This s a key\n")
        else:
            ser.write(b"This is a key\n")

