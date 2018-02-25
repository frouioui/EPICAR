import RPi.GPIO as GPIO
from time import sleep
import requests
from playsound import playsound
import time

def get_nbr_likes():
	r = requests.get('https://www.googleapis.com/youtube/v3/videos?id=' + yt + '&key=' + key + '&part=statistics').json()
	like = int(r['items'][0]['statistics']['likeCount'])
	return like

def get_nbr_dislikes():
	r = requests.get('https://www.googleapis.com/youtube/v3/videos?id=' + yt + '&key=' + key + '&part=statistics').json()
	dislike = int(r['items'][0]['statistics']['dislikeCount'])
	return dislike

# def get_distance(trig_pin, echo_pin):
# 	distance_list = []
# 	distance_average = 0
# 	i = 0
# 	while i < 10:
# 		GPIO.output(trig_pin, True)
# 		time.sleep(0.00001)
# 		GPIO.output(trig_pin, False)
# 		while GPIO.input(echo_pin) == 0:
# 			pulse = time.time()
# 		while GPIO.input(echo_pin) == 1:
# 			end_pulse = time.time()
# 		distance_list.append(round((end_pulse - pulse) * 340 * 100 / 2, 1))
# 		i = i + 1
# 	for dist in distance_list:
# 		distance_average = distance_average + dist
# 	return distance_average / 10


print("Developper's key = ")
key = raw_input()
print("Live ID = ")
yt = raw_input()

## INIT ##
# GPIO.setmode(GPIO.BCM)

# trig_forward = 23
# echo_forward = 24

# GPIO.setup(trig_forward, GPIO.OUT)
# GPIO.setup(echo_forward, GPIO.IN)

# GPIO.output(trig_forward, False)


current_likes = get_nbr_likes()
current_dislikes = get_nbr_dislikes()
tmp = 0

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

while (1):
	tmp = current_likes
	current_likes = get_nbr_likes()
	if current_likes > tmp:
		playsound("like.ogg")
	tmp = current_dislikes
	current_dislikes = get_nbr_dislikes()
	if current_dislikes > tmp:
		playsound("dislike.ogg")

	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
# 	#if get_distance(trig_forward, echo_forward) <= 15:
# 		#trop proche d'un mur
# 	##avance