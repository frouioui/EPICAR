import RPi.GPIO as GPIO
from time import sleep
import time

Motor1A = 16
Motor1B = 18
Motor1E = 22
Motor2A = 19
Motor2B = 21
Motor2E = 23

Trigcenter = 38
Echocenter = 40
Trigright = 38
Echoright = 40
Trigleft = 38
Echoleft = 40
x = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
p = GPIO.PWM(22, 50)
p.start(85)

def get_distance(trig_pin, echo_pin):
	distance_list = []
	distance_average = 0
	i = 0
	while i < 10:
		GPIO.output(trig_pin, True)
		time.sleep(0.00001)
		GPIO.output(trig_pin, False)
		while GPIO.input(echo_pin) == 0:
			pulse = time.time()
		while GPIO.input(echo_pin) == 1:
			end_pulse = time.time()
		distance_list.append(round((end_pulse - pulse) * 340 * 100 / 2, 1))
		i = i + 1
	for dist in distance_list:
		distance_average = distance_average + dist
	return distance_average / 10

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

GPIO.output(Trig, False)

print "Distance: ", get_distance(Trig, Echo), " cm"

while x == 0:
	if get_distance(Trigcenter, Echocenter) > 20 and
	get_distance(Trigright, Echoright) > 20 and
	get_distance(Trigleft, Echoleft) > 20:
		print "Going forwards"
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.HIGH)
	else:
		while get_distance(Trigcenter, Echocenter) < 20 and
		get_distance(Trigright, Echoright) < 20 and
		get_distance(Trigleft, Echoleft) < 20:
			GPIO.output(Motor1A,GPIO.LOW)
			GPIO.output(Motor1B,GPIO.LOW)
			GPIO.output(Motor1E,GPIO.LOW)
			GPIO.output(Motor2A,GPIO.HIGH)
			GPIO.output(Motor2B,GPIO.LOW)
			GPIO.output(Motor2E,GPIO.HIGH)
			sleep(0.35)
GPIO.cleanup()
