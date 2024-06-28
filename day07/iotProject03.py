# qt5로 IOT 시스템
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

# LED 값
red = 2
blue = 3
green = 4
switch = 16
piezoPin = 17
servoPin = 18
SERVO_MAX_DUTY = 12		# 서보모터 각도 최대 180도
SERVO_MIN_DUTY = 3		# 서보모터 각도 최소 0도

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50) # 서보핀 PWM모드 50Hz로 사용
servo.start(0)	# 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작 x
Buzz = GPIO.PWM(piezoPin, 440)

form_class = uic.loadUiType("design03.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):			# 생성자, 첫번째 인자는 self
		super().__init__()	# 부모클래스 생성자(QWidgets)
		self.setupUi(self)
	# 부저 스타트
	def buzz_start(self):
		Buzz.start(50)
		Buzz.ChangeFrequency(131)
		time.sleep(0.3)
		Buzz.stop()
	# 서보모터 제어 함수
	def servo_open(self):
		degree = 0
		if degree == 0:
			degree = 180
			duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
			self.textEdit.setText("Door Open")
			servo.ChangeDutyCycle(duty)
		elif degree == 180:
			degree = 0
			duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
			self.textEdit.setText("Door Close")
			servo.ChangeDutyCycle(duty)

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
