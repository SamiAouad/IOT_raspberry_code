#!/usr/bin/python

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      
      
def run_code(filename):
    exec(open('nfc_listener.py').read())


# Create two threads as follows
try:
   _thread.start_new_thread( run_code, ('face_detection.py',))
except:
   print ("Error: unable to start thread")

while 1:
   pass
