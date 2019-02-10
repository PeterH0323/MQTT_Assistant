# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JT_EMQ_Test_Assistant_UI_Simple.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JT_EMQ_Test_Assistant(object):
    def setupUi(self, JT_EMQ_Test_Assistant):
        JT_EMQ_Test_Assistant.setObjectName("JT_EMQ_Test_Assistant")
        JT_EMQ_Test_Assistant.setEnabled(True)
        JT_EMQ_Test_Assistant.resize(1199, 1015)
        JT_EMQ_Test_Assistant.setAutoFillBackground(False)
        JT_EMQ_Test_Assistant.setStyleSheet("background-color:white;\n"
"\n"
"")
        JT_EMQ_Test_Assistant.setIconSize(QtCore.QSize(20, 30))
        self.centralwidget = QtWidgets.QWidget(JT_EMQ_Test_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.Connect_EMQ_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_EMQ_Button.setGeometry(QtCore.QRect(930, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_EMQ_Button.setFont(font)
        self.Connect_EMQ_Button.setStyleSheet("QPushButton{\n"
"    background-color:#16A085;\n"
"    color:#ffffff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#FFFFFF;\n"
"    background:#2EE1C1;\n"
"}\n"
"")
        self.Connect_EMQ_Button.setObjectName("Connect_EMQ_Button")
        self.Emq_connect_lable = QtWidgets.QLabel(self.centralwidget)
        self.Emq_connect_lable.setGeometry(QtCore.QRect(940, 150, 181, 31))
        self.Emq_connect_lable.setStyleSheet("QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, \n"
"QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {\n"
"    background-color: #222222;\n"
"    color: #BBBBBB;\n"
"    font-family: \"Calibri\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.Emq_connect_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Emq_connect_lable.setObjectName("Emq_connect_lable")
        self.EMQ_Setting_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.EMQ_Setting_groupBox.setGeometry(QtCore.QRect(60, 30, 821, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.EMQ_Setting_groupBox.setFont(font)
        self.EMQ_Setting_groupBox.setStyleSheet("QGroupBox {\n"
"    /* background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #E0E0E0, stop: 1 #FFFFFF);*/\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FFOECE, stop: 1 #FFFFFF);\n"
"}\n"
"")
        self.EMQ_Setting_groupBox.setObjectName("EMQ_Setting_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.EMQ_Setting_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 37))
        self.label_2.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.Host_lineEdit = QtWidgets.QLineEdit(self.splitter_4)
        self.Host_lineEdit.setMinimumSize(QtCore.QSize(270, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.Host_lineEdit.setFont(font)
        self.Host_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.Host_lineEdit.setPlaceholderText("")
        self.Host_lineEdit.setObjectName("Host_lineEdit")
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        self.label_5.setMinimumSize(QtCore.QSize(100, 37))
        self.label_5.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.Username_lineEdit = QtWidgets.QLineEdit(self.splitter_5)
        self.Username_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.Username_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.Username_lineEdit.setPlaceholderText("")
        self.Username_lineEdit.setObjectName("Username_lineEdit")
        self.gridLayout.addWidget(self.splitter_5, 0, 2, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setMinimumSize(QtCore.QSize(100, 37))
        self.label_3.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.Port_lineEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.Port_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.Port_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.Port_lineEdit.setPlaceholderText("")
        self.Port_lineEdit.setObjectName("Port_lineEdit")
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)
        self.splitter_6 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_6.setMinimumSize(QtCore.QSize(30, 10))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_6 = QtWidgets.QLabel(self.splitter_6)
        self.label_6.setMinimumSize(QtCore.QSize(100, 37))
        self.label_6.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.Password_lineEdit = QtWidgets.QLineEdit(self.splitter_6)
        self.Password_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.Password_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.Password_lineEdit.setPlaceholderText("")
        self.Password_lineEdit.setObjectName("Password_lineEdit")
        self.gridLayout.addWidget(self.splitter_6, 1, 2, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setMinimumSize(QtCore.QSize(100, 37))
        self.label_4.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.ClientID_lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.ClientID_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.ClientID_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.ClientID_lineEdit.setPlaceholderText("")
        self.ClientID_lineEdit.setObjectName("ClientID_lineEdit")
        self.gridLayout.addWidget(self.splitter_2, 2, 0, 1, 1)
        self.splitter_7 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_9 = QtWidgets.QLabel(self.splitter_7)
        self.label_9.setMinimumSize(QtCore.QSize(100, 37))
        self.label_9.setMaximumSize(QtCore.QSize(100, 37))
        self.label_9.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.PublishTopic_lineEdit = QtWidgets.QLineEdit(self.splitter_7)
        self.PublishTopic_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.PublishTopic_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.PublishTopic_lineEdit.setPlaceholderText("")
        self.PublishTopic_lineEdit.setObjectName("PublishTopic_lineEdit")
        self.gridLayout.addWidget(self.splitter_7, 2, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        self.label_8.setMinimumSize(QtCore.QSize(100, 37))
        self.label_8.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.KeepAlive_lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.KeepAlive_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.KeepAlive_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.KeepAlive_lineEdit.setPlaceholderText("")
        self.KeepAlive_lineEdit.setObjectName("KeepAlive_lineEdit")
        self.gridLayout.addWidget(self.splitter, 3, 0, 1, 1)
        self.splitter_8 = QtWidgets.QSplitter(self.EMQ_Setting_groupBox)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_10 = QtWidgets.QLabel(self.splitter_8)
        self.label_10.setMinimumSize(QtCore.QSize(100, 37))
        self.label_10.setMaximumSize(QtCore.QSize(100, 37))
        self.label_10.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"   /* border: 2px solid blue;*/\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:11px;\n"
"    font-weight:bold;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.SubTopic_lineEdit = QtWidgets.QLineEdit(self.splitter_8)
        self.SubTopic_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.SubTopic_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.SubTopic_lineEdit.setPlaceholderText("")
        self.SubTopic_lineEdit.setObjectName("SubTopic_lineEdit")
        self.gridLayout.addWidget(self.splitter_8, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.R_S_Data_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.R_S_Data_groupBox.setGeometry(QtCore.QRect(50, 290, 551, 641))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.R_S_Data_groupBox.setFont(font)
        self.R_S_Data_groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FFOECE, stop: 1 #FFFFFF);\n"
"}")
        self.R_S_Data_groupBox.setObjectName("R_S_Data_groupBox")
        self.EMQ_Data_textEdit = QtWidgets.QTextEdit(self.R_S_Data_groupBox)
        self.EMQ_Data_textEdit.setGeometry(QtCore.QRect(10, 20, 521, 571))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.EMQ_Data_textEdit.setFont(font)
        self.EMQ_Data_textEdit.setStyleSheet("\n"
"QTextEdit {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"")
        self.EMQ_Data_textEdit.setObjectName("EMQ_Data_textEdit")
        self.Save_Log_checkBox = QtWidgets.QCheckBox(self.R_S_Data_groupBox)
        self.Save_Log_checkBox.setGeometry(QtCore.QRect(340, 600, 91, 31))
        self.Save_Log_checkBox.setStyleSheet("")
        self.Save_Log_checkBox.setObjectName("Save_Log_checkBox")
        self.Rec_Data_Clean_Button = QtWidgets.QPushButton(self.R_S_Data_groupBox)
        self.Rec_Data_Clean_Button.setGeometry(QtCore.QRect(440, 600, 93, 28))
        self.Rec_Data_Clean_Button.setStyleSheet("QPushButton{    \n"
"    border:2px solid #8f8f91;\n"
"    border-radius:6px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#f6f7fa, stop: 1 #dadbde);\n"
"    min-width:80px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"stop:0#dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"border: none;/* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default{\n"
"border-color: navy;/* make the default button prominent */\n"
"}")
        self.Rec_Data_Clean_Button.setObjectName("Rec_Data_Clean_Button")
        self.Command_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Command_groupBox.setGeometry(QtCore.QRect(620, 290, 541, 641))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Command_groupBox.setFont(font)
        self.Command_groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 3ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FFOECE, stop: 1 #FFFFFF);\n"
"}")
        self.Command_groupBox.setObjectName("Command_groupBox")
        self.Command_list_tableWidget = QtWidgets.QTableWidget(self.Command_groupBox)
        self.Command_list_tableWidget.setGeometry(QtCore.QRect(10, 80, 521, 511))
        self.Command_list_tableWidget.setObjectName("Command_list_tableWidget")
        self.Command_list_tableWidget.setColumnCount(4)
        self.Command_list_tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(3, item)
        self.Command_Add_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Add_Button.setGeometry(QtCore.QRect(330, 600, 93, 28))
        self.Command_Add_Button.setStyleSheet("QPushButton{    \n"
"    border:2px solid #8f8f91;\n"
"    border-radius:6px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#f6f7fa, stop: 1 #dadbde);\n"
"    min-width:80px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"stop:0#dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"border: none;/* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default{\n"
"border-color: navy;/* make the default button prominent */\n"
"}")
        self.Command_Add_Button.setObjectName("Command_Add_Button")
        self.Command_Del_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Del_Button.setGeometry(QtCore.QRect(430, 600, 93, 28))
        self.Command_Del_Button.setStyleSheet("QPushButton{    \n"
"    border:2px solid #8f8f91;\n"
"    border-radius:6px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#f6f7fa, stop: 1 #dadbde);\n"
"    min-width:80px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"stop:0#dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"border: none;/* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default{\n"
"border-color: navy;/* make the default button prominent */\n"
"}")
        self.Command_Del_Button.setObjectName("Command_Del_Button")
        self.Command_Activate_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Activate_Button.setEnabled(False)
        self.Command_Activate_Button.setGeometry(QtCore.QRect(20, 600, 91, 28))
        self.Command_Activate_Button.setStyleSheet("QPushButton{    \n"
"    border:2px solid #8f8f91;\n"
"    border-radius:6px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#f6f7fa, stop: 1 #dadbde);\n"
"    min-width:80px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"stop:0#dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"border: none;/* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default{\n"
"border-color: navy;/* make the default button prominent */\n"
"}")
        self.Command_Activate_Button.setObjectName("Command_Activate_Button")
        self.Command_Data_lineEdit = QtWidgets.QLineEdit(self.Command_groupBox)
        self.Command_Data_lineEdit.setGeometry(QtCore.QRect(10, 20, 411, 41))
        self.Command_Data_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.Command_Data_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style:none;\n"
"    padding:6px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #3498DB;\n"
"}")
        self.Command_Data_lineEdit.setPlaceholderText("")
        self.Command_Data_lineEdit.setObjectName("Command_Data_lineEdit")
        self.Command_Send_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Send_Button.setEnabled(False)
        self.Command_Send_Button.setGeometry(QtCore.QRect(440, 20, 84, 41))
        self.Command_Send_Button.setStyleSheet("QPushButton{    \n"
"    border:2px solid #8f8f91;\n"
"    border-radius:6px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#f6f7fa, stop: 1 #dadbde);\n"
"    min-width:80px;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0#dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"border: none;/* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default{\n"
"border-color: navy;/* make the default button prominent */\n"
"}")
        self.Command_Send_Button.setObjectName("Command_Send_Button")
        JT_EMQ_Test_Assistant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JT_EMQ_Test_Assistant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        JT_EMQ_Test_Assistant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JT_EMQ_Test_Assistant)
        self.statusbar.setObjectName("statusbar")
        JT_EMQ_Test_Assistant.setStatusBar(self.statusbar)
        self.actionImport_configuration_file = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionImport_configuration_file.setEnabled(False)
        self.actionImport_configuration_file.setShortcut("")
        self.actionImport_configuration_file.setObjectName("actionImport_configuration_file")
        self.actionEMQ = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionEMQ.setEnabled(False)
        self.actionEMQ.setObjectName("actionEMQ")
        self.actionConnect_EMQ_Button = QtWidgets.QAction(JT_EMQ_Test_Assistant)
        self.actionConnect_EMQ_Button.setObjectName("actionConnect_EMQ_Button")
        self.menuFile.addAction(self.actionImport_configuration_file)
        self.menuSetting.addAction(self.actionEMQ)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(JT_EMQ_Test_Assistant)
        QtCore.QMetaObject.connectSlotsByName(JT_EMQ_Test_Assistant)
        JT_EMQ_Test_Assistant.setTabOrder(self.Connect_EMQ_Button, self.Host_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Host_lineEdit, self.Username_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Username_lineEdit, self.Port_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Port_lineEdit, self.Password_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Password_lineEdit, self.ClientID_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.ClientID_lineEdit, self.PublishTopic_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.PublishTopic_lineEdit, self.KeepAlive_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.KeepAlive_lineEdit, self.SubTopic_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.SubTopic_lineEdit, self.Command_Data_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_Data_lineEdit, self.Command_Send_Button)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_Send_Button, self.EMQ_Data_textEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.EMQ_Data_textEdit, self.Command_list_tableWidget)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_list_tableWidget, self.Save_Log_checkBox)
        JT_EMQ_Test_Assistant.setTabOrder(self.Save_Log_checkBox, self.Rec_Data_Clean_Button)
        JT_EMQ_Test_Assistant.setTabOrder(self.Rec_Data_Clean_Button, self.Command_Activate_Button)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_Activate_Button, self.Command_Add_Button)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_Add_Button, self.Command_Del_Button)

    def retranslateUi(self, JT_EMQ_Test_Assistant):
        _translate = QtCore.QCoreApplication.translate
        JT_EMQ_Test_Assistant.setWindowTitle(_translate("JT_EMQ_Test_Assistant", "MainWindow"))
        self.Connect_EMQ_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ accroding to setting"))
        self.Connect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ"))
        self.Emq_connect_lable.setText(_translate("JT_EMQ_Test_Assistant", "EMQ Disconnect"))
        self.EMQ_Setting_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "EMQ Setting"))
        self.label_2.setText(_translate("JT_EMQ_Test_Assistant", "Host:"))
        self.Host_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "139.159.163.25"))
        self.label_5.setText(_translate("JT_EMQ_Test_Assistant", "Username:"))
        self.Username_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "eie-device"))
        self.label_3.setText(_translate("JT_EMQ_Test_Assistant", "Port:"))
        self.Port_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "8083"))
        self.label_6.setText(_translate("JT_EMQ_Test_Assistant", "Password:"))
        self.Password_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "Eie_28918499"))
        self.label_4.setText(_translate("JT_EMQ_Test_Assistant", "Client ID:"))
        self.ClientID_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "mqtt_test_assistant"))
        self.label_9.setText(_translate("JT_EMQ_Test_Assistant", "Publish Topic: "))
        self.PublishTopic_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "EIE/out/00000000/00000001"))
        self.label_8.setText(_translate("JT_EMQ_Test_Assistant", "Keep Alive:"))
        self.KeepAlive_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "120"))
        self.label_10.setText(_translate("JT_EMQ_Test_Assistant", "Subscribe Topic: "))
        self.SubTopic_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "EIE/in/00000000/00000001"))
        self.R_S_Data_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "Receive + Send Data "))
        self.EMQ_Data_textEdit.setHtml(_translate("JT_EMQ_Test_Assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibir\'; font-size:12pt; font-weight:400;\"><br /></p></body></html>"))
        self.Save_Log_checkBox.setText(_translate("JT_EMQ_Test_Assistant", "Save log"))
        self.Rec_Data_Clean_Button.setText(_translate("JT_EMQ_Test_Assistant", "Clean"))
        self.Command_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "Command List"))
        item = self.Command_list_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("JT_EMQ_Test_Assistant", "1"))
        item = self.Command_list_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("JT_EMQ_Test_Assistant", "2"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Command Name"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Data"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Intervals(ms)"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Activate"))
        self.Command_Add_Button.setText(_translate("JT_EMQ_Test_Assistant", "Add"))
        self.Command_Del_Button.setText(_translate("JT_EMQ_Test_Assistant", "Del"))
        self.Command_Activate_Button.setText(_translate("JT_EMQ_Test_Assistant", "Activate"))
        self.Command_Data_lineEdit.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Data you want to send"))
        self.Command_Data_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "Hey mate. "))
        self.Command_Send_Button.setText(_translate("JT_EMQ_Test_Assistant", "Send(&Q)"))
        self.menuFile.setTitle(_translate("JT_EMQ_Test_Assistant", "File(&F)"))
        self.menuSetting.setTitle(_translate("JT_EMQ_Test_Assistant", "Setting(&S)"))
        self.actionImport_configuration_file.setText(_translate("JT_EMQ_Test_Assistant", "Import Configuration file"))
        self.actionEMQ.setText(_translate("JT_EMQ_Test_Assistant", "EMQ"))
        self.actionEMQ.setStatusTip(_translate("JT_EMQ_Test_Assistant", "EMQ Setting"))
        self.actionEMQ.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+S"))
        self.actionConnect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "actionConnect_EMQ_Button"))

