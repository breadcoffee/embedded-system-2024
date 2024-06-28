# qt5로 IOT 시스템
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QTime
import RPi.GPIO as GPIO
import time

# LED 값
red = 2
blue = 3
green = 4
switch = 16
piezoPin = 17
servoPin = 12
trigPin = 14
echoPin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

servo = GPIO.PWM(servoPin, 50) # 서보핀 PWM모드 50Hz로 사용
servo.start(0)	# 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작 x
Buzz = GPIO.PWM(piezoPin, 440)

form_class = uic.loadUiType("design04.ui")[0]

def measure():
	GPIO.output(trigPin, True)
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()

	while GPIO.input(echoPin) == False:
		start = time.time()
	while GPIO.input(echoPin) == True:
		stop = time.time()
	elapsed = stop - start
	distance = (elapsed * 19000) / 2
	return distance
def door_open():
	servo.ChangeDutyCycle(10)
def door_close():
    servo.ChangeDutyCycle(5)

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):			# 생성자, 첫번째 인자는 self
		super().__init__()	# 부모클래스 생성자(QWidgets)
		self.setupUi(self)
		self.timer = QTimer(self)
	def ultra_start(self):
		self.timer.timeout.connect(self.update_distance)
		self.timer.start(1000)
	def ultra_stop(self):
		self.timer.stop()
	# 부저 스타트
	def buzz_start(self):
		Buzz.start(50)
		Buzz.ChangeFrequency(131)
		time.sleep(0.3)
		self.textEdit_2.setText("띵동 띵동 문열어주세요~")
		Buzz.stop()
	# 서보모터 제어 함수
	def servo_open(self):
		self.textEdit_2.setText("문이 열렸습니다!")
		door_open()
	def servo_close(self):
		self.textEdit_2.setText("문이 닫혔습니다!")
		door_close()
	# 거리 감지 센서
	def measure(self):
		GPIO.output(trigPin, True)
		time.sleep(0.00001)
		GPIO.output(trigPin, False)
		start = time.time()

		while GPIO.input(echoPin) == False:
			start = time.time()
		while GPIO.input(echoPin) == True:
			stop = time.time()
		elapsed = stop - start
		distance = (elapsed * 19000) / 2
		return distance
	def update_distance(self):
		distance = measure()
		print(distance)
		if distance <= 5:
			self.textEdit_3.setText("문이 열립니다")
			door_open()
		else:
			self.textEdit_3.setText("문이 닫힙니다")
			door_close()

	# LED 이벤트 함수 등록
	def red_on(self):
		GPIO.output(red, False)
		GPIO.output(blue, True)
		GPIO.output(green, True)
		self.textEdit.setText("Red on")
	def blue_on(self):
		GPIO.output(blue, False)
		GPIO.output(red, True)
		GPIO.output(green, True)
		self.textEdit.setText("Blue on")
	def green_on(self):
		GPIO.output(green, False)
		GPIO.output(red, True)
		GPIO.output(blue, True)
		self.textEdit.setText("Green on")
	def led_off(self):
		GPIO.output(red, True)
		GPIO.output(blue, True)
		GPIO.output(green, True)
		self.textEdit.setText("LED off")

if __name__ == "__main__":
	app = QApplication(sys.argv)	# 프로그램 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass()인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행
