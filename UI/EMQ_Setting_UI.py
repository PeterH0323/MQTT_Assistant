# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EMQ_Setting_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EMQ_Setting_Dialog(object):
    def setupUi(self, EMQ_Setting_Dialog):
        EMQ_Setting_Dialog.setObjectName("EMQ_Setting_Dialog")
        EMQ_Setting_Dialog.resize(519, 624)
        self.Setting_EMQ_Buttons = QtWidgets.QDialogButtonBox(EMQ_Setting_Dialog)
        self.Setting_EMQ_Buttons.setGeometry(QtCore.QRect(180, 560, 321, 51))
        self.Setting_EMQ_Buttons.setOrientation(QtCore.Qt.Horizontal)
        self.Setting_EMQ_Buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Setting_EMQ_Buttons.setObjectName("Setting_EMQ_Buttons")
        self.label_7 = QtWidgets.QLabel(EMQ_Setting_Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 381, 21))
        self.label_7.setObjectName("label_7")
        self.splitter = QtWidgets.QSplitter(EMQ_Setting_Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 481, 451))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Host_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Host_lineEdit.setPlaceholderText("")
        self.Host_lineEdit.setObjectName("Host_lineEdit")
        self.horizontalLayout.addWidget(self.Host_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Port_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Port_lineEdit.setPlaceholderText("")
        self.Port_lineEdit.setObjectName("Port_lineEdit")
        self.horizontalLayout_2.addWidget(self.Port_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ClientID_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ClientID_lineEdit.setPlaceholderText("")
        self.ClientID_lineEdit.setObjectName("ClientID_lineEdit")
        self.horizontalLayout_3.addWidget(self.ClientID_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Username_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Username_lineEdit.setPlaceholderText("")
        self.Username_lineEdit.setObjectName("Username_lineEdit")
        self.horizontalLayout_4.addWidget(self.Username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Password_lineEdit.setPlaceholderText("")
        self.Password_lineEdit.setObjectName("Password_lineEdit")
        self.horizontalLayout_5.addWidget(self.Password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.KeepAlive_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.KeepAlive_lineEdit.setPlaceholderText("")
        self.KeepAlive_lineEdit.setObjectName("KeepAlive_lineEdit")
        self.horizontalLayout_6.addWidget(self.KeepAlive_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.PublishTopic_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.PublishTopic_lineEdit.setPlaceholderText("")
        self.PublishTopic_lineEdit.setObjectName("PublishTopic_lineEdit")
        self.horizontalLayout_8.addWidget(self.PublishTopic_lineEdit)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.SubTopic_lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.SubTopic_lineEdit.setPlaceholderText("")
        self.SubTopic_lineEdit.setObjectName("SubTopic_lineEdit")
        self.horizontalLayout_7.addWidget(self.SubTopic_lineEdit)
        self.splitter.raise_()
        self.Setting_EMQ_Buttons.raise_()
        self.label_7.raise_()

        self.retranslateUi(EMQ_Setting_Dialog)
        self.Setting_EMQ_Buttons.accepted.connect(EMQ_Setting_Dialog.accept)
        self.Setting_EMQ_Buttons.rejected.connect(EMQ_Setting_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EMQ_Setting_Dialog)

    def retranslateUi(self, EMQ_Setting_Dialog):
        _translate = QtCore.QCoreApplication.translate
        EMQ_Setting_Dialog.setWindowTitle(_translate("EMQ_Setting_Dialog", "Dialog"))
        self.label_7.setText(_translate("EMQ_Setting_Dialog", "EMQ Setting"))
        self.label.setText(_translate("EMQ_Setting_Dialog", "Host:"))
        self.Host_lineEdit.setText(_translate("EMQ_Setting_Dialog", "139.159.163.25"))
        self.label_2.setText(_translate("EMQ_Setting_Dialog", "Port:"))
        self.Port_lineEdit.setText(_translate("EMQ_Setting_Dialog", "8083"))
        self.label_3.setText(_translate("EMQ_Setting_Dialog", "Client ID:"))
        self.ClientID_lineEdit.setText(_translate("EMQ_Setting_Dialog", "mqtt_test_assistant"))
        self.label_4.setText(_translate("EMQ_Setting_Dialog", "Username:"))
        self.Username_lineEdit.setText(_translate("EMQ_Setting_Dialog", "eie-device"))
        self.label_5.setText(_translate("EMQ_Setting_Dialog", "Password:"))
        self.Password_lineEdit.setText(_translate("EMQ_Setting_Dialog", "Eie_28918499"))
        self.label_6.setText(_translate("EMQ_Setting_Dialog", "Keep Alive:"))
        self.KeepAlive_lineEdit.setText(_translate("EMQ_Setting_Dialog", "60"))
        self.label_9.setText(_translate("EMQ_Setting_Dialog", "Publish Topic: "))
        self.PublishTopic_lineEdit.setText(_translate("EMQ_Setting_Dialog", "EIE/out/00000000/00000001"))
        self.label_8.setText(_translate("EMQ_Setting_Dialog", "Subscribe Topic: "))
        self.SubTopic_lineEdit.setText(_translate("EMQ_Setting_Dialog", "EIE/in/00000000/00000001"))
