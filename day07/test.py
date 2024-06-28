import RPi.GPIO as GPIO
import time
pin = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

p = GPIO.PWM(pin,50)
p.start(0)

try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(1)
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(10)
		time.sleep(3)
except KeyboardInterrupt:
	p.stop()

GPIO.cleanup()