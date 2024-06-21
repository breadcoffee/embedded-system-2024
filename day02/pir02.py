import RPi.GPIO as GPIO
import time

pirPin = 25
red = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(red, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
			print("Detected")
			GPIO.output(red, False)
			time.sleep(0.5)
		else:
			GPIO.output(red, True)

except KeyboardInterrupt:
	GPIO.cleanup()
