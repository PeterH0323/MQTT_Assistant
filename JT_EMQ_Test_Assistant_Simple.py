# -*- coding: utf-8 -*-

"""

This program is for JT EMQ test

author: Peter H
last edited: January 2019

"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QDialog, QWidget, QMessageBox

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant

import mqtt_connect
import time


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):
    messageAddSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EIE MQTT Assistant")

        self.Command_Activate_Button.setEnabled(False)

        self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

        self.Connect_EMQ_Button.clicked.connect(self.connect_emq_button_clicked)
        self.Command_Activate_Button.clicked.connect(self.command_activate_button_clicked)
        self.Rec_Data_Clean_Button.clicked.connect(self.rec_data_clean_button_clicked)

        self.mqttRunThread = MqttRunThread()
        self.mqttRunThread.messageTrigger.connect(self.add_messages)

        self.messageAddSignal.connect(self.add_messages)

        self.mqttRunThread.started.connect(self.mqttRunThread.thread_started)
        self.mqttRunThread.finished.connect(self.mqttRunThread.thread_finished)

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

            mqtt_connect.MqttClient.mqtt_connect(mqtt_client)

            self.mqttRunThread.start()

        elif self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':
            self.Connect_EMQ_Button.setText("Connect to EMQ")
            self.Emq_connect_lable.setText("MQTT disconnected...")
            self.EMQ_Setting_groupBox.setEnabled(True)
            self.Command_Activate_Button.setEnabled(False)

            mqtt_connect.generate_client_id()
            self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

            mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
            mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)

            # self.mqttRunThread.wait()

            self.mqttRunThread.running = False

    @pyqtSlot()
    def command_activate_button_clicked(self):

        # print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, "Test PUBLISH")

    @pyqtSlot()
    def rec_data_clean_button_clicked(self):
        self.EMQ_Data_textEdit.clear()

    # call_back function
    def receive_messages(self, client, userdata, msg):

        mqtt_connect.MqttClient.message_temp = str(msg.payload)

        print('mqtt_connect.MqttClient.message_temp = ' + mqtt_connect.MqttClient.message_temp)
        self.mqttRunThread.send_flag = 1
        print("self.mqttRunThread.send_flag = " + str(self.mqttRunThread.send_flag))

        print('receive new message from ' + msg.topic + " -> " + str(msg.payload))
        # self.mqttRunThread.messageTrigger.emit(msg.topic + " -> " + str(msg.payload))
        # self.messageAddSignal.emit(msg.topic + " -> " + str(msg.payload))

        # self.mqttRunThread.start()

    def add_messages(self, receive_message):

        # self.EMQ_Data_textEdit.append("receive_message!!!!!!")

        self.EMQ_Data_textEdit.append("Receive: -> " + receive_message)
        self.EMQ_Data_plainTextEdit.appendPlainText("Receive: -> " + receive_message)
        # self.mqttRunThread.send_flag = 0

        print("add_messages: ->" + receive_message)

        mqtt_connect.MqttClient.message_temp = ""

    def closeEvent(self, event):

        mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
        mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)

        # res = QMessageBox.question(self, '消息', '确认退出？', QMessageBox.Yes | QMessageBox.No,
        #                            QMessageBox.No)  # 两个按钮是否， 默认No则关闭这个提示框
        # if res == QMessageBox.Yes:
        #     mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
        #     mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)
        #     event.accept()
        # else:
        #     event.ignore()


class MqttRunThread(QThread):
    messageTrigger = pyqtSignal(str)

    def __init__(self):
        super(MqttRunThread, self).__init__()
        self.running = True
        self.send_flag = 0

    def __del__(self):
        self.running = False
        self.wait()

    def run(self):
        self.running = True

        self.messageTrigger.emit("hi,im MqttRunThread.run!!")

        while self.running:
            # print("self.send_flag = " + str(self.send_flag))
            # if self.send_flag == 1:
            if mqtt_connect.MqttClient.message_temp != "":
                self.messageTrigger.emit(mqtt_connect.MqttClient.message_temp)
                time.sleep(0.01)
                # print("run -> mqtt_connect.MqttClient.message_temp = " + mqtt_connect.MqttClient.message_temp)
            # self.messageTrigger.emit("hi,im MqttRunThread.run")
            # self.sleep(1)

    def thread_started(self):
        print("MqttRunThread started")

    def thread_finished(self):
        print("MqttRunThread finished")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mqtt_connect.generate_client_id()

    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    mqtt_client = mqtt_connect.MqttClient()

    sys.exit(app.exec_())
