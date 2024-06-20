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
            - secs : 0.001초 단위 1000 = 1초

    ![라즈베리파이 핀맵](https://raw.githubusercontent.com/breadcoffee/embedded-system-2024/main/images/em001.png)
    