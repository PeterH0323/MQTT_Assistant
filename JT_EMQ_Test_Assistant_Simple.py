# -*- coding: utf-8 -*-

"""

# This program is for JT EMQ test
# author: Peter H.
# First Version : 2019.02.04
# Last Edited: 2019.02.13

    后续升级思路：
        1、循环发送的时候 鲜颜色底色 标出所在的指令位置
        2、QTextEdit设置语法高亮：send or Rec ， 搜索关键词 ：Qt QTextEdit 语法高亮： https://blog.csdn.net/weixin_42837024/article/details/81871636
        3、QTextEdit光标所在行高亮


"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QDialog, QWidget, QMessageBox

from UI.JT_EMQ_Test_Assistant_UI_Simple import Ui_JT_EMQ_Test_Assistant

import Interface.mqtt_connect as mqtt_connect
import Interface.EMQ_Web_Get_Data as emq_web_get_data
import pickle
import csv
import time
import datetime
import subprocess

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
        try:
            load_file = open("./Data/mqtt_setting_info.txt", "rb")

        except FileNotFoundError:  # No file exists
            # print("Unexpected error:", sys.exc_info()[0])
            return "FileNotFoundError"

        else:
            loaded_setting_data = pickle.load(load_file)
            load_file.close()
            return loaded_setting_data


class MainWindow(QMainWindow, Ui_JT_EMQ_Test_Assistant):
    command_send_index = []
    command_next_num = 0
    command_next_timing = 1000
    command_loop_times = 1
    command_loop_infinite_flag = False

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EIE MQTT Assistant")

        self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)
        self.Host_lineEdit.setInputMask("000.000.000.000")

        self.command_send_timer = QTimer(self)
        self.command_send_timer.timeout.connect(self.command_send_message)

        '''
             QTableView data load
        '''
        self.load_insert_command_data()

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

        # Already set by Qt designer
        # self.Command_list_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # Select whole row
        # self.Command_list_tableWidget.setSelectionMode(QTableWidget.SingleSelection)  # Select single row

        self.Command_list_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # Enable right click
        self.Command_list_tableWidget.customContextMenuRequested.connect(self.command_list_tableWidget_menu)

        # self.Command_list_tableWidget.setItem(3, 5, QTableWidgetItem())
        # self.Command_list_tableWidget.item(3, 5).setBackground(QColor(100, 100, 150))

        '''
             PyQt Slot connect
        '''
        self.Connect_EMQ_Button.clicked.connect(self.connect_emq_button_clicked)
        self.Command_Activate_Button.stateChanged.connect(self.command_activate_button_state_changed)
        self.Command_Send_Button.clicked.connect(self.command_send_button_clicked)
        self.Command_Add_Button.clicked.connect(self.command_add_button_clicked)
        self.Command_Single_Send_Button.clicked.connect(self.command_single_send_button_clicked)
        self.Command_Del_Button.clicked.connect(self.command_del_button_clicked)
        self.Command_Save_Button.clicked.connect(self.command_save_button_clicked)
        self.Command_list_tableWidget.itemClicked.connect(self.command_list_item_clicked)
        self.Save_Log_checkBox.stateChanged.connect(self.save_log_checkbox_state_changed)
        self.Rec_Data_Clean_Button.clicked.connect(self.rec_data_clean_button_clicked)

        self.radioButton_loop_times.toggled.connect(self.radioButton_toggled)
        self.EMQ_Data_textEdit.cursorPositionChanged.connect(self.text_edit_position_changed)
        self.textEdit_Fianl_Line_Button.clicked.connect(self.text_edit_final_line_button_clicked)
        self.textEdit_Open_Log_Button.clicked.connect(self.text_edit_open_log_button_clicked)

        self.Check_EMQ_Button.clicked.connect(self.check_emq_button_clicked)
        self.actionExtranet.triggered.connect(self.action_extranet_clicked)
        self.actionIntranet.triggered.connect(self.action_intranet_clicked)
        # self.Check_EMQ_Button.clicked.connect(emq_topic_data.show)

        # self.Rec_Data_Clean_Button.setCursor(QCursor(Qt.PointingHandCursor))

        self.mqttDataHandlerThread = MqttDataHandlerThread()
        self.mqttDataHandlerThread.messageTrigger.connect(self.add_messages)
        self.mqttDataHandlerThread.started.connect(self.mqttDataHandlerThread.thread_started)
        self.mqttDataHandlerThread.finished.connect(self.mqttDataHandlerThread.thread_finished)

        self.commandActivateThread = CommandActivateThread()
        self.commandActivateThread.commandTrigger.connect(self.command_send_message)
        self.commandActivateThread.started.connect(self.commandActivateThread.thread_started)
        self.commandActivateThread.finished.connect(self.commandActivateThread.thread_finished)

        '''
             Mqtt setting load
        '''
        get_setting_data = save_load_info(None, "Load")

        if get_setting_data != "FileNotFoundError":
            # print('get_setting_data != "FileNotFoundError"')
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

            # self.Emq_connect_lable.setText("MQTT connect successful !!")
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
            self.Command_Single_Send_Button.setEnabled(True)

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
            # self.Emq_connect_lable.setText("MQTT disconnected...")
            self.EMQ_Setting_groupBox.setEnabled(True)
            self.Command_Activate_Button.setEnabled(False)
            self.Command_Send_Button.setEnabled(False)
            self.Command_Single_Send_Button.setEnabled(False)

            mqtt_connect.generate_client_id()
            self.ClientID_lineEdit.setText(mqtt_connect.MqttSetting.client_id)

            mqtt_connect.MqttClient.mqtt_disconnect(mqtt_client)
            mqtt_connect.MqttClient.mqtt_loop_stop(mqtt_client)

            # self.mqttDataHandlerThread.wait()

            self.mqttDataHandlerThread.running = False

    @pyqtSlot()
    def command_activate_button_state_changed(self):

        # mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, "Test PUBLISH")

        # item = self.Command_list_tableWidget.item(0, 0)
        # print(item.checkState())

        if self.Command_Activate_Button.isChecked():

            row = self.Command_list_tableWidget.rowCount() - 1
            check_box_state = []
            self.command_loop_times = 0
            self.command_next_num = 0
            self.command_send_index = []

            for i in range(row):

                # item = self.Command_list_tableWidget.item(i, 0).checkState()
                # if item == "2":
                if self.Command_list_tableWidget.item(i, 0).checkState() == 2:
                    check_box_state.append(i)

                    # try:
                    #     data_send = self.Command_list_tableWidget.item(i, 1).text()
                    # except AttributeError:  # a blank item !!
                    #     print("AttributeError")
                    #     data_send = 0

                    # send_time_state.append(int(data_send))
            # command_send_time = send_time_state[:]
            # print(command_send_time)

            self.command_send_index = check_box_state
            print("command_send_index = ", self.command_send_index)

            self.Command_list_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.loop_times_spinBox.setEnabled(False)
            self.radioButton_infinite.setEnabled(False)
            self.radioButton_loop_times.setEnabled(False)

            if len(self.command_send_index) > 0:
                self.command_next_num = 0

                try:
                    data_send = self.Command_list_tableWidget.item(
                        self.command_send_index[self.command_next_num], 3).text()
                    # print("data_send = ", data_send)
                    print("self.command_send_index[self.command_next_num] ",
                          self.command_send_index[self.command_next_num])

                except AttributeError:  # a blank item !!
                    print("AttributeError")
                    # item = ""

                else:
                    mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

                new_timing = int(self.Command_list_tableWidget.item(
                    self.command_send_index[self.command_next_num], 1).text())

                self.command_send_timer.start(new_timing)
                print("command_send_timer.start = ", new_timing)

            self.Command_send_progressBar.setValue(0)
            # self.commandActivateThread.start()

            if self.radioButton_loop_times.isChecked():
                self.command_loop_infinite_flag = False
                # self.command_loop_times = self.loop_times_spinBox.value()
                # print("self.command_loop_times = ", self.command_loop_times)

            elif self.radioButton_infinite.isChecked():
                self.command_loop_infinite_flag = True

            else:
                return
        else:
            self.Command_list_tableWidget.setEditTriggers(
                QAbstractItemView.DoubleClicked | QAbstractItemView.AnyKeyPressed)
            self.commandActivateThread.running = False
            self.loop_times_spinBox.setEnabled(True)
            self.radioButton_infinite.setEnabled(True)
            self.radioButton_loop_times.setEnabled(True)


            self.command_send_timer.stop()

            print("Command_Activate_Button.is unChecked")

    @pyqtSlot()
    def command_send_button_clicked(self):
        data_send = self.Command_Data_lineEdit.text()
        # print('publish_topic = ' + mqtt_connect.MqttSetting.publish_topic)
        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

    @pyqtSlot()
    def text_edit_open_log_button_clicked(self):
        # subprocess.Popen(r'explorer /select,"J:\desktop_shortcuts\programme\PyQt5\MQTT_Assistant\Log\collect.log"')
        subprocess.Popen(r'explorer /select,".\Log\collect.log"')

    @pyqtSlot()
    def check_emq_button_clicked(self):
        emq_topic_data.show()

        network = self.Host_lineEdit.text()

        if network == "192.168.1.113":
            emq_topic_data.Get_Intranet_EMQ_data()

        elif network == "139.159.163.25":
            emq_topic_data.Get_Extranet_EMQ_data()

    @pyqtSlot()
    def action_extranet_clicked(self):
        self.Host_lineEdit.setText("139.159.163.25")

    @pyqtSlot()
    def action_intranet_clicked(self):
        self.Host_lineEdit.setText("192.168.1.113")


    @pyqtSlot()
    def command_list_item_clicked(self):
        selected_row = self.Command_list_tableWidget.currentRow()
        # print(selected_row)

        if selected_row != -1:
            # print("selected_row != -1")
            try:
                set_data = self.Command_list_tableWidget.item(selected_row, 3).text()
            except AttributeError:  # a blank item !!
                print("AttributeError")
                # item = ""

            else:
                self.Command_Data_lineEdit.setText(set_data)


    @pyqtSlot()
    def text_edit_position_changed(self):
        # print("text_edit_position_changed")
        cursor = self.EMQ_Data_textEdit.textCursor()
        row = cursor.blockNumber()
        # col = cursor.columnNumber()
        print("row = ", row)

    @pyqtSlot()
    def text_edit_final_line_button_clicked(self):
        cursor = self.EMQ_Data_textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.EMQ_Data_textEdit.setTextCursor(cursor)

    @pyqtSlot()
    def rec_data_clean_button_clicked(self):
        self.EMQ_Data_textEdit.clear()

    @pyqtSlot()
    def radioButton_toggled(self):
        # print("radioButton_loop_times_toggled")
        if self.radioButton_loop_times.isChecked():
            print("self.radioButton_loop_times.isChecked()")
        elif self.radioButton_infinite.isChecked():
            print("self.radioButton_infinite.isChecked()")

    @pyqtSlot(QPoint)
    def command_list_tableWidget_menu(self, pos):

        # print("pos = ", pos)
        # row_num = -1

        # for i in self.Command_list_tableWidget.selectionModel().selection().indexes():
        #     row_num = i.row()
        #     print(row_num)

        # if row_num < 2:
        menu = QMenu()
        item1 = menu.addAction("Send")
        item2 = menu.addAction("Delete")

        action = menu.exec_(self.Command_list_tableWidget.mapToGlobal(pos))

        if action == item1:
            # print("Send")
            self.command_single_send_button_clicked()

        elif action == item2:
            # print("Delete")
            self.command_del_button_clicked()

        else:
            return

    @pyqtSlot()
    def command_single_send_button_clicked(self):

        # get selected row
        selected_row = self.Command_list_tableWidget.currentRow()

        # self.Command_list_tableWidget.item(selected_row, 2).setBackground(QColor(180, 220, 255))

        if selected_row != -1:
            # print("selected_row != -1")
            try:
                data_send = self.Command_list_tableWidget.item(selected_row, 3).text()
            except AttributeError:  # a blank item !!
                print("AttributeError")
                # item = ""

            else:
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

        row = self.Command_list_tableWidget.currentRow()
        self.Command_list_tableWidget.removeRow(row)

    @pyqtSlot()
    def command_add_button_clicked(self):

        if self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':
            self.Command_Activate_Button.setEnabled(True)

        row = self.Command_list_tableWidget.rowCount()
        self.Command_list_tableWidget.setRowCount(row + 1)
        table_row = row

        # Insert a checkbox
        # checkBox = QTableWidgetItem("False")
        checkBox = QTableWidgetItem()

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

                        if column == 0:
                            item = self.Command_list_tableWidget.item(row, column).checkState()

                        else:
                            item = self.Command_list_tableWidget.item(row, column).text()

                    except AttributeError:  # a blank item !!
                        # print("AttributeError")
                        item = ""

                    # except:
                    #     print("Unexpected error:", sys.exc_info()[0])
                    #     # raise

                    row_data.append(item)
                f_csv.writerow(row_data)
        print("Saved CSV")

    @pyqtSlot(str)
    def add_messages(self, message):

        self.EMQ_Data_textEdit.append(message)
        print("add_messages: ->" + message)

    # @pyqtSlot(int)
    # def command_send_message(self, value):
    @pyqtSlot()
    def command_send_message(self):
        self.command_send_timer.stop()
        print("self.command_send_timer.stop()")

        self.command_next_num += 1

        if self.command_next_num < len(self.command_send_index):

            try:
                data_send = self.Command_list_tableWidget.item(
                    self.command_send_index[self.command_next_num], 3).text()
                # print("data_send = ", data_send)
                print("self.command_send_index[self.command_next_num] ", self.command_send_index[self.command_next_num])

            except AttributeError:  # a blank item !!
                print("AttributeError")
                # item = ""

            else:
                mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)

            new_timing = int(self.Command_list_tableWidget.item(
                self.command_send_index[self.command_next_num], 1).text())

            self.command_send_timer.start(new_timing)
            print("command_send_timer.start = ", new_timing)

            progressBar_value = self.command_next_num / len(self.command_send_index) * 100
            # print("progressBar_value = ", progressBar_value)
            self.Command_send_progressBar.setValue(progressBar_value)


        else:
            self.Command_send_progressBar.setValue(0)
            self.command_next_num = 0
            self.command_loop_times += 1
            if self.command_loop_infinite_flag == False:
                if self.command_loop_times < self.loop_times_spinBox.value():

                    try:
                        data_send = self.Command_list_tableWidget.item(
                            self.command_send_index[self.command_next_num], 3).text()
                        # print("data_send = ", data_send)
                        print("self.command_send_index[self.command_next_num] ",
                              self.command_send_index[self.command_next_num])

                    except AttributeError:  # a blank item !!
                        print("AttributeError")
                        # item = ""

                    else:
                        mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic,
                                                           data_send)


                    new_timing = int(self.Command_list_tableWidget.item(
                        self.command_send_index[self.command_next_num], 1).text())

                    self.command_send_timer.start(new_timing)
                    print("command_send_timer.start = ", new_timing)

                else:
                    self.Command_send_progressBar.setValue(100)
                    self.Command_Activate_Button.setChecked(False)
            else:

                try:
                    data_send = self.Command_list_tableWidget.item(
                        self.command_send_index[self.command_next_num], 3).text()
                    # print("data_send = ", data_send)
                    print("self.command_send_index[self.command_next_num] ",
                          self.command_send_index[self.command_next_num])

                except AttributeError:  # a blank item !!
                    print("AttributeError")
                    # item = ""

                else:
                    mqtt_connect.MqttClient.on_publish(mqtt_client, mqtt_connect.MqttSetting.publish_topic, data_send)


                new_timing = int(self.Command_list_tableWidget.item(
                    self.command_send_index[self.command_next_num], 1).text())

                self.command_send_timer.start(new_timing)
                print("command_send_timer.start = ", new_timing)




        # # print(datetime.datetime.now().strftime(TimeFormat))
        #
        # # if len(self.command_send_index) > 0:
        #     # self.command_send_timer = self.Command_list_tableWidget.item(
        #     #     self.command_send_index[int(self.command_next_num)], 1).text()
        #     # print(self.command_send_timer)
        # # print(self.Command_list_tableWidget.item(1, 1).text())
        # self.command_send_timer = int(self.Command_list_tableWidget.item(1, 1).text())
        # print(self.command_send_timer)
        #
        # # self.command_send_timer.start(self.command_send_timer)
        #
        # # print("int(self.command_send_timer) = ", int(self.command_send_timer))
        # # value /= 10
        # # self.Command_send_progressBar.setValue(value)
        # # if value == 90:
        # #     print("value == 90")
        # #     self.commandActivateThread.start()

    def load_insert_command_data(self):
        # path = QtGui.QFileDialog.getOpenFileName(
        #     self, 'Open File', '', 'CSV(*.csv)')
        # if not path.isEmpty():

        # with open('./Data/Command_List.csv') as f:
        #     f_tsv = csv.reader(f, delimiter='\t')
        #     for row in f_tsv:
        #         print(row)
        try:
            load_file = open("./Data/Command_List.csv", "r")

        except FileNotFoundError:  # No file exists
            # print("Unexpected error:", sys.exc_info()[0])
            return "FileNotFoundError"

        else:
            with open('./Data/Command_List.csv', 'r') as f:

                f_tsv = csv.reader(f, delimiter='\t')

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
                            # print("row =", row, "column=", column, " item = ", item)

                    else:
                        row = row - 1
                        for column, data in enumerate(f_tsv):

                            if column == 0:

                                # Insert a checkbox
                                checkBox = QTableWidgetItem()

                                # Set checkBox state
                                if data == "2":
                                    # checkBox = QTableWidgetItem("True")
                                    checkBox.setCheckState(Qt.Checked)

                                elif data == "0":
                                    # checkBox = QTableWidgetItem("False")
                                    checkBox.setCheckState(Qt.Unchecked)

                                self.Command_list_tableWidget.setItem(row, column, checkBox)

                            else:
                                item = QTableWidgetItem(str(data))
                                self.Command_list_tableWidget.setItem(row, column, item)

                                # print("row =", row, "column=", column, " item = ", item)

                # delete the last row
                last_row = self.Command_list_tableWidget.rowCount() - 1
                self.Command_list_tableWidget.removeRow(last_row)

    # # call_back function
    # def receive_messages(self, client, userdata, msg):
    #     receive_time = datetime.datetime.now().strftime(TimeFormat)
    #     mqtt_connect.MqttClient.message_temp = "【" + str(receive_time) + "】" + " Rec -> " + str(msg.payload)
    #     print('receive new message from ' + msg.topic + " -> " + str(msg.payload))
    #     mqtt_connect.storedToLog.info("Rec->" + msg.topic + " -> " + str(msg.payload))
    #     self.mqttDataHandlerThread.messageTrigger.emit(msg.topic + " -> " + str(msg.payload))

    def closeEvent(self, event):

        if self.Connect_EMQ_Button.text() == 'Disconnect from EMQ':
            self.mqttDataHandlerThread.running = False

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
        print("MqttDataHandlerThread started")

    def thread_finished(self):
        print("mqttDataHandlerThread finished")


class CommandActivateThread(QThread):
    commandTrigger = pyqtSignal(int)

    def __init__(self):
        super(CommandActivateThread, self).__init__()
        self.running = True
        self.time_counting = 0

    def __del__(self):
        self.running = False
        self.wait()

    def run(self):
        self.running = True
        self.time_counting = 0
        print(datetime.datetime.now().strftime(TimeFormat))
        while self.running:

            if self.time_counting < Assistant_MainWidow.commmand_next_timing:
                print(self.time_counting)
                time.sleep(0.1)
                self.time_counting += 100

                self.commandTrigger.emit(self.time_counting)

            elif self.time_counting == Assistant_MainWidow.commmand_next_timing:

                print(datetime.datetime.now().strftime(TimeFormat))

                # self.commandTrigger.emit(self.time_counting)
                self.running = False

    def thread_started(self):
        print("CommandActivate started")

    def thread_finished(self):
        print("CommandActivate finished")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mqtt_connect.generate_client_id()

    emq_topic_data = emq_web_get_data.EmqTopicData()

    Assistant_MainWidow = MainWindow()
    Assistant_MainWidow.show()

    mqtt_client = mqtt_connect.MqttClient()

    sys.exit(app.exec_())
