import paho.mqtt.client as mqtt

def on_message(clinet, userdata, message):
    print('message received'.str(message.payload.deconde('utf-8')))
    print('message topic='.message.topic)
    print('message qod='.message.qos)
    print('message retain flag='.message.retain)
    print('message retain flag'.message.retain)

broker_adress = '192.168.100.100'
client1 = mqtt.Client('client')
client1.connect(broker_adress)