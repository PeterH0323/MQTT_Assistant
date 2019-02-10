# -*- coding: utf-8 -*-

"""

This program is for JT EMQ test

author: Peter H
last edited: January 2019
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

import Interface.mqtt_connect

from UI.EMQ_Setting_UI import Ui_EMQ_Setting_Dialog
from UI.JT_EMQ_Test_Assistant_UI import Ui_JT_EMQ_Test_Assistant

mqtt_host = 0
mqtt_port = 0
mqtt_clientID = 0
mqtt_username = 0
mqtt_password = 0
mqtt_keepAlive = 0
mqtt_publishTopic = 0
mqtt_subTopic = 0


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    @pyqtSlot()
    def on_Connect_EMQ_Button_released(self):
        self.Emq_connect_lable.setText("MQTT connect successful")
        self.Receive_EMQ_textEdit.append("Ready to receive data:")
        print("result = ", mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
              mqtt_publishTopic,
              mqtt_subTopic)
        # mqtt_connect.connect_mqtt(mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
        #                           mqtt_publishTopic, mqtt_subTopic)
        # mqtt_connect.start()

    # @pyqtSlot()
    # def on_actionEMQ_triggered(self):
    #     setting_dialog_show = Setting()
    #     setting_dialog_show.show()


class Setting(QDialog, Ui_EMQ_Setting_Dialog):

    def __init__(self, parent=None):
        super(Setting, self).__init__(parent)

        self.setupUi(self)

    def on_Setting_EMQ_Buttons_accepted(self):
        mqtt_host = self.Host_lineEdit.text()
        mqtt_port = self.Port_lineEdit.text()
        mqtt_clientID = self.ClientID_lineEdit.text()
        mqtt_username = self.Username_lineEdit.text()
        mqtt_password = self.Password_lineEdit.text()
        mqtt_keepAlive = self.KeepAlive_lineEdit.text()
        mqtt_publishTopic = self.PublishTopic_lineEdit.text()
        mqtt_subTopic = self.SubTopic_lineEdit.text()

        # print("result = ", mqtt_host, mqtt_port, mqtt_clientID, mqtt_username, mqtt_password, mqtt_keepAlive,
        #       mqtt_publishTopic,
        #       mqtt_subTopic)

    def on_Setting_EMQ_Buttons_rejected(self):
        self.close()
        print("Close")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test_Assistant_MainWidow = MainWindow()
    test_Assistant_MainWidow.show()

    setting_dialog = Setting()

    test_Assistant_MainWidow.actionEMQ.triggered.connect(setting_dialog.show)

    sys.exit(app.exec_())
