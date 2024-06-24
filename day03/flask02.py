from flask import Flask

app = Flask(__name__) # name 이름을 통한 flask객체생성

@app.route("/")			# 라우팅을 위한 뷰함수 등록
def hello():
	return "Hello World"

@app.route("/name")
def name():
	return "<h1>my name is Lee joowon</h1>"

@app.route("/age")
def age():
	return "<h1> 27 year's old</h1>"

if __name__ == "__main__":	# 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다.
	app.run(host="0.0.0.0", port="10111",  debug=True) # 실행
