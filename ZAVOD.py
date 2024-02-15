import random
import time
import csv
from paho.mqtt import client as mqtt_client

broker = '192.168.0.221'
port = 1883
topic1 = "python/DC_AS"
topic2 = "python/DC_GES"
topic3 = "python/DC_GOROD"
topic4 = "python/DC_ZAVOD"

client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'admin'
password = 'admin'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %dn", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, 'python3')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,data_DC):
    while True:
        for i in range(len(data_DC)):
            result = client.publish(topic1, data_DC[i][0]) 
            result = client.publish(topic2, data_DC[i][1])
            result = client.publish(topic3, data_DC[i][2])
            result = client.publish(topic4, data_DC[i][3])
            time.sleep(1)


def main():
    client = connect_mqtt()
    client.loop_start()
    
    fake_data_DC = []
    with open('DC_bez_ZAVODA.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data_DC.append(b)
    publish(client,fake_data_DC)


if __name__ == '__main__':
    main()