import paho.mqtt.client as mqtt

import mqtt_Log
import string
import random
# import Interface.mqtt_Log as mqtt_Log

# import os
# import sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, base_dir)

# from UI.EMQ_Setting_UI import Ui_EMQ_Setting_Dialog
# from UI.JT_EMQ_Test_Assistant_UI import Ui_JT_EMQ_Test_Assistant

# import JT_EMQ_Test_Assistant_Simple

import JT_EMQ_Test_Assistant_Simple as mainWindow

infolog = mqtt_Log.Log("collect.log", level='info').logger
errorlog = mqtt_Log.Log("error.log", level='error').logger


class MqttSetting:
    host = '139.159.163.25'
    port = 8083
    client_id = 'mqtt_assistant_'
    username = 'eie-device'
    password = 'Eie_28918499'
    keep_alive = 60
    publish_topic = 'EIE/out/00000000/0000000C'
    subscribe_topic = 'EIE/in/00000000/0000000C'


def generate_client_id():

    MqttSetting.client_id = 'mqtt_assistant_'

    for i in range(0, 4):
        MqttSetting.client_id += random.choice(string.digits + string.ascii_letters)

    print("client_id = ", MqttSetting.client_id)


class MqttClient:

    message_temp = ""

    def __init__(self):
        # generate_client_id()
        # print("client_id = ", MqttSetting.client_id)
        self.client = mqtt.Client(client_id=MqttSetting.client_id, transport='websockets')
        self.client.on_connect = self.on_connect

        # self.client.on_message = self.on_message
        self.client.on_message = mainWindow.MainWindow().receive_messages

        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        infolog.info("Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        infolog.info("Disconnected with result code " + str(rc))

    def on_publish(self, topic, payload):
        self.client.publish(topic, payload)

    def on_message(self, client, userdata, msg):
        # infolog.info('receive new message from ' + msg.topic + " + " + str(msg.payload))
        print('receive new message from ' + msg.topic + " + " + str(msg.payload))

        # test_payload = 'Test PUBLISH'
        # self.on_publish(MqttSetting.publish_topic, 'Test PUBLISH')

        # source_msg = json.loads(msg.payload.decode())
        # print(target_msg)

    def mqtt_loop_start(self):
        self.client.loop_start()

    def mqtt_loop_stop(self, force=False):
        self.client.loop_stop(force=force)

    def mqtt_connect(self):
        # client = mqtt.Client(client_id=client_id, transport='websockets')
        self.client.username_pw_set(username=MqttSetting.username, password=MqttSetting.password)
        self.client.connect(MqttSetting.host, MqttSetting.port, MqttSetting.keep_alive)
        self.client.subscribe(MqttSetting.subscribe_topic)
        # self.client.loop_forever()
        self.mqtt_loop_start()

    def mqtt_disconnect(self):
        self.client.disconnect()


if __name__ == '__main__':
    test = MqttClient()
    test.mqtt_connect()
