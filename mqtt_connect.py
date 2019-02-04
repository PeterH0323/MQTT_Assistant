import paho.mqtt.client as mqtt

import mqtt_Log

# import Interface.mqtt_Log as mqtt_Log

# import os
# import sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, base_dir)

# from UI.EMQ_Setting_UI import Ui_EMQ_Setting_Dialog
# from UI.JT_EMQ_Test_Assistant_UI import Ui_JT_EMQ_Test_Assistant

# import JT_EMQ_Test_Assistant_Simple

from JT_EMQ_Test_Assistant_Simple import MainWindow

# EMQ配置
HOST = '139.159.163.25'
PORT = 8083
client_id = 'mqttjs_0ae165f583'
topic = 'EIE-AT/out/00000000/0000000A'
username = 'eie-device'
password = 'Eie_28918499'

infolog = mqtt_Log.Log("collect.log", level='info').logger
errorlog = mqtt_Log.Log("error.log", level='error').logger


def on_connect(client, userdata, flags, rc):
    infolog.info("Connected with result code " + str(rc))

    client.subscribe(topic)


def on_message(client, userdata, msg):
    # infolog.info('receive new message from ' + msg.topic + " + " + str(msg.payload))

    test_assistant_main_window = MainWindow()
    # test_assistant_main_window.EMQ_Data_textEdit.append('receive new message from ' + msg.topic + " + " + str(msg.payload))
    test_assistant_main_window.Signal_OneParameter.connect(test_assistant_main_window.on_EMQ_Data_emit_slot)
    # test_assistant_main_window.EMQ_Data_textEdit.append('receive new message')

    # source_msg = json.loads(msg.payload.decode())
    # print(target_msg)


def client_loop():
    client = mqtt.Client(client_id=client_id, transport='websockets')
    client.username_pw_set(username=username,
                           password=password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def start():
    client_loop()


def connect_mqtt(mqtt_client_id, mqtt_username, mqtt_password, mqtt_subscribe, mqtt_host, mqtt_port, mqtt_keepAlive):
    client = mqtt.Client(client_id=mqtt_client_id, transport='websockets')
    client.username_pw_set(username=mqtt_username,
                           password=mqtt_password)

    client.on_connect = client.subscribe(mqtt_subscribe)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_host, mqtt_port, mqtt_keepAlive)


if __name__ == '__main__':
    client_loop()
