# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Master.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(421, 499)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(421, 499))
        Form.setMaximumSize(QtCore.QSize(421, 499))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Tab2 = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab2.sizePolicy().hasHeightForWidth())
        self.Tab2.setSizePolicy(sizePolicy)
        self.Tab2.setMinimumSize(QtCore.QSize(0, 0))
        self.Tab2.setMaximumSize(QtCore.QSize(9999, 99999))
        self.Tab2.setObjectName("Tab2")
        self.tab_hosts = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_hosts.sizePolicy().hasHeightForWidth())
        self.tab_hosts.setSizePolicy(sizePolicy)
        self.tab_hosts.setObjectName("tab_hosts")
        self.comboBox = QtWidgets.QComboBox(self.tab_hosts)
        self.comboBox.setGeometry(QtCore.QRect(70, 9, 46, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lable_netmask = QtWidgets.QLabel(self.tab_hosts)
        self.lable_netmask.setGeometry(QtCore.QRect(9, 9, 57, 25))
        self.lable_netmask.setObjectName("lable_netmask")
        self.pushButton = QtWidgets.QPushButton(self.tab_hosts)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_hosts)
        self.splitter_2.setGeometry(QtCore.QRect(10, 60, 197, 25))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_network = QtWidgets.QLabel(self.splitter_2)
        self.label_network.setObjectName("label_network")
        self.line_network = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_network.sizePolicy().hasHeightForWidth())
        self.line_network.setSizePolicy(sizePolicy)
        self.line_network.setObjectName("line_network")
        self.listWidget = QtWidgets.QListWidget(self.tab_hosts)
        self.listWidget.setGeometry(QtCore.QRect(90, 90, 221, 351))
        self.listWidget.setObjectName("listWidget")
        self.progressBar = QtWidgets.QProgressBar(self.tab_hosts)
        self.progressBar.setGeometry(QtCore.QRect(250, 60, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.Tab2.addTab(self.tab_hosts, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 171, 201))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(230, 0, 171, 201))
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 40, 41, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 110, 41, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_4.setGeometry(QtCore.QRect(230, 240, 171, 211))
        self.listWidget_4.setObjectName("listWidget_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 380, 83, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setGeometry(QtCore.QRect(20, 221, 142, 126))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Tab2.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.Tab2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.Tab2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Abu-Trika"))
        Form.setToolTip(_translate("Form", "Abu-Trika"))
        self.comboBox.setItemText(0, _translate("Form", "24"))
        self.comboBox.setItemText(1, _translate("Form", "16"))
        self.comboBox.setItemText(2, _translate("Form", "8"))
        self.lable_netmask.setText(_translate("Form", "netmask "))
        self.pushButton.setText(_translate("Form", "Scan "))
        self.label_network.setText(_translate("Form", "Network"))
        self.line_network.setPlaceholderText(_translate("Form", "192.168.1.1"))
        self.Tab2.setTabText(self.Tab2.indexOf(self.tab_hosts), _translate("Form", "Hosts"))
        self.pushButton_2.setText(_translate("Form", ">>"))
        self.pushButton_3.setText(_translate("Form", "<<"))
        self.pushButton_4.setText(_translate("Form", "Auth"))
        self.label.setText(_translate("Form", "username :"))
        self.lineEdit.setPlaceholderText(_translate("Form", "root"))
        self.label_2.setText(_translate("Form", "password :"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "password"))
        self.label_3.setText(_translate("Form", "password again :"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "password"))
        self.Tab2.setTabText(self.Tab2.indexOf(self.tab_2), _translate("Form", "auth"))

