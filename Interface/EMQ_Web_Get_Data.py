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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QDialog, QWidget, QMessageBox
from UI.EMQ_Topic_Get import Ui_EMQ_Topic_Get_Dialog


# current date and time
def get_timestamp():
    now = datetime.now()

    timestamp = datetime.timestamp(now)

    timestamp = int(timestamp * 1000)

    print("timestamp =", timestamp)
    return timestamp

def Get_EMQ_data():

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

        print(web_data.headers)
        print(web_data)
        print(web_data.text)

        web_data_json = web_data.text

        data = json.loads(web_data_json)
        result = data['result']['objects']

        for n in result:
            client_id = n['client_id']
            qos = n['qos']
            topic = n['topic']

            print(client_id, qos, topic)
    # return data


class EmqTopicData(QDialog, Ui_EMQ_Topic_Get_Dialog):



    def __init__(self, parent=None):
        super(EmqTopicData, self).__init__(parent)

        self.setupUi(self)

    # def show(self):
    #     self.show()







if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    emq_topic_data = EmqTopicData()
    emq_topic_data.show()

    data = Get_EMQ_data()
    print(data)


    sys.exit(app.exec_())