import RPi.GPIO as GPIO
import time

# 0~9까지 1 byte hex값
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [20, 21, 22, 23, 24, 25, 26] # a~g led 핀
fndSels = [5, 6, 7, 8]
count = 0

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data, sel): # a~g 불을 점등해 숫자 만드는 함수
	for i in range(0, 7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
		for j in range(3, -1, -1):		# 해당 자리 수의 fnd만 on
			if j == sel:
				GPIO.output(fndSels[j], 0)
			else:
				GPIO.output(fndSels[j], 1)

try:
	while True:
		count += 1
		d1000 = count / 1000
		d100 = count  % 1000 /100
		d10 = count % 100 / 10
		d1 = count % 10
		d = [d1000, d100, d10, d1]
		for i in range(3, -1, -1):
			GPIO.output(fndSels[i], 0) # fnd 선택
			for j in range(0, 10):
				fndOut(int(d[i]), i)
				time.sleep(0.0005)

except KeyboardInterrupt:
	GPIO.cleanup()
