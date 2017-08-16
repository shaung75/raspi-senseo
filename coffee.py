#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgi, cgitb
#import RPi.GPIO as GPIO
import time
import subprocess
#from sys import stdout
cgitb.enable()

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT) 	# Power
#GPIO.setup(13, GPIO.OUT)	# Button
#GPIO.setup(15, GPIO.IN)		# LED

print("Cache-Control: no-cache, no-store, must-revalidate")
print("Pragma: no-cache")
print("Expires: 0")
print("Content-Type: application/json;charset=UTF-8")
print()
print("{ \"version\": \"1.0\", \"response\": { \"outputSpeech\": { \"type\": \"PlainText\", \"text\": \"Hahaha! She won't make you one so let me do it for you instead.\"} }}")
#stdout.flush()
subprocess.Popen(['python', 'mkcoffe.py'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

# turn on machine
#GPIO.output(11,False)
#time.sleep(0.5)
#GPIO.output(11,True)

# wait for warmup
#print("warming...\n")
#time.sleep(60)

# Get some brew on
#print("Brewing...\n")
#GPIO.output(13, False)
#time.sleep(0.5)
#GPIO.output(13, True)

# Turn off machine
#time.sleep(10)
#print("Turning off in 10")
#stdout.flush()
#GPIO.output(11, False)
#time.sleep(0.5)
#GPIO.output(11, True)
#print("bye")
#GPIO.cleanup()
