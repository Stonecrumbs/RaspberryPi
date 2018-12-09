#buttonImputAndPhoto.py

import RPi.GPIO as GPIO
import picamera
from time import sleep

GPIO.setmode(GPIO.BCM)

sleeptime = .1

lightPin = 4
buttonPin = 17

camera = picamera.PiCamera()

GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

try:
    while True:
        GPIO.output(lightPin, not GPIO.input(buttonPin))
        if not (GPIO.input(buttonPin)):
            camera.capture('Sample.jpg');
        sleep(sleeptime)
finally:
        GPIO.output(lightPin, False)
        GPIO.cleanup()
         
