# URL 접속
from flask import Flask, request

app = Flask(__name__) 

@app.route("/") 
def get():
    value1 = request.args.get("이름", "user")
    value2 = request.args.get("주소", "부산")
    return "이름 : " + value1 + "<br>주소 : " + value2

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="10011",  debug=True)
