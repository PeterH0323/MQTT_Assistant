# -*- coding: utf-8 -*-
# Programmer : PeterH 
# Date: 2019.02.20


"""
https://zhuanlan.zhihu.com/p/24838761
http://docs.python-requests.org/zh_CN/latest/user/authentication.html -> 基本身份验证
"""

# '''
# # Log in to EMQ：
# '''
# import json
# import requests

# url = 'http://139.159.163.25:18083/#/subscriptions'
# payload = {'username': 'admin', 'password': 'Eie28918499'}
# headers = {'content-type': 'application/json'}
# r = requests.post(url, data=json.dumps(payload), headers=headers)
# print(r.text)

from requests.auth import HTTPBasicAuth
import json
import requests
from datetime import datetime
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from UI.EMQ_Topic_Get import Ui_EMQ_Topic_Get_Dialog

import pyperclip


# import JT_EMQ_Test_Assistant_Simple


# current date and time
def get_timestamp():
    now = datetime.now()

    timestamp = datetime.timestamp(now)

    timestamp = int(timestamp * 1000)

    print("timestamp =", timestamp)
    return timestamp


class EmqTopicData(QDialog, Ui_EMQ_Topic_Get_Dialog):
    selected_topic = ''

    def __init__(self, parent=None):
        super(EmqTopicData, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("EMQ Topic Data")

        '''
             PyQt Slot connect
        '''
        self.EMQ_Data_Dialog_Cancel_Button.clicked.connect(self.close)
        self.EMQ_Data_Dialog_OK_Button.clicked.connect(self.emq_data_dialog_ok_button_clicked)
        self.EMQ_Data_tableWidget.itemClicked.connect(self.emq_data_tableWidget_item_clicked)

    def Get_Extranet_EMQ_data(self):

        '''
            Init the tableWidget
        '''
        self.EMQ_Data_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.EMQ_Data_tableWidget.setRowCount(0)
        self.EMQ_Data_tableWidget.setColumnCount(0)

        self.EMQ_Data_tableWidget.setColumnCount(2)

        item = QTableWidgetItem("Client ID")
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Topic")
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(1, item)

        timestamp = get_timestamp()

        url = 'http://139.159.163.25:18083/api/v2/nodes/emq@127.0.0.1/subscriptions?curr_page=1&page_size=10&timestamps=' + str(
            timestamp)

        web_data = requests.get(url, auth=HTTPBasicAuth('admin', 'Eie28918499'))
        # print(web_data.headers)
        # print(web_data)
        # print(web_data.text)
        wbdata = web_data.text
        data = json.loads(wbdata)
        total_page = int(data['result']['total_page'])
        print("total_page = ", total_page)

        for m in range(1, total_page + 1):
            url = 'http://139.159.163.25:18083/api/v2/nodes/emq@127.0.0.1/subscriptions?curr_page=' + str(
                m) + '&page_size=10&timestamps=' + str(timestamp)
            print(url)

            web_data = requests.get(url, auth=HTTPBasicAuth('admin', 'Eie28918499'))

            # print(web_data.headers)
            # print(web_data)
            # print(web_data.text)

            web_data_json = web_data.text

            data = json.loads(web_data_json)
            result = data['result']['objects']

            for n in result:
                client_id = n['client_id']
                qos = n['qos']
                topic = n['topic']

                # print(client_id, qos, topic)

                row = self.EMQ_Data_tableWidget.rowCount()
                self.EMQ_Data_tableWidget.insertRow(row)
                item = QTableWidgetItem(str(client_id))
                self.EMQ_Data_tableWidget.setItem(row, 0, item)
                item = QTableWidgetItem(str(topic))
                self.EMQ_Data_tableWidget.setItem(row, 1, item)

        self.ClipBox_Message_lable.setText("Click OK to copy to clip box !")

    def Get_Intranet_EMQ_data(self):

        '''
            Init the tableWidget
        '''
        self.EMQ_Data_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.EMQ_Data_tableWidget.setRowCount(0)
        self.EMQ_Data_tableWidget.setColumnCount(0)

        self.EMQ_Data_tableWidget.setColumnCount(2)

        item = QTableWidgetItem("Client ID")
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Topic")
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(1, item)

        timestamp = get_timestamp()

        url = 'http://192.168.1.113:18083/api/v3/subscriptions?_page=1&_limit=10&_=' + str(timestamp)

        web_data = requests.get(url, auth=HTTPBasicAuth('admin', 'public'))
        # print(web_data.headers)
        # print(web_data)
        # print(web_data.text)
        wbdata = web_data.text
        data = json.loads(wbdata)
        total_page = int(data['meta']['page'])
        print("total_page = ", total_page)

        for m in range(1, total_page + 1):

            url = 'http://192.168.1.113:18083/api/v3/subscriptions?_page=' + str(m) + '&_limit=10&_=' + str(timestamp)

            print(url)

            web_data = requests.get(url, auth=HTTPBasicAuth('admin', 'public'))

            print(web_data.headers)
            print(web_data)
            print(web_data.text)

            web_data_json = web_data.text

            data = json.loads(web_data_json)
            result = data['data']

            for n in result:
                client_id = n['client_id']
                topic = n['topic']

                # print(client_id, qos, topic)

                row = self.EMQ_Data_tableWidget.rowCount()
                self.EMQ_Data_tableWidget.insertRow(row)
                item = QTableWidgetItem(str(client_id))
                self.EMQ_Data_tableWidget.setItem(row, 0, item)
                item = QTableWidgetItem(str(topic))
                self.EMQ_Data_tableWidget.setItem(row, 1, item)

        self.ClipBox_Message_lable.setText("Click OK to copy to clip box !")



    @pyqtSlot()
    def emq_data_tableWidget_item_clicked(self):
        self.EMQ_Data_Dialog_OK_Button.setEnabled(True)

    @pyqtSlot()
    def emq_data_dialog_ok_button_clicked(self):

        # get selected row
        selected_row = self.EMQ_Data_tableWidget.currentRow()

        if selected_row != -1:
            selected_topic = self.EMQ_Data_tableWidget.item(selected_row, 1).text()

            # else:
            print(selected_topic)
            pyperclip.copy(selected_topic)

            # self.ClipBox_Message_lable.setText(" Copied Done !")

            self.close()

            # JT_EMQ_Test_Assistant_Simple.MainWindow.PublishTopic_lineEdit.setText("Hi")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    emq_topic_data = EmqTopicData()
    emq_topic_data.show()

    emq_topic_data.Get_EMQ_data()
    # print(data)

    sys.exit(app.exec_())
