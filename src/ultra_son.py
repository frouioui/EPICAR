import RPi.GPIO as GPIO
import time

def get_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    while GPIO.input(echo_pin) == 0:
      pulse = time.time()

    while GPIO.input(echo_pin) == 1:
       end_pulse = time.time()

    distance = round((end_pulse - pulse) * 340 * 100 / 2, 1)
    return distance

##### BEGINNING #####
GPIO.setmode(GPIO.BCM)

Trig = 23         # Pin Trig (HC-SR04 - GPIO 23)
Echo = 24         # Sortie Echo (HC-SR04 - GPIO 24)

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

GPIO.output(Trig, False)

print "Distance: ", get_distance(Trig, Echo), " cm"

GPIO.cleanup()