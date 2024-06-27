# qt5로 IOT 시스템
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

red = 21
blue = 22
green = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


form_class = uic.loadUiType("design.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):			# 생성자, 첫번째 인자는 self
		super().__init__()	# 부모클래스 생성자(QWidgets)
		self.setupUi(self)
		# 이벤트 함수 등록

	def red_on(self):
		GPIO.output(red, False)
		self.textEdit.setText("red on")
	def blue_on(self):
		print("blue on")
		self.textEdit.setText("blue on")
	def green_on(self):
		print("green on")
		self.textEdit.setText("green on")

if __name__ == "__main__":
	app = QApplication(sys.argv)	# 프로그램 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass()인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행
