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
        EMQ_Topic_Get_Dialog.resize(563, 467)
        self.gridLayout = QtWidgets.QGridLayout(EMQ_Topic_Get_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.EMQ_Data_tableWidget = QtWidgets.QTableWidget(EMQ_Topic_Get_Dialog)
        self.EMQ_Data_tableWidget.setStyleSheet("/* 标题头 每个单独的标题区域*/\n"
"QHeaderView::section {\n"
"\n"
"    font-size:14px;                /* 每个标题的字体大小*/\n"
"    font-family:\"Microsoft YaHei\"; /* 每个标题的字体类型*/\n"
"    color:#FFFFFF;                 /* 每个标题的字体颜色*/\n"
"\n"
"    background:#ff8a37;            /* 每个标题区域的背景色*/\n"
"    border:none;                   /* 每个标题区域的边框*/\n"
"\n"
"    min-height:49px;               /* 标题区域的高度*/\n"
"    max-height:49px;              \n"
"\n"
"    margin-left:0px;               /* 每个标题区域的margin*/\n"
"    padding-left:0px;              /* 每个标题区域的padding*/\n"
"}\n"
"\n"
"/* 整个表格控件*/\n"
"QTableWidget{\n"
"    background:#FFFFFF;            /* 整个表格控件 背景色*/\n"
"    border:none;                   /* 整个表格控件 边框*/\n"
"\n"
"    font-size:12px;                /* 所有字体大小*/\n"
"    font-family:\"Microsoft YaHei\"; /* 所有字体 family*/\n"
"    color:#666666;                 /* 所有字体颜色*/\n"
"}\n"
"\n"
"/* 每个单元格*/\n"
"QTableWidget::item {\n"
"    border-bottom:1px solid #EEF1F7 ; /* 只显示每个单元格下边框*/\n"
"}\n"
"\n"
"/* 每个单元格被选中状态*/\n"
"QTableWidget::item::selected {\n"
"\n"
"    color:#ff6a38;                         /*每个单元格被选中时 字体颜色*/\n"
"    background:#EFF4FF;                /*每个单元格被选中时 背景颜色*/\n"
"}\n"
"\n"
"QTableView::indicator:unchecked {\n"
"    image: url(./images/checkBox2_unchecked.png)\n"
"}\n"
"\n"
"QTableView::indicator:checked {\n"
"    image: url(./images/checkBox2_checked.png)\n"
"}\n"
"\n"
"\n"
"")
        self.EMQ_Data_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.EMQ_Data_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.EMQ_Data_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.EMQ_Data_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.EMQ_Data_tableWidget.setObjectName("EMQ_Data_tableWidget")
        self.EMQ_Data_tableWidget.setColumnCount(2)
        self.EMQ_Data_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EMQ_Data_tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.EMQ_Data_tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.EMQ_Data_Dialog_OK_Button = QtWidgets.QPushButton(EMQ_Topic_Get_Dialog)
        self.EMQ_Data_Dialog_OK_Button.setEnabled(False)
        self.EMQ_Data_Dialog_OK_Button.setObjectName("EMQ_Data_Dialog_OK_Button")
        self.horizontalLayout.addWidget(self.EMQ_Data_Dialog_OK_Button)
        self.EMQ_Data_Dialog_Cancel_Button = QtWidgets.QPushButton(EMQ_Topic_Get_Dialog)
        self.EMQ_Data_Dialog_Cancel_Button.setObjectName("EMQ_Data_Dialog_Cancel_Button")
        self.horizontalLayout.addWidget(self.EMQ_Data_Dialog_Cancel_Button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(EMQ_Topic_Get_Dialog)
        QtCore.QMetaObject.connectSlotsByName(EMQ_Topic_Get_Dialog)

    def retranslateUi(self, EMQ_Topic_Get_Dialog):
        _translate = QtCore.QCoreApplication.translate
        EMQ_Topic_Get_Dialog.setWindowTitle(_translate("EMQ_Topic_Get_Dialog", "Dialog"))
        item = self.EMQ_Data_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "Client id"))
        item = self.EMQ_Data_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EMQ_Topic_Get_Dialog", "Topic"))
        self.EMQ_Data_Dialog_OK_Button.setText(_translate("EMQ_Topic_Get_Dialog", "OK"))
        self.EMQ_Data_Dialog_Cancel_Button.setText(_translate("EMQ_Topic_Get_Dialog", "Cancel"))

