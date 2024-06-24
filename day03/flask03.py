# URL 접속을 /led/on, /led/off 로 접속하면 led를 on, off하는 웹페이지
from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__) # name 이름을 통한 flask객체생성
led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route("/")			# 라우팅을 위한 뷰함수 등록
def hello():
	return "Hello LED ON/OFF > /led/on or /led/off"

@app.route("/led/<state>")
def led_onoff(state):
	if state == "on":
		GPIO.output(led, False)
		return "<h1>led on</h1>"
	elif state == "off":
		GPIO.output(led, True)
		return "<h1>led off</h1>"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO clean"

if __name__ == "__main__":	# 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다.
	app.run(host="0.0.0.0", port="10111",  debug=True) # 실행
