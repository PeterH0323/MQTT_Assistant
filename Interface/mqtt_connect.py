try:
    import paho.mqtt.client as mqtt
except :
    print("catch paho")
    import os
    os.system('python -m pip install -i http://pypi.douban.com/simple/ paho-mqtt')
    import paho.mqtt.client as mqtt 

import Interface.mqtt_Log as mqtt_Log
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

import datetime

TimeFormat = '%H:%M:%S:%f'

storedToLog = mqtt_Log.Log("./Log/collect.log", level='info').logger


# errorlog = mqtt_Log.Log("error.log", level='error').logger


class MqttSetting:
    hosthosthost = '139.159.163.25'
    port = 8083
    client_id = 'mqtt_assistant_'
    username = 'eie-device'
    password = 'Eie_28918499'
    keep_alive = 60
    publish_topic = 'EIE/in/00000000/0000000C'
    subscribe_topic = 'EIE/out/00000000/0000000C'

    save_log_flag = False


def generate_client_id():
    MqttSetting.client_id = 'mqtt_assistant_'

    for i in range(0, 5):
        MqttSetting.client_id += random.choice(string.digits + string.ascii_letters)

    print("client_id = ", MqttSetting.client_id)


class MqttClient:
    message_temp = ""

    def __init__(self):
        # generate_client_id()
        # print("client_id = ", MqttSetting.client_id)
        self.client = mqtt.Client(client_id=MqttSetting.client_id, transport='websockets')
        self.client.on_connect = self.on_connect

        self.client.on_message = self.on_message
        # self.client.on_message = mainWindow.MainWindow().receive_messages

        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        if MqttSetting.save_log_flag:
            storedToLog.info("Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        if MqttSetting.save_log_flag:
            storedToLog.info("Disconnected with result code " + str(rc))

    def on_publish(self, topic, payload):
        self.client.publish(topic, payload)
        send_time = datetime.datetime.now().strftime(TimeFormat)
        MqttClient.message_temp = "【" + str(send_time) + "】" + "Send -> " + payload

        if MqttSetting.save_log_flag:
            storedToLog.info("Send->" + topic + " -> " + str(payload))

    def on_message(self, client, userdata, msg):
        receive_time = datetime.datetime.now().strftime(TimeFormat)

        MqttClient.message_temp = "【" + str(receive_time) + "】" + "Rec -> " + msg.payload.decode(encoding='utf-8')
        # print('receive new message from ' + msg.topic + " -> " + str(msg.payload))

        if MqttSetting.save_log_flag:
            storedToLog.info("Rec->" + msg.topic + " -> " + msg.payload.decode(encoding='utf-8'))

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
