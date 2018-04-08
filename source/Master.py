# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Master.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from source.codes import code101

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
        self.Tabs = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
        self.Tabs.setSizePolicy(sizePolicy)
        self.Tabs.setMinimumSize(QtCore.QSize(0, 0))
        self.Tabs.setMaximumSize(QtCore.QSize(9999, 99999))
        self.Tabs.setObjectName("Tabs")
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
        self.line_network.setObjectName("line_network")
        self.listWidget = QtWidgets.QListWidget(self.tab_hosts)
        self.listWidget.setGeometry(QtCore.QRect(0, 100, 401, 351))
        self.listWidget.setObjectName("listWidget")
        self.Tabs.addTab(self.tab_hosts, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Tabs.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Abu-Trika"))
        Form.setToolTip(_translate("Form", "Abu-Trika"))
        self.comboBox.setItemText(0, _translate("Form", "8"))
        self.comboBox.setItemText(1, _translate("Form", "16"))
        self.comboBox.setItemText(2, _translate("Form", "24"))
        self.lable_netmask.setText(_translate("Form", "netmask "))
        self.pushButton.setText(_translate("Form", "Scan "))
        self.label_network.setText(_translate("Form", "Network"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_hosts), _translate("Form", "Hosts"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), _translate("Form", "Tab 2"))

