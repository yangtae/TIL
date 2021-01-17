import paho.mqtt.client as mqtt
#1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

try:
    #2. 브로커 연결
    client.connect('localhost')

    #3.토픽 메세지 발행
    client.publish('SYS','Hello World')
    client.loop(2)
except Exception as err:
    print('에러 : %s'%err)