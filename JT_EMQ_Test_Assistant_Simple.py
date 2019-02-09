# -*- coding: utf-8 -*-

"""

This program is for JT EMQ test

author: Peter H
last edited: January 2019

"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant

import mqtt_connect


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.thread = MqttRunThread()
        self.thread.messageTrigger.connect(self.add_messages)

    @pyqtSlot()
    def on_Connect_EMQ_Button_released(self):
        self.Emq_connect_lable.setText("MQTT connect successful !! ")
        self.EMQ_Data_textEdit.append("Ready to receive data:")

        mqtt_connect.MqttSetting.client_id = self.ClientID_lineEdit.text()
        mqtt_connect.MqttSetting.host = self.Host_lineEdit.text()
        mqtt_connect.MqttSetting.port = int(self.Port_lineEdit.text())
        mqtt_connect.MqttSetting.client_id = self.ClientID_lineEdit.text()
        mqtt_connect.MqttSetting.username = self.Username_lineEdit.text()
        mqtt_connect.MqttSetting.password = self.Password_lineEdit.text()
        mqtt_connect.MqttSetting.keep_alive = int(self.KeepAlive_lineEdit.text())
        mqtt_connect.MqttSetting.publish_topic = self.PublishTopic_lineEdit.text()
        mqtt_connect.MqttSetting.subscribe_topic = self.SubTopic_lineEdit.text()

        print("result = ", mqtt_connect.MqttSetting.host, mqtt_connect.MqttSetting.port,
              mqtt_connect.MqttSetting.client_id, mqtt_connect.MqttSetting.username, mqtt_connect.MqttSetting.password,
              mqtt_connect.MqttSetting.keep_alive, mqtt_connect.MqttSetting.publish_topic,
              mqtt_connect.MqttSetting.subscribe_topic)

        self.Connect_EMQ_Button.setEnabled(False)
        self.Host_lineEdit.setEnabled(False)
        self.Host_lineEdit.setEnabled(False)
        self.Port_lineEdit.setEnabled(False)
        self.ClientID_lineEdit.setEnabled(False)
        self.Username_lineEdit.setEnabled(False)
        self.Password_lineEdit.setEnabled(False)
        self.KeepAlive_lineEdit.setEnabled(False)
        self.PublishTopic_lineEdit.setEnabled(False)
        self.SubTopic_lineEdit.setEnabled(False)

        mqtt_thread.start()

        # mqtt_connect.connect_mqtt(mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
        #                           mqtt_publishTopic, mqtt_subTopic)

    @pyqtSlot()
    def on_EMQ_Data_emit_slot(self):
        # self.EMQ_Data_textEdit.append('receive new message' + Str)
        self.EMQ_Data_textEdit.append('receive new message')
        # pass

    def add_messages(self, receive_message):
        # self.EMQ_Data_textEdit.append('receive new message' + Str)
        self.EMQ_Data_textEdit.append('receive new message' + receive_message)


class MqttRunThread(QThread):
    messageTrigger = pyqtSignal(str)

    def __init__(self):
        super(MqttRunThread, self).__init__()

    def run(self):
        # pass
        mqtt_client = mqtt_connect.MqttClient()
        mqtt_connect.MqttClient.start(mqtt_client)

        # mqtt_connect.MqttClient.connect_mqtt(mqtt_client)
        # mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, 'Test PUBLISH')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    mqtt_thread = MqttRunThread()

    sys.exit(app.exec_())
