import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.output(Motor1A,100)
GPIO.output(Motor1B,0)
GPIO.output(Motor1E,100)

sleep(2)

GPIO.output(Motor1E,0)

GPIO.cleanup()
