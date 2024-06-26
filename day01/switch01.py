import RPi.GPIO as GPIO
import time

red = 21
blue = 23
green = 24
switch = 16
count = 0

GPIO.setwarnings(False)
#GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(switch) == GPIO.HIGH:
			count += 1
			if (count == 1):
				print("push")
				break
				# red
				#GPIO.output(red, False)
				time.sleep(1)
			elif(count == 2):
				# blue
				GPIO.output(red, True)
				GPIO.output(blue, False)
				time.sleep(1)
			elif(count == 3):
				# green
				GPIO.output(blue, True)
				GPIO.output(green, False)
				time.sleep(1)
			elif(count == 4):
				# all off
				GPIO.output(green, True)
				time.sleep(1)
			else:
				count = 0

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
