#proximitySensor_HC-SR04.py

# Inpu GPIO pins work at 3.3v range and need to be reduced from 5v to 3.3v.
# 3.3V / 5V = R2 / (R1+R2) --> R2 = 2 * R1
# Echo-1k-pin4-2k-GND

import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers (BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 17
pinEcho = 4

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
        # By setting trigger High for 0.01 ms we're sending a singnal 40kHz
	# set Trigger to HIGH
	GPIO.output(pinTrigger, True)
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

        #Initialising variables
	startTime = time.time()
	stopTime = time.time()

        # Echo will go high (1) when starts receiving the signal 
	# save start time
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

        # Echo will go low (0) when stops receiving the signal 
	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	print ("Distance: %.1f cm" % distance)
	time.sleep(1)
