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

import Interface.mqtt_connect as mqtt_connect
import pickle
import csv
import sys

TimeFormat = '%H:%M:%S:%f'


def save_load_info(data_class, opt):
    if opt == "Save":
        save_dict = {key: value for key, value in data_class.__dict__.items() if
                     not key.startswith('__') and not callable(key)}
        # print(save_dict)

        save_file = open("./Data/mqtt_setting_info.txt", "wb")

        pickle.dump(save_dict, save_file)
        save_file.close()
        print("saved")

    elif opt == "Load":

        load_file = open("./Data/mqtt_setting_info.txt", "rb")
        loaded_setting_data = pickle.load(load_file)
        load_file.close()

        # print(loaded_setting_data)

        return loaded_setting_data


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EIE MQTT Assistant")

        self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)
        self.Host_lineEdit.setInputMask("000.000.000.000")

        self.load_inster_command_data()

        '''
            QTableView QSS 
        '''
        self.Command_list_tableWidget.setColumnWidth(0, 65)  # Set table width
        self.Command_list_tableWidget.setColumnWidth(1, 80)
        self.Command_list_tableWidget.setColumnWidth(2, 150)

        # Table cover the blank
        self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Enable manually adjust column width
        self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)

        '''
             PyQt Slot connect
        '''
        self.Connect_EMQ_Button.clicked.connect(self.connect_emq_button_clicked)
        self.Command_Activate_Button.stateChanged.connect(self.command_activate_button_state_changed)
        self.Rec_Data_Clean_Button.clicked.connect(self.rec_data_clean_button_clicked)
        self.Command_Send_Button.clicked.connect(self.command_send_button_clicked)
        self.Save_Log_checkBox.stateChanged.connect(self.save_log_checkbox_state_changed)
        self.Command_Add_Button.clicked.connect(self.command_add_button_clicked)
        self.Command_Single_Send_Button.clicked.connect(self.command_single_send_button_clicked)
        self.Command_Del_Button.clicked.connect(self.command_del_button_clicked)
        self.Command_Save_Button.clicked.connect(self.command_save_button_clicked)

        # self.Rec_Data_Clean_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.mqttDataHandlerThread = MqttDataHandlerThread()
        self.mqttDataHandlerThread.messageTrigger.connect(self.add_messages)
        self.mqttDataHandlerThread.started.connect(self.mqttDataHandlerThread.thread_started)
        self.mqttDataHandlerThread.finished.connect(self.mqttDataHandlerThread.thread_finished)

        '''
             Mqtt setting load
        '''
        get_setting_data = save_load_info(None, "Load")
        # print(get_setting_data)
        self.Host_lineEdit.setText(get_setting_data.get('host'))
        self.Port_lineEdit.setText(str(get_setting_data.get('port')))
        # self.ClientID_lineEdit.setText(get_setting_data.get('client_id'))
        self.Username_lineEdit.setText(get_setting_data.get('username'))
        self.Password_lineEdit.setText(get_setting_data.get('password'))
        self.KeepAlive_lineEdit.setText(str(get_setting_data.get('keep_alive')))
        self.PublishTopic_lineEdit.setText(get_setting_data.get('publish_topic'))
        self.SubTopic_lineEdit.setText(get_setting_data.get('subscribe_topic'))
        # self.Host_lineEdit.setText(get_setting_data.get('save_log_flag'))

    @pyqtSlot()
    def connect_emq_button_clicked(self):

        if self.Connect_EMQ_Button.text() == 'Connect to EMQ':

            self.Connect_EMQ_Button.setText("Disconnect from EMQ")

            button_new_style = '''
                    QPushButton{
                        background-color:#E74C3C;
                        color:#FFFFFF;
                        border-radius: 5px;
                    }       
                    QPushButton:hover{
                        color:#FFF5E7;
                        background:#EC7064;
                    }
                    
                '''
            self.Connect_EMQ_Button.setStyleSheet(button_new_style)

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

            mqtt_connect.MqttSetting.save_log_flag = bool(self.Save_Log_checkBox.checkState())
            # print("save_log_flag = " + str(mqtt_connect.MqttSetting.save_log_flag))
            # print("result = ", mqtt_connect.MqttSetting.host, mqtt_connect.MqttSetting.port,
            #       mqtt_connect.MqttSetting.client_id, mqtt_connect.MqttSetting.username, mqtt_connect.MqttSetting.password,
            #       mqtt_connect.MqttSetting.keep_alive, mqtt_connect.MqttSetting.publish_topic,
            #       mqtt_connect.MqttSetting.subscribe_topic)

            self.EMQ_Setting_groupBox.setEnabled(False)
            self.Command_Send_Button.setEnabled(True)

            row = self.Command_list_tableWidget.rowCount()
            if row > 0:
                self.Command_Activate_Button.setEnabled(True)

            save_load_info(mqtt_connect.MqttSetting, "Save")

            mqtt_connect.MqttClient.mqtt_connect(mqtt_client)

            self.mqttDataHandlerThread.start()

        elif self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':

            button_new_style = '''
                    QPushButton{
                        background-color:#1ABC9C;
                        color:#FFFFFF;
                        border-radius: 5px;
                    }    
                    QPushButton:hover{
                        color:#FFFFFF;
                        background:#2EE1C1;
                    }                       
                '''
            self.Connect_EMQ_Button.setStyleSheet(button_new_style)

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
    def command_activate_button_state_changed(self):

        # mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, "Test PUBLISH")

        item = self.Command_list_tableWidget.item(0, 0)
        print(item.checkState())

        if self.Command_Activate_Button.isChecked():
            print("Command_Activate_Button.isChecked")
        else:
            print("Command_Activate_Button.is unChecked")

    @pyqtSlot()
    def command_send_button_clicked(self):
        data_send = self.Command_Data_lineEdit.text()
        # print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

    @pyqtSlot()
    def rec_data_clean_button_clicked(self):
        self.EMQ_Data_textEdit.clear()

    @pyqtSlot()
    def command_single_send_button_clicked(self):

        # get selected row
        selected_row = self.Command_list_tableWidget.currentRow()
        data_send = self.Command_list_tableWidget.item(selected_row, 3).text()
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

    @pyqtSlot()
    def save_log_checkbox_state_changed(self):

        if self.Save_Log_checkBox.isChecked():
            mqtt_connect.MqttSetting.save_log_flag = True
            print("mqtt_connect.MqttSetting.save_log_flag = True")
        else:
            mqtt_connect.MqttSetting.save_log_flag = False
            print("mqtt_connect.MqttSetting.save_log_flag = False")

    @pyqtSlot()
    def command_del_button_clicked(self):


        pass

    @pyqtSlot()
    def command_add_button_clicked(self):

        self.Command_Activate_Button.setEnabled(True)

        row = self.Command_list_tableWidget.rowCount()
        self.Command_list_tableWidget.setRowCount(row + 1)
        table_row = row

        # Insert a checkbox
        checkBox = QTableWidgetItem("False")

        # Set checkBox state to unchecked
        checkBox.setCheckState(Qt.Unchecked)

        self.Command_list_tableWidget.setItem(table_row, 0, checkBox)
        self.Command_list_tableWidget.setItem(table_row, 1, QTableWidgetItem("1000"))

    @pyqtSlot()
    def command_save_button_clicked(self):

        headers = []
        column_count = self.Command_list_tableWidget.columnCount()
        for i in range(0, column_count):
            headers.append(self.Command_list_tableWidget.horizontalHeaderItem(i).text())
        print(headers)

        with open('./Data/Command_List.csv', 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)

            for row in range(self.Command_list_tableWidget.rowCount()):
                row_data = []
                for column in range(self.Command_list_tableWidget.columnCount()):
                    try:
                        item = self.Command_list_tableWidget.item(row, column).text()

                    except AttributeError:   # a blank item !!
                        # print("AttributeError")
                        item = ""

                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        # raise

                    row_data.append(item)
                f_csv.writerow(row_data)
        print("Saved CSV")




    def load_inster_command_data(self):
        # path = QtGui.QFileDialog.getOpenFileName(
        #     self, 'Open File', '', 'CSV(*.csv)')
        # if not path.isEmpty():

        # with open('./Data/Command_List.csv') as f:
        #     f_tsv = csv.reader(f, delimiter='\t')
        #     for row in f_tsv:
        #         print(row)

        with open('./Data/Command_List.csv', 'r') as f:

            f_tsv = csv.reader(f, delimiter='\t')



            # '''
            #     QTableView QSS
            # '''
            # self.Command_list_tableWidget.setColumnWidth(0, 65)  # Set table width
            # self.Command_list_tableWidget.setColumnWidth(1, 80)
            # self.Command_list_tableWidget.setColumnWidth(2, 150)
            #
            # # Table cover the blank
            # self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            #
            # # Enable manually adjust column width
            # self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            # self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
            # self.Command_list_tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)

            self.Command_list_tableWidget.setRowCount(0)
            self.Command_list_tableWidget.setColumnCount(0)

            for f_tsv in csv.reader(f):
                row = self.Command_list_tableWidget.rowCount()
                self.Command_list_tableWidget.insertRow(row)
                self.Command_list_tableWidget.setColumnCount(len(f_tsv))

                if row == 0:  # header

                    for column, data in enumerate(f_tsv):
                        item = QTableWidgetItem(str(data))
                        self.Command_list_tableWidget.setHorizontalHeaderItem(column, item)
                        print("row =", row, "column=", column, " item = ", item)

                else:
                    row = row - 1
                    for column, data in enumerate(f_tsv):

                        if column == 0:
                            # Insert a checkbox
                            checkBox = QTableWidgetItem(str(data))

                            # Set checkBox state to unchecked
                            checkBox.setCheckState(Qt.Unchecked)

                            self.Command_list_tableWidget.setItem(row, column, checkBox)

                        else:
                            item = QTableWidgetItem(str(data))
                            self.Command_list_tableWidget.setItem(row, column, item)
                            print("row =", row, "column=", column, " item = ", item)

            # delete the last row
            last_row = self.Command_list_tableWidget.rowCount()-1
            self.Command_list_tableWidget.removeRow(last_row)









    # # call_back function
    # def receive_messages(self, client, userdata, msg):
    #     receive_time = datetime.datetime.now().strftime(TimeFormat)
    #     mqtt_connect.MqttClient.message_temp = "【" + str(receive_time) + "】" + " Rec -> " + str(msg.payload)
    #     print('receive new message from ' + msg.topic + " -> " + str(msg.payload))
    #     mqtt_connect.storedToLog.info("Rec->" + msg.topic + " -> " + str(msg.payload))
    #     self.mqttDataHandlerThread.messageTrigger.emit(msg.topic + " -> " + str(msg.payload))

    def add_messages(self, message):

        self.EMQ_Data_textEdit.append(message)
        print("add_messages: ->" + message)
        # mqtt_connect.MqttClient.message_temp = ""



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
                mqtt_connect.MqttClient.message_temp = ""

                # time.sleep(0.05)

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
