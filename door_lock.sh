#!/bin/bash

python on_boot.py
python sync_data.py &
python rasp_socket.py &
python AlphaBot2/python/Joystick.py &
python AlphaBot2/python/Joystick2.py &
python nfc_listener.py &
flask run -h 192.168.238.230 &
(cd flask && flask run -h 192.168.238.230) &
