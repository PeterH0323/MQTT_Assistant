# -*- coding: utf-8 -*-

"""

# This program is for JT EMQ test
# author: Peter H.
# First Version : 2019.01
# Last Edited: 2019.2

"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QDialog, QWidget, QMessageBox

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant

import mqtt_connect
import time
import datetime

TimeFormat = '%H:%M:%S:%f'


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EIE MQTT Assistant")

        self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

        self.Connect_EMQ_Button.clicked.connect(self.connect_emq_button_clicked)
        self.Command_Activate_Button.clicked.connect(self.command_activate_button_clicked)
        self.Rec_Data_Clean_Button.clicked.connect(self.rec_data_clean_button_clicked)
        self.Command_Send_Button.clicked.connect(self.command_send_button_clicked)

        self.mqttDataHandlerThread = MqttDataHandlerThread()
        self.mqttDataHandlerThread.messageTrigger.connect(self.add_messages)
        self.mqttDataHandlerThread.started.connect(self.mqttDataHandlerThread.thread_started)
        self.mqttDataHandlerThread.finished.connect(self.mqttDataHandlerThread.thread_finished)

    @pyqtSlot()
    def connect_emq_button_clicked(self):

        if self.Connect_EMQ_Button.text() == 'Connect to EMQ':

            self.Connect_EMQ_Button.setText("Disconnect from EMQ")

            self.Emq_connect_lable.setText("MQTT connect successful !!")
            # self.EMQ_Data_textEdit.append("Ready to receive data:")

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
            self.Command_Send_Button.setEnabled(True)

            mqtt_connect.MqttClient.mqtt_connect(mqtt_client)

            self.mqttDataHandlerThread.start()

        elif self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':
            self.Connect_EMQ_Button.setText("Connect to EMQ")
            self.Emq_connect_lable.setText("MQTT disconnected...")
            self.EMQ_Setting_groupBox.setEnabled(True)
            self.Command_Activate_Button.setEnabled(False)
            self.Command_Send_Button.setEnabled(False)


            mqtt_connect.generate_client_id()
            self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

            mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
            mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)

            # self.mqttDataHandlerThread.wait()

            self.mqttDataHandlerThread.running = False

    @pyqtSlot()
    def command_activate_button_clicked(self):

        # print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, "Test PUBLISH")

    @pyqtSlot()
    def command_send_button_clicked(self):
        data_send = self.Command_Data_lineEdit.text()
        # print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

    @pyqtSlot()
    def rec_data_clean_button_clicked(self):
        self.EMQ_Data_textEdit.clear()

    # call_back function
    def receive_messages(self, client, userdata, msg):
        receive_time = datetime.datetime.now().strftime(TimeFormat)
        mqtt_connect.MqttClient.message_temp = "【" + str(receive_time) + "】" + " Receive: -> " + str(msg.payload)
        print('receive new message from ' + msg.topic + " -> " + str(msg.payload))
        # self.mqttDataHandlerThread.messageTrigger.emit(msg.topic + " -> " + str(msg.payload))

    def add_messages(self, message):

        self.EMQ_Data_textEdit.append(message)
        print("add_messages: ->" + message)
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


class MqttDataHandlerThread(QThread):
    messageTrigger = pyqtSignal(str)

    def __init__(self):
        super(MqttDataHandlerThread, self).__init__()
        self.running = True

    def __del__(self):
        self.running = False
        self.wait()

    def run(self):
        self.running = True
        # self.messageTrigger.emit("hi,im mqttDataHandlerThread.run!!")
        while self.running:
            # self.messageTrigger.emit("hi,im mqttDataHandlerThread.run")
            # self.sleep(1)
            if mqtt_connect.MqttClient.message_temp != "":
                self.messageTrigger.emit(mqtt_connect.MqttClient.message_temp)
                time.sleep(0.05)

    def thread_started(self):
        print("mqttDataHandlerThread started")

    def thread_finished(self):
        print("mqttDataHandlerThread finished")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mqtt_connect.generate_client_id()

    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    mqtt_client = mqtt_connect.MqttClient()

    sys.exit(app.exec_())
