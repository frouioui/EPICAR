import RPi.GPIO as GPIO
import time

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

##### BEGINNING #####
GPIO.setmode(GPIO.BCM)

Trig = 20	# Pin Trig (HC-SR04 - GPIO 23)
Echo = 21	# Sortie Echo (HC-SR04 - GPIO 24)

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

GPIO.output(Trig, False)

print "Distance: ", get_distance(Trig, Echo), " cm"

GPIO.cleanup()
