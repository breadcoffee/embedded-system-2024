import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = [20,21,22,23,24,25,26]

for a in pin:
	GPIO.setup(a, GPIO.OUT)

list = [
	[0,0,1,1,1,1,1,1], # 0
	[0,0,0,0,0,1,1,0], # 1
	[0,1,0,1,1,0,1,1], # 2
	[0,1,0,0,1,1,1,1], # 3
	[0,1,1,0,0,1,1,0], # 4
	[0,1,1,0,1,1,0,1], # 5
	[0,1,1,1,1,1,0,1], # 6
	[0,0,0,0,0,1,1,1], # 7
	[0,1,1,1,1,1,1,1], # 8
	[0,1,1,0,0,1,1,1], #9
	]

def Display(num):
	y = 0
	# 각 자리 숫자 추출
	fnd = [5,6,7,8]
	fnd[0] = int((num/100)/10)
	fnd[1] = int((num/100)%10)
	fnd[2] = int((num%100)/10)
	fnd[3] = int((num%100)%10)

	# 자리에 맞는 숫자 출력
	for i in range(4):
		if y == 0:
			d = fnd[y] # 해당 자리 숫자배열 출력
			for j in pin[3:]:
				if y+7 == j:
					GPIO.output(j, GPIO.LOW)
				else:
					GPIO.output(j, GPIO.HIGH)
		elif y == 1:
			d = fnd[y]
			for j in pin[3:]:
				if y+7 == j:
					GPIO.output(j, GPIO.LOW)
				else:
					GPIO.output(j, GPIO.HIGH)
		elif y == 2:
			d = fnd[y]
			for j in pin[3:]:
				if y+7 == j:
					GPIO.output(j, GPIO.LOW)
				else:
					GPIO.output(j, GPIO.HIGH)
		elif y == 3:
			d = fnd[y]
			for j in pin[3:]:
				if y+7 == j:
					GPIO.output(j, GPIO.LOW)
				else:
					GPIO.output(j, GPIO.HIGH)

		else:
			for k in pin[3:]:
				GPIO.output(k, GPIO.HIGH)

		# 숫자 원형 출력
		for x in list[d]:
			GPIO.output(20,x)
			GPIO.output(21,1)
			GPIO.output(21,0)
			GPIO.output(20,0)
			GPIO.output(22,1)
			GPIO.output(22,0)
		y+=1
		time.sleep(0.005)

try:
	while True:
		Display(1234)

except KeyboardInterrupt:
	GPIO.cleanup()
