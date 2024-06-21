import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True) 		# 10us 동안 High레벨로 triger를 출력하여 초음파 발생 준비
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()					# 현재시간 저장

	while GPIO.input(echoPin) == False:	# echo가 없으면
		start = time.time()				# 현재시간을 start 변수에 저장하고
	while GPIO.input(echoPin) == True:	# echo가 있으면
		stop = time.time()				# 현재 시간을 stop변수에 저장
	elapsed = stop - start				# 걸린 시간을 구하고
	distance = (elapsed * 19000) / 2	# 초음파 속도를 계산

	return distance

# 핀설정
trigPin = 14
echoPin = 15
piezoPin = 13
melody = [329.6, 311.1, 329.6, 311.1, 329.6, 246.9, 293.6, 261.6, 220]

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		distance = measure()
		print("Distance: %.2f cm" %distance)
		time.sleep(0.2)

		if(distance <= 30 and distance > 15): # 30~16cm
			Buzz.start(50)
			Buzz.ChangeFrequency(523)
			time.sleep(0.3)
			Buzz.stop()
			time.sleep(0.3)
		elif(distance <= 15 and distance > 5): # 15~6cm
			Buzz.start(50)
			Buzz.ChangeFrequency(523)
			time.sleep(0.15)
			Buzz.stop()
			time.sleep(0.1)
		elif(distance <= 5): # 5cm 이하
			Buzz.start(50)
			Buzz.ChangeFrequency(523)
			time.sleep(0.05)
			Buzz.stop()
			time.sleep(0.01)
		else:
			Buzz.stop()
			time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
