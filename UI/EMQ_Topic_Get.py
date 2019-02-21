# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EMQ_Topic_Get.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EMQ_Topic_Get_Dialog(object):
    def setupUi(self, EMQ_Topic_Get_Dialog):
        EMQ_Topic_Get_Dialog.setObjectName("EMQ_Topic_Get_Dialog")
        EMQ_Topic_Get_Dialog.resize(873, 624)
        self.tableWidget = QtWidgets.QTableWidget(EMQ_Topic_Get_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(370, 170, 451, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.listWidget = QtWidgets.QListWidget(EMQ_Topic_Get_Dialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 170, 321, 261))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(EMQ_Topic_Get_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(610, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(EMQ_Topic_Get_Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 540, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(EMQ_Topic_Get_Dialog)
        QtCore.QMetaObject.connectSlotsByName(EMQ_Topic_Get_Dialog)

    def retranslateUi(self, EMQ_Topic_Get_Dialog):
        _translate = QtCore.QCoreApplication.translate
        EMQ_Topic_Get_Dialog.setWindowTitle(_translate("EMQ_Topic_Get_Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "Client id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "Topic"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "新建项目"))
        item = self.listWidget.item(1)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "新建项目"))
        item = self.listWidget.item(2)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("EMQ_Topic_Get_Dialog", "OK"))
        self.pushButton_2.setText(_translate("EMQ_Topic_Get_Dialog", "Cancel"))

