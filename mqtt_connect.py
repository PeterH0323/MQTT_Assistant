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

import JT_EMQ_Test_Assistant_Simple as mainWindow

# EMQ配置
HOST = '139.159.163.25'
PORT = 8083
client_id = 'mqtt_assistant_test_'
topic = 'EIE/out/00000000/0000000C'
username = 'eie-device'
password = 'Eie_28918499'

infolog = mqtt_Log.Log("collect.log", level='info').logger
errorlog = mqtt_Log.Log("error.log", level='error').logger


class MqttClient:
    client = mqtt.Client(client_id=client_id, transport='websockets')

    def __init__(self):
        self.thread = mainWindow.MqttRunThread()
        main_window = mainWindow.MainWindow()
        self.thread.messageTrigger.connect(main_window.add_messages)
        # pass

    def on_connect(self, client, userdata, flags, rc):
        infolog.info("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        # infolog.info('receive new message from ' + msg.topic + " + " + str(msg.payload))

        print('receive new message from ' + msg.topic + " + " + str(msg.payload))

        # self.thread.messageTrigger.emit(str(msg.payload))

        # main_window = MainWindow()
        # # main_window.EMQ_Data_textEdit.append('receive new message from ' + msg.topic + " + " + str(msg.payload))
        #
        # main_window.Signal_OneParameter.connect(main_window.on_EMQ_Data_emit_slot)
        # main_window.EMQ_Data_textEdit.append('receive new message')

        # source_msg = json.loads(msg.payload.decode())
        # print(target_msg)

    def start(self):
        # client = mqtt.Client(client_id=client_id, transport='websockets')
        self.client.username_pw_set(username=username,
                                    password=password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(HOST, PORT, 60)
        self.client.subscribe(topic)
        self.client.loop_forever()

    def connect_mqtt(self, mqtt_client_id, mqtt_username, mqtt_password, mqtt_subscribe, mqtt_host, mqtt_port,mqtt_keepalive):
        self.client = mqtt.Client(client_id=mqtt_client_id, transport='websockets')
        self.client.username_pw_set(username=mqtt_username, password=mqtt_password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(mqtt_host, mqtt_port, mqtt_keepalive)
        self.client.subscribe(mqtt_subscribe)
        self.client.loop_forever()



if __name__ == '__main__':
    test = MqttClient()
    test.start()
