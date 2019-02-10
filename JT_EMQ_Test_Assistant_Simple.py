# -*- coding: utf-8 -*-

"""

This program is for JT EMQ test

author: Peter H
last edited: January 2019

"""

import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant

import mqtt_connect


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EIE MQTT Assistant")

        self.Command_Activate_Button.setEnabled(False)

        self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

        self.Connect_EMQ_Button.clicked.connect(self.connect_emq_button_clicked)
        self.Command_Activate_Button.clicked.connect(self.command_activate_button_clicked)

        self.mqttRunThread = MqttRunThread()
        self.mqttRunThread.messageTrigger.connect(self.add_messages)

        # self.mqttRunThread.started.connect(self.mqttRunThread.thread_started)

    @pyqtSlot()
    def connect_emq_button_clicked(self):

        if self.Connect_EMQ_Button.text() == 'Connect to EMQ':

            self.Connect_EMQ_Button.setText("Disconnect from EMQ")

            self.Emq_connect_lable.setText("MQTT connect successful !!")
            self.EMQ_Data_textEdit.append("Ready to receive data:")
            self.EMQ_Data_plainTextEdit.appendPlainText('HI')

            mqtt_connect.MqttSetting.client_id = self.ClientID_lineEdit.text()
            mqtt_connect.MqttSetting.host = self.Host_lineEdit.text()
            mqtt_connect.MqttSetting.port = int(self.Port_lineEdit.text())
            mqtt_connect.MqttSetting.client_id = self.ClientID_lineEdit.text()
            mqtt_connect.MqttSetting.username = self.Username_lineEdit.text()
            mqtt_connect.MqttSetting.password = self.Password_lineEdit.text()
            mqtt_connect.MqttSetting.keep_alive = int(self.KeepAlive_lineEdit.text())
            mqtt_connect.MqttSetting.publish_topic = self.PublishTopic_lineEdit.text()
            mqtt_connect.MqttSetting.subscribe_topic = self.SubTopic_lineEdit.text()

            # print("result = ", mqtt_connect.MqttSetting.host, mqtt_connect.MqttSetting.port,
            #       mqtt_connect.MqttSetting.client_id, mqtt_connect.MqttSetting.username, mqtt_connect.MqttSetting.password,
            #       mqtt_connect.MqttSetting.keep_alive, mqtt_connect.MqttSetting.publish_topic,
            #       mqtt_connect.MqttSetting.subscribe_topic)

            self.EMQ_Setting_groupBox.setEnabled(False)
            self.Command_Activate_Button.setEnabled(True)

            # mqtt_client = mqtt_connect.MqttClient()
            mqtt_connect.MqttClient.mqtt_connect(mqtt_client)

            # self.mqttRunThread.start()

        elif self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':
            self.Connect_EMQ_Button.setText("Connect to EMQ")
            self.Emq_connect_lable.setText("MQTT disconnected...")
            self.EMQ_Setting_groupBox.setEnabled(True)
            self.Command_Activate_Button.setEnabled(False)

            mqtt_connect.generate_client_id()
            self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

            # mqtt_client = mqtt_connect.MqttClient()
            mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
            mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)

            # self.mqttRunThread.running = False

    @pyqtSlot()
    def command_activate_button_clicked(self):
        print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)

        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, "Test PUBLISH")

    @pyqtSlot()
    def receive_messages(self, client, userdata, msg):

        print('receive new message from ' + msg.topic + " -> " + str(msg.payload))
        self.mqttRunThread.messageTrigger.emit(msg.topic + " -> " + str(msg.payload))

    def add_messages(self, receive_message):

        # mqtt_client = mqtt_connect.MqttClient()
        # mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client, force=True)

        self.EMQ_Data_textEdit.append("i fucking did it + 2")
        self.EMQ_Data_textEdit.append(receive_message + "2")
        self.EMQ_Data_plainTextEdit.appendPlainText(receive_message + "2")

        # mqtt_connect.MqttClient.mqtt_loop_start(mqtt_client)

        print("add_messages: ->" + receive_message)


class MqttRunThread(QThread):
    messageTrigger = pyqtSignal(str)

    def __init__(self):
        super(MqttRunThread, self).__init__()
        self.running = True

    def __del__(self):
        self.running = False
        self.wait()

    def run(self):
        self.messageTrigger.emit("hi,im here")

        # while self.running:
        #     self.messageTrigger.emit("hi,im here")
        #     self.sleep(1)

    # @pyqtSlot()
    def thread_started(self):
        print("MqttRunThread started")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mqtt_connect.generate_client_id()

    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    mqtt_client = mqtt_connect.MqttClient()

    sys.exit(app.exec_())
