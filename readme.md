# Main Scripts 
## door_lock.sh
The primary script runs multiple essential scripts simultaneously to enable all the door lock functionalities.
##  on_boot.py
The initial script that runs when the arduino is powered on is responsible for both generating the account creation code and producing the token utilized for communication.
## sync_data.py
This file contains the script that synchronizes the data with the distant server, it is executed periodically to keep the data up to date with the data existing in the server.

## rasp_socket.py
This script establishes a socket connection with the distant server in order to log different operations occuraing on the door lock, for example in case of opening the door, it also allows the client to open the door using the web interface.

## Alphabot2/python/Joystick.py
This file triggers the execution of the script charged with detecting the faces, it is created to trigger the face detection only when it is necessary

## Alphabot2/python/Joystick2.py
This script triggers the deletion of the date from the local raspberry, it is meant as a simulation of the mechanism for which the data is erased in case the raspberry is stolen

## nfc_listener.py
This script is charged with reading NFC tags and recognizing them, in case of failure in authentification a request is forwarded to the server to verify the credentials.

## Flask 
Is a small web server which provides an interface for the user, to change the WIFI credentials in case of a change.

# Other scripts
## arduino_accept
Send a message to the arduino to open the door (normally it should have been through Radio but with issues we simulated it with serial communication)
## arduino_refuse
Send a message to the arduino to print a "Try Again!" message indicating to the user that the authentification failed (normally it should have been through Radio but with issues we simulated it with serial communication)

