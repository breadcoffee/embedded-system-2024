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
    ```