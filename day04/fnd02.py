import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = (20,21,22,23,24,25,26)

for a in pin:
	GPIO.setup(a, GPIO.OUT)
	GPIO.output(a, 0)

list = {
	'0':(1,1,1,1,1,1,0,0), # 0
	'1':(0,1,1,0,0,0,0,0), # 1
	'2':(1,1,0,1,1,0,1,0), # 2
	'3':(1,1,1,1,0,0,1,0), # 3
	'4':(0,1,1,0,0,1,1,0), # 4
	'5':(1,0,1,1,0,1,1,0), # 5
	'6':(1,0,1,1,1,1,1,0), # 6
	'7':(1,1,1,0,0,1,0,0), # 7
	'8':(1,1,1,1,1,1,1,0), # 8
	'9':(1,1,1,1,0,1,1,0) # 9
	}

try:
	for index in range(0,10):
		s = str(index)
		for loop in range(0, 7):
			GPIO.output(pin[loop], list[s][loop])
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
