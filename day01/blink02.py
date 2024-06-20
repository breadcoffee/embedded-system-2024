import RPi.GPIO as GPIO
import time

red = 21
blue = 23
green = 24

#GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
	while True:
		# red 핀
		GPIO.output(red, False)
		time.sleep(1)
		GPIO.output(red, True)
		time.sleep(1)
		# blue 핀
		GPIO.output(blue, False)
		time.sleep(1)
		GPIO.output(blue, True)
		time.sleep(1)
		# green 핀
		GPIO.output(green, False)
		time.sleep(1)
		GPIO.output(green, True)
		time.sleep(1)

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
