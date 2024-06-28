# embedded-system-2024
부경대 2024 IoT 개발자 과정 임베디드 시스템 학습 리포지토리

## 1일차
- 라즈베리파이 기초
    - 전압, 전류, 저항
        - 전류(Cuttent) : 전기(전자)의 흐름
        - 전압(Volt) : 전기 에너지의 압력, 전압이 높은 곳에서 낮은곳으로 흐르는 성질을 전압차, 전위차라고 함
        - 저항(Resister) : 전류가 흐르면서 생기는 손실
        - 옴의 법칙 : V = I * R
        - 전력(Power) : 시간당 전기가 하는 일(와트, W), P = V * I

    - GPIO 설정함수
        1. GPIO.setmode(GPIO.BOARD) - WPi
        2. GPIO.setmode(GPIO.BCM) - BCM
        3. GPIO.setup(channel, GPIO.mode)
            - channel : 핀번호, mode : IN/OUT
        4. GPIO.cleanup()
    - GPIO 출력함수
        1. GPIO.output(channel, state)
            - channel : 핀번호, state : HIGH/LOW or 1/0 or True/False
    - GPIO 입력함수
        1. GPIO.input(channel)
            - channel : 핀번호, 반환값 : H/L or 1/0 or T/F
    - 시간지연 함수
        1. time.sleep(secs)
            - secs : 1초 단위

    ![라즈베리파이 핀맵](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em001.png)

    - 인터럽트 : CPU가 특정 기능을 수행하는 도중에 급하게 다른 일을 처리하고자 할 때 사용할 수 있는 기능이다.
    
## 2일차
- 가상환경 
    - venv : 표준 라이브러리 중 하나로, 별도의 패키지나 모듈 환경을 제공하는 가상 환경을 만들기 위해 사용할 수 있다.
        - 장점
            1. 격리된 환경: 다양한 프로젝트에서 서로 다른 패키지나 Python 버전의 충돌 없이 작업할 수 있다.
            2. 버전 관리: 프로젝트별로 필요한 패키지와 그 버전을 쉽게 관리할 수 있다.
            3. 의존성 문제 해결: 각 프로젝트의 의존성을 명확하게 알 수 있으므로 배포나 협업 시 문제를 최소화 할 수 있다.
        - 단점
            - 추가적인 공간: 각 가상 환경마다 패키지를 복제하기 때문에 디스크 공간이 추가로 필요하다.
            - 관리: 여러 가상 환경을 사용하면 관리가 복잡해질 수 있다.
    ```python
        python -m venv env # venv 설치
        source ./env/bin/activate # venv 실행
        deactivate # venv 실행종료
        python -m venv --system-site-packages env # 패키지까지 같이 설치
    ```

## 3일차
- 릴레이 모듈
    - 릴레이는 전자석의 원리로 전류가 흐르면 자기장을 형성해 자기력으로 자석을 끌어 당겼다가 전류가 흐르지 않으면 자석을 놓는 원리이다.
    - 즉, 스위치 역할로 사용 가능하다.
    - 기본적으로 5V에서 동작한다.

    ![릴레이 모듈](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em002.png)

- 스텝 모터
    - 한 바퀴 회전을 많은 스텝들로 나눌 수 있는 브러쉬리스 직류 전기 모터이다.
    - 스텝 상태의 펄스에 순서를 부여하고 주어진 펄스 수에 비례한 각도만큼 회전하는 모터이다.
    - 특징으로는 미세한 각도 조절이 가능한 모터이다.

- Flask
    - 파이썬 언어로 개발한 웹개발 프레임워크 중 하나이다.
    - 용량도 작고 사용법도 간단해 라즈베리파이에서 손쉽게 웹을 통해 GPIO를 제어할 수 있음

    - GET 방식 파라미터 전달 : ?key=value&key=value 값으로 전달
    ![GET 방식](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em003.png)

## 4일차
- FND(7-segment)
    - 세그먼트 방식의 숫자 표시 소자로 일반적으로 7개의 세그먼트로 숫자를 표시하는 방식이다.
    - 각 자리마다 알파벳이 생기고 해당하는 자리에 점등하여 글자를 표시한다. 

    ![세그먼트 표현방식](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em004.png)

    ![fnd 핀](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em005.png)

## 5일차
- FND 응용
    - FND 4digit 모두 점등하기
        - FND는 불을 계속 켜놓는 것이 아닌 번갈아서 소등 및 점등을 반복하는 것이다.
        - 짧은 시간안에 반복하여 계속 켜저 있는 것처럼 보이게 만듬

    - 스위치로 1씩 숫자 증가
        - 스위치를 누를때 숫자 1씩 증가시 time.sleep()를 사용해야하는데 그때 점등이 잠깐 멈춤
        - 다른 방법을 찾아봐야함

## 6일차
- PyQt5 
    - GUI를 간단하게 개발하게 해주는 어플리케이션 프레임워크 툴
    - GUI와 센서를 연결하여 동작한다.

## 7일차
- 개인 프로젝트(PyQt5 이용)
    - iotProject01 & design01.ui
        - LED on/off 기능
        - red/blue/green/all off 버튼이 있음

    - iotProject02 & design02.ui
        - 온습도 센서 포함
        - Adafruit 모듈 설치가 안되서 실패

    - iotProject03 & design03.ui
        - 출입문 시스템
        - 종모양 버튼으로 부저를 울리고 open/close 버튼으로 서보모터를 동작 시킴