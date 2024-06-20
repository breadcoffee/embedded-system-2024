import RPi.GPIO as GPIO

led = 21

#GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		text = input("입력 > ")
		if(text == "o"):
			GPIO.output(led, False)
		else:
			GPIO.output(led, True)

except KeyboardInterrupt: # Ctrl + C
	GPIO.cleanup()
