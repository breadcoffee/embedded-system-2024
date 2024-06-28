# qt5로 IOT 시스템
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time
import Adafruit_DHT.DHT11

# LED 값
red = 2
blue = 3
green = 4
# 온습도 센서
dht = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
sensor = Adafruit_DHT.DHT11

form_class = uic.loadUiType("design.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):			# 생성자, 첫번째 인자는 self
		super().__init__()	# 부모클래스 생성자(QWidgets)
		self.setupUi(self)

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
		GPIO.output(green, True)
		GPIO.output(red, True)
		GPIO.output(blue, True)
		self.textEdit.setText("LED off")
	def dht_start(self):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, dht)
		if humidty is not None and temperature is not None:
			self.textEdit.setText("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
		else:
			self.textEdit.setText("Try again!")

if __name__ == "__main__":
	app = QApplication(sys.argv)	# 프로그램 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass()인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행
