# piezo
import RPi.GPIO as GPIO
import time

piezoPin = 17
melody = [131, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

# 아날로그 출력을 위한 객체생성 (440HZ 출력)
Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		num = int(input('도(0)레(1)미(2)파(3)솔(4)라(5)시(6)도(7)> '))
		if(num==0 or num==1 or num==2 or num==3 or num==4 or num==5 or num==6 or num==7):
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[num])
			time.sleep(0.3)
			Buzz.stop()
		else:
			pass
except KeyboardInterrupt:
	GPIO.cleanup()
