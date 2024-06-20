import RPi.GPIO as GPIO
import time

led = 21

#GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		GPIO.output(led, False)
		time.sleep(1)
		GPIO.output(led, True)
		time.sleep(1)

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
