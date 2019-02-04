# -*- coding: utf-8 -*-

"""

This program is for JT EMQ test

author: Peter H
last edited: January 2019

"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

import mqtt_connect

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    @pyqtSlot()
    def on_Connect_EMQ_Button_released(self):
        self.Emq_connect_lable.setText("MQTT connect successful")
        self.EMQ_Data_textEdit.append("Ready to receive data:")

        mqtt_host = self.Host_lineEdit.text()
        mqtt_port = self.Port_lineEdit.text()
        mqtt_clientID = self.ClientID_lineEdit.text()
        mqtt_username = self.Username_lineEdit.text()
        mqtt_password = self.Password_lineEdit.text()
        mqtt_keepAlive = self.KeepAlive_lineEdit.text()
        mqtt_publishTopic = self.PublishTopic_lineEdit.text()
        mqtt_subTopic = self.SubTopic_lineEdit.text()

        print("result = ", mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
              mqtt_publishTopic, mqtt_subTopic)

        # mqtt_connect.connect_mqtt(mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
        #                           mqtt_publishTopic, mqtt_subTopic)

    @pyqtSlot()
    def on_EMQ_Data_emit_slot(self):
        # self.EMQ_Data_textEdit.append('receive new message' + Str)
        self.EMQ_Data_textEdit.append('receive new message')
        # pass


class MqttRun(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(MqttRun, self).__init__()

    def run(self):
        mqtt_connect.start()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    sys.exit(app.exec_())
