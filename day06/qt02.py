# qt5로 LED ON/OFF
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("btn01.ui")[0]

# windowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):			# 생성자, 첫번째 인자는 self
		super().__init__()	# 부모클래스 생성자(QWidgets)
		self.setupUi(self)
		# 이벤트 함수 등록
		self.btn_1.clicked.connect(self.btn1Function)
		self.btn_2.clicked.connect(self.btn2Function)

	def btn1Function(self):
		print("LED ON")
	def btn2Function(self):
		print("LED OFF")
	def slot1(self):
		print("EXIT!!!")

if __name__ == "__main__":
	app = QApplication(sys.argv)	# 프로그램 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass()인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행
