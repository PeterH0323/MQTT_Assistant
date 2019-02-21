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
        JT_EMQ_Test_Assistant.resize(1191, 921)
        JT_EMQ_Test_Assistant.setAutoFillBackground(False)
        JT_EMQ_Test_Assistant.setStyleSheet("QMainWindow    {\n"
"    background-color:white;\n"
"}\n"
"\n"
"/*\n"
"QStatusBar {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"    background-color: #148CD2;\n"
"    border: 1px solid #19232D;\n"
"    color: #19232D;\n"
"    padding: 0;   //remove padding, for fix combo box tooltip\n"
"    opacity: 230; //reducing transparency to read better\n"
"}\n"
"*/\n"
"")
        JT_EMQ_Test_Assistant.setIconSize(QtCore.QSize(20, 30))
        self.centralwidget = QtWidgets.QWidget(JT_EMQ_Test_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EMQ_Setting_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.EMQ_Setting_groupBox.setMaximumSize(QtCore.QSize(824, 300))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
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
        self.horizontalLayout.addWidget(self.EMQ_Setting_groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.Check_EMQ_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Check_EMQ_Button.sizePolicy().hasHeightForWidth())
        self.Check_EMQ_Button.setSizePolicy(sizePolicy)
        self.Check_EMQ_Button.setMinimumSize(QtCore.QSize(201, 30))
        self.Check_EMQ_Button.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Check_EMQ_Button.setFont(font)
        self.Check_EMQ_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Check_EMQ_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Check_EMQ_Button.setStyleSheet("QPushButton{\n"
"    background-color:#66CCFF;\n"
"    color:#ffffff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#FFFFFF;\n"
"    background:#99FFFF;\n"
"}\n"
"")
        self.Check_EMQ_Button.setObjectName("Check_EMQ_Button")
        self.verticalLayout.addWidget(self.Check_EMQ_Button)
        self.Connect_EMQ_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connect_EMQ_Button.sizePolicy().hasHeightForWidth())
        self.Connect_EMQ_Button.setSizePolicy(sizePolicy)
        self.Connect_EMQ_Button.setMinimumSize(QtCore.QSize(201, 51))
        self.Connect_EMQ_Button.setMaximumSize(QtCore.QSize(201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_EMQ_Button.setFont(font)
        self.Connect_EMQ_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Connect_EMQ_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
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
        self.verticalLayout.addWidget(self.Connect_EMQ_Button)
        self.Emq_connect_lable = QtWidgets.QLabel(self.centralwidget)
        self.Emq_connect_lable.setMinimumSize(QtCore.QSize(201, 31))
        self.Emq_connect_lable.setMaximumSize(QtCore.QSize(201, 31))
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
        self.verticalLayout.addWidget(self.Emq_connect_lable)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.R_S_Data_groupBox = QtWidgets.QGroupBox(self.widget)
        self.R_S_Data_groupBox.setMinimumSize(QtCore.QSize(543, 0))
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.R_S_Data_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.EMQ_Data_textEdit = QtWidgets.QTextEdit(self.R_S_Data_groupBox)
        self.EMQ_Data_textEdit.setMinimumSize(QtCore.QSize(521, 0))
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
        self.gridLayout_2.addWidget(self.EMQ_Data_textEdit, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Save_Log_checkBox = QtWidgets.QCheckBox(self.R_S_Data_groupBox)
        self.Save_Log_checkBox.setMaximumSize(QtCore.QSize(16777215, 28))
        self.Save_Log_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Save_Log_checkBox.setStyleSheet("/*RadioButton和checkbox字体和间距设置*/\n"
"QRadioButton ,QCheckBox{\n"
"    spacing: 5px;\n"
"    font-family: \"Calibri\";\n"
"    font-weight:bold;\n"
"    font-size:15px\n"
"}\n"
"/*checkbox样式设置*/\n"
"QCheckBox::indicator { \n"
"    width: 26px;\n"
"    height: 50px;\n"
"}\n"
"/*未选中*/\n"
"QCheckBox::indicator::unchecked {   \n"
"    image: url(./images/checkbox_unchecked.png);\n"
"}\n"
"/*选中*/\n"
"QCheckBox::indicator::checked { \n"
"    image: url(./images/checkbox_checked.png);\n"
"}")
        self.Save_Log_checkBox.setIconSize(QtCore.QSize(40, 40))
        self.Save_Log_checkBox.setChecked(True)
        self.Save_Log_checkBox.setTristate(False)
        self.Save_Log_checkBox.setObjectName("Save_Log_checkBox")
        self.horizontalLayout_4.addWidget(self.Save_Log_checkBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.textEdit_Fianl_Line_Button = QtWidgets.QPushButton(self.R_S_Data_groupBox)
        self.textEdit_Fianl_Line_Button.setMinimumSize(QtCore.QSize(84, 28))
        self.textEdit_Fianl_Line_Button.setMaximumSize(QtCore.QSize(91, 28))
        self.textEdit_Fianl_Line_Button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.textEdit_Fianl_Line_Button.setStyleSheet("QPushButton{    \n"
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
        self.textEdit_Fianl_Line_Button.setObjectName("textEdit_Fianl_Line_Button")
        self.horizontalLayout_4.addWidget(self.textEdit_Fianl_Line_Button)
        self.Rec_Data_Clean_Button = QtWidgets.QPushButton(self.R_S_Data_groupBox)
        self.Rec_Data_Clean_Button.setMinimumSize(QtCore.QSize(84, 28))
        self.Rec_Data_Clean_Button.setMaximumSize(QtCore.QSize(91, 28))
        self.Rec_Data_Clean_Button.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
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
        self.horizontalLayout_4.addWidget(self.Rec_Data_Clean_Button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.R_S_Data_groupBox, 0, 1, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(15, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 1, 4, 1, 1)
        self.Command_groupBox = QtWidgets.QGroupBox(self.widget)
        self.Command_groupBox.setMinimumSize(QtCore.QSize(541, 0))
        self.Command_groupBox.setMaximumSize(QtCore.QSize(1000, 16777215))
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Command_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Command_send_progressBar = QtWidgets.QProgressBar(self.Command_groupBox)
        self.Command_send_progressBar.setStyleSheet("/**********进度条*********\n"
"QProgressBar{\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background: rgb(48, 50, 51);\n"
"}\n"
"QProgressBar::chunk {\n"
"        background: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QProgressBar#progressBar {\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/Black/progressBar\");\n"
"        background-repeat: repeat-x;\n"
"}\n"
"QProgressBar#progressBar::chunk {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/Black/progressBarChunk\");\n"
"        background-repeat: repeat-x;\n"
"}*/\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 1px;\n"
"}\n"
"\n"
"/*\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}\n"
"*/\n"
"\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    font-familly:\"Calibri\";\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"\n"
"")
        self.Command_send_progressBar.setProperty("value", 0)
        self.Command_send_progressBar.setObjectName("Command_send_progressBar")
        self.gridLayout_4.addWidget(self.Command_send_progressBar, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Command_Data_lineEdit = QtWidgets.QLineEdit(self.Command_groupBox)
        self.Command_Data_lineEdit.setMinimumSize(QtCore.QSize(270, 37))
        self.Command_Data_lineEdit.setMaximumSize(QtCore.QSize(500, 37))
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
"    border:2px solid #4DB34D;\n"
"}")
        self.Command_Data_lineEdit.setPlaceholderText("")
        self.Command_Data_lineEdit.setObjectName("Command_Data_lineEdit")
        self.horizontalLayout_5.addWidget(self.Command_Data_lineEdit)
        self.Command_Send_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Send_Button.setEnabled(False)
        self.Command_Send_Button.setMaximumSize(QtCore.QSize(84, 28))
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
        self.horizontalLayout_5.addWidget(self.Command_Send_Button)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.Command_list_tableWidget = QtWidgets.QTableWidget(self.Command_groupBox)
        self.Command_list_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Command_list_tableWidget.setAutoFillBackground(False)
        self.Command_list_tableWidget.setStyleSheet("/* 标题头 每个单独的标题区域*/\n"
"QHeaderView::section {\n"
"\n"
"    font-size:14px;                /* 每个标题的字体大小*/\n"
"    font-family:\"Microsoft YaHei\"; /* 每个标题的字体类型*/\n"
"    color:#FFFFFF;                 /* 每个标题的字体颜色*/\n"
"\n"
"    background:#60669B;            /* 每个标题区域的背景色*/\n"
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
"    color:red;                         /*每个单元格被选中时 字体颜色*/\n"
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
"QScrollBar:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: white;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.Command_list_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Command_list_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Command_list_tableWidget.setObjectName("Command_list_tableWidget")
        self.Command_list_tableWidget.setColumnCount(4)
        self.Command_list_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Command_list_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Command_list_tableWidget.setHorizontalHeaderItem(3, item)
        self.Command_list_tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.gridLayout_4.addWidget(self.Command_list_tableWidget, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Command_Single_Send_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Single_Send_Button.setEnabled(False)
        self.Command_Single_Send_Button.setMinimumSize(QtCore.QSize(84, 28))
        self.Command_Single_Send_Button.setMaximumSize(QtCore.QSize(150, 28))
        self.Command_Single_Send_Button.setStyleSheet("QPushButton{    \n"
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
        self.Command_Single_Send_Button.setObjectName("Command_Single_Send_Button")
        self.horizontalLayout_6.addWidget(self.Command_Single_Send_Button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.Command_Activate_Button = QtWidgets.QCheckBox(self.Command_groupBox)
        self.Command_Activate_Button.setEnabled(False)
        self.Command_Activate_Button.setMinimumSize(QtCore.QSize(90, 28))
        self.Command_Activate_Button.setMaximumSize(QtCore.QSize(84, 90))
        self.Command_Activate_Button.setStyleSheet("/*RadioButton和checkbox字体和间距设置*/\n"
"QRadioButton ,QCheckBox{\n"
"    spacing: 5px;\n"
"    font-family: \"Calibri\";\n"
"    font-weight:bold;\n"
"    font-size:15px\n"
"}\n"
"/*checkbox样式设置*/\n"
"QCheckBox::indicator { \n"
"    width: 26px;\n"
"    height: 50px;\n"
"}\n"
"/*未选中*/\n"
"QCheckBox::indicator::unchecked {   \n"
"    image: url(./images/checkbox_unchecked.png);\n"
"}\n"
"/*选中*/\n"
"QCheckBox::indicator::checked { \n"
"    image: url(./images/checkbox_checked.png);\n"
"}")
        self.Command_Activate_Button.setObjectName("Command_Activate_Button")
        self.horizontalLayout_6.addWidget(self.Command_Activate_Button)
        self.radioButton_loop_times = QtWidgets.QRadioButton(self.Command_groupBox)
        self.radioButton_loop_times.setStyleSheet("/*RadioButton样式设置*/\n"
"QRadioButton::indicator { \n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"/*单选框未选中样式*/\n"
"QRadioButton::indicator::unchecked {\n"
"     \n"
"    image: url(./images/RadioButton_unchecked.png);\n"
"}\n"
"/*单选框选中样式*/\n"
"QRadioButton::indicator::checked { \n"
"    image: url(./images/RadioButton_checked.png);\n"
"}\n"
"/*RadioButton和checkbox字体和间距设置*/\n"
"QRadioButton ,QCheckBox{\n"
"    spacing: 5px;\n"
"    font-size: 15px;\n"
"}")
        self.radioButton_loop_times.setChecked(True)
        self.radioButton_loop_times.setObjectName("radioButton_loop_times")
        self.horizontalLayout_6.addWidget(self.radioButton_loop_times)
        self.loop_times_spinBox = QtWidgets.QSpinBox(self.Command_groupBox)
        self.loop_times_spinBox.setMinimumSize(QtCore.QSize(60, 29))
        self.loop_times_spinBox.setMaximumSize(QtCore.QSize(60, 29))
        self.loop_times_spinBox.setStyleSheet("QSpinBox\n"
"{\n"
"    border-style:none;\n"
"    padding:4px;\n"
"    border-radius:5px;\n"
"    border:2px solid #DCE4EC;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QSpinBox:focus\n"
"{\n"
"    border:2px solid #AA55AA;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    border-image: url(./images/UpArrow.png) 1;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"/*\n"
"QSpinBox::up-button:hover {\n"
"    border-image: url(:/images/spinup_hover.png) 1;\n"
"}\n"
"*/\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    border-image: url(./images/UpArrow_press.png) 1;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/images/UpArrow.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"*/\n"
"\n"
"/*\n"
"QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off { /* off state when value is max\n"
"   image: url(:/images/up_arrow_disabled.png);\n"
"}\n"
" */\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    border-image: url(./images/DownArrow.png) 1;\n"
"    border-width: 1px;\n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    border-image: url(./images/DownArrow_press.png) 1;\n"
"}\n"
"\n"
"/*\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/images/down_arrow.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"*/\n"
"\n"
"/* off state when value in min \n"
"QSpinBox::down-arrow:disabled,QSpinBox::down-arrow:off { \n"
"   image: url(:/images/down_arrow_disabled.png);\n"
"}\n"
"*/\n"
"")
        self.loop_times_spinBox.setMinimum(1)
        self.loop_times_spinBox.setMaximum(100)
        self.loop_times_spinBox.setObjectName("loop_times_spinBox")
        self.horizontalLayout_6.addWidget(self.loop_times_spinBox)
        self.radioButton_infinite = QtWidgets.QRadioButton(self.Command_groupBox)
        self.radioButton_infinite.setStyleSheet("/*RadioButton样式设置*/\n"
"QRadioButton::indicator { \n"
"    width: 17px;\n"
"    height: 17px;\n"
"}\n"
"/*单选框未选中样式*/\n"
"QRadioButton::indicator::unchecked {\n"
"     \n"
"    image: url(./images/RadioButton_unchecked.png);\n"
"}\n"
"/*单选框选中样式*/\n"
"QRadioButton::indicator::checked { \n"
"    image: url(./images/RadioButton_checked.png);\n"
"}\n"
"/*RadioButton和checkbox字体和间距设置*/\n"
"QRadioButton ,QCheckBox{\n"
"    spacing: 5px;\n"
"    font-size: 15px;\n"
"}")
        self.radioButton_infinite.setObjectName("radioButton_infinite")
        self.horizontalLayout_6.addWidget(self.radioButton_infinite)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Command_Save_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Save_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Command_Save_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Command_Save_Button.setStyleSheet("QPushButton{    \n"
"    border-image: url(./images/Save.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(./images/Save_press.png);\n"
"}\n"
"")
        self.Command_Save_Button.setText("")
        self.Command_Save_Button.setObjectName("Command_Save_Button")
        self.horizontalLayout_3.addWidget(self.Command_Save_Button)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.Command_Add_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Add_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Command_Add_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Command_Add_Button.setStyleSheet("QPushButton{    \n"
"    border-image: url(./images/add.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(./images/add_press.png);\n"
"}\n"
"")
        self.Command_Add_Button.setText("")
        self.Command_Add_Button.setObjectName("Command_Add_Button")
        self.horizontalLayout_3.addWidget(self.Command_Add_Button)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.Command_Del_Button = QtWidgets.QPushButton(self.Command_groupBox)
        self.Command_Del_Button.setMinimumSize(QtCore.QSize(25, 25))
        self.Command_Del_Button.setMaximumSize(QtCore.QSize(25, 25))
        self.Command_Del_Button.setStyleSheet("QPushButton{    \n"
"    border-image: url(./images/Del.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(./images/Del_press.png);\n"
"}\n"
"")
        self.Command_Del_Button.setText("")
        self.Command_Del_Button.setObjectName("Command_Del_Button")
        self.horizontalLayout_3.addWidget(self.Command_Del_Button)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Command_groupBox, 0, 3, 2, 1)
        self.gridLayout_5.addWidget(self.widget, 1, 0, 1, 1)
        JT_EMQ_Test_Assistant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JT_EMQ_Test_Assistant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 23))
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
        JT_EMQ_Test_Assistant.setTabOrder(self.Host_lineEdit, self.Username_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Username_lineEdit, self.Port_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Port_lineEdit, self.Password_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.Password_lineEdit, self.ClientID_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.ClientID_lineEdit, self.PublishTopic_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.PublishTopic_lineEdit, self.KeepAlive_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.KeepAlive_lineEdit, self.SubTopic_lineEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.SubTopic_lineEdit, self.Command_Send_Button)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_Send_Button, self.EMQ_Data_textEdit)
        JT_EMQ_Test_Assistant.setTabOrder(self.EMQ_Data_textEdit, self.Command_list_tableWidget)
        JT_EMQ_Test_Assistant.setTabOrder(self.Command_list_tableWidget, self.Save_Log_checkBox)
        JT_EMQ_Test_Assistant.setTabOrder(self.Save_Log_checkBox, self.Rec_Data_Clean_Button)

    def retranslateUi(self, JT_EMQ_Test_Assistant):
        _translate = QtCore.QCoreApplication.translate
        JT_EMQ_Test_Assistant.setWindowTitle(_translate("JT_EMQ_Test_Assistant", "MainWindow"))
        self.EMQ_Setting_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "EMQ Setting"))
        self.label_5.setText(_translate("JT_EMQ_Test_Assistant", "Username:"))
        self.Username_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "eie-device"))
        self.label_4.setText(_translate("JT_EMQ_Test_Assistant", "Client ID:"))
        self.ClientID_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "mqtt_test_assistant"))
        self.label_9.setText(_translate("JT_EMQ_Test_Assistant", "Publish Topic: "))
        self.PublishTopic_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "EIE/in/00000000/00000001"))
        self.label_6.setText(_translate("JT_EMQ_Test_Assistant", "Password:"))
        self.Password_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "Eie_28918499"))
        self.label_10.setText(_translate("JT_EMQ_Test_Assistant", "Subscribe Topic: "))
        self.SubTopic_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "EIE/out/00000000/00000001"))
        self.label_2.setText(_translate("JT_EMQ_Test_Assistant", "Host:"))
        self.Host_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "139.159.163.25"))
        self.label_8.setText(_translate("JT_EMQ_Test_Assistant", "Keep Alive:"))
        self.KeepAlive_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "120"))
        self.label_3.setText(_translate("JT_EMQ_Test_Assistant", "Port:"))
        self.Port_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "8083"))
        self.Check_EMQ_Button.setToolTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ"))
        self.Check_EMQ_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ accroding to setting"))
        self.Check_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "Get EMQ Topics"))
        self.Connect_EMQ_Button.setToolTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ"))
        self.Connect_EMQ_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ accroding to setting"))
        self.Connect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "Connect to EMQ"))
        self.Emq_connect_lable.setText(_translate("JT_EMQ_Test_Assistant", "Produced by PeterH"))
        self.R_S_Data_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "Receive + Send Data "))
        self.EMQ_Data_textEdit.setHtml(_translate("JT_EMQ_Test_Assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibir\'; font-size:12pt; font-weight:400;\"><br /></p></body></html>"))
        self.Save_Log_checkBox.setText(_translate("JT_EMQ_Test_Assistant", "Save log"))
        self.Save_Log_checkBox.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+R"))
        self.textEdit_Fianl_Line_Button.setText(_translate("JT_EMQ_Test_Assistant", "Final Line"))
        self.Rec_Data_Clean_Button.setText(_translate("JT_EMQ_Test_Assistant", "Clean"))
        self.Command_groupBox.setTitle(_translate("JT_EMQ_Test_Assistant", "Command List"))
        self.Command_Data_lineEdit.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Data you want to send"))
        self.Command_Data_lineEdit.setText(_translate("JT_EMQ_Test_Assistant", "Hey mate. "))
        self.Command_Send_Button.setText(_translate("JT_EMQ_Test_Assistant", "Send(&Q)"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Activate"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Delay_ms"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Name"))
        item = self.Command_list_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("JT_EMQ_Test_Assistant", "Data"))
        self.Command_Single_Send_Button.setText(_translate("JT_EMQ_Test_Assistant", "Single send"))
        self.Command_Activate_Button.setText(_translate("JT_EMQ_Test_Assistant", "Activate"))
        self.radioButton_loop_times.setText(_translate("JT_EMQ_Test_Assistant", "Times"))
        self.radioButton_infinite.setText(_translate("JT_EMQ_Test_Assistant", "Infinite"))
        self.Command_Save_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Save command list , Short cut : Ctrl + S"))
        self.Command_Save_Button.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+S"))
        self.Command_Add_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Add a command  , Short cut : Ctrl + A"))
        self.Command_Add_Button.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+A"))
        self.Command_Del_Button.setStatusTip(_translate("JT_EMQ_Test_Assistant", "Delete a command  , Short cut : Ctrl + D"))
        self.Command_Del_Button.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+D"))
        self.menuFile.setTitle(_translate("JT_EMQ_Test_Assistant", "File(&F)"))
        self.menuSetting.setTitle(_translate("JT_EMQ_Test_Assistant", "Setting(&S)"))
        self.actionImport_configuration_file.setText(_translate("JT_EMQ_Test_Assistant", "Import Configuration file"))
        self.actionEMQ.setText(_translate("JT_EMQ_Test_Assistant", "EMQ"))
        self.actionEMQ.setStatusTip(_translate("JT_EMQ_Test_Assistant", "EMQ Setting"))
        self.actionEMQ.setShortcut(_translate("JT_EMQ_Test_Assistant", "Ctrl+S"))
        self.actionConnect_EMQ_Button.setText(_translate("JT_EMQ_Test_Assistant", "actionConnect_EMQ_Button"))

