# 가상의 센서 4개 운영
# 값은 센서마다 범위를 주고 랜덤하게
# 1 온도센서 5초간격으로 측정값 발행 (iot/user1/temp)
# 2 습도센서 7초간격으로 측정값 발행 (iot/user1/humi)
# 3 조도센서 10초간격으로 측정값 발행 (iot/user1/illu)
# 4 미세먼지 센서 12초 간격으로 측정값 발행 (iot/user1/dust)

from threading import Thread
import time
import random #센서의 범위를 랜덤으로 주기위해
import paho.mqtt.client as mqtt

HOST = 'localhost'
class Sensor(Thread): #각 센서마다 초가 따로 돌아야하기 때문에 스레드를 사용한다
    def __init__(self,range,interval,topic):
        self.range = range
        self.interval =interval
        self.topic = topic
        self.client = mqtt.Client()

    def run(self):
        self.client.connect(HOST)
        while True:
            time.sleep(self.interval)
            value = random.uiform(*self.rnage)
            #토픽 발행
            print(self.topic,value)
            self.client.publish(self.topic,value)
            self.client.loop(2)

if __name__ == '__main__':
    temp_sensor = Sensor(5,(3,10),'iot/user1/temp')
    temp_sensor.start()



# #모니터 운영
# 토픽 수신시
# 시간, 토픽, 값 을 sensorvalues.csv파일에 추가
# 메시지 수신시에만 file open 단일 메시지 기록 후 close

# 모니터운영 2
# 0)온도 1) 습도  2)조도 3)미세먼지 4)종료
# 해당 메뉴를 선택한 경우 현재까지의 평균값 출력