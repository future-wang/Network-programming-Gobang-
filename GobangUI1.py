# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gobang.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1063, 768)
        # Form.setMouseTracking(True)
        # Form.setTabletTracking(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 281, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridGroupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textPort = QtWidgets.QLineEdit(self.gridGroupBox)
        self.textPort.setObjectName("textPort")
        self.gridLayout.addWidget(self.textPort, 1, 1, 1, 1)
        self.textIP = QtWidgets.QLineEdit(self.gridGroupBox)
        self.textIP.setObjectName("textIP")
        self.gridLayout.addWidget(self.textIP, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridGroupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.butConnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.butConnect.setObjectName("butConnect")
        self.horizontalLayout_2.addWidget(self.butConnect)
        self.butDisconnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.butDisconnect.setObjectName("butDisconnect")
        self.horizontalLayout_2.addWidget(self.butDisconnect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(300, 10, 750, 750))
        self.frame.setMinimumSize(QtCore.QSize(750, 750))
        self.frame.setMaximumSize(QtCore.QSize(750, 750))
        self.frame.setMouseTracking(True)
        # self.frame.setTabletTracking(True)
        self.frame.setStyleSheet("background-image: url(:/src/Img/gobang.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "端口:"))
        self.label_2.setText(_translate("Form", "地址："))
        self.butConnect.setText(_translate("Form", "连接"))
        self.butDisconnect.setText(_translate("Form", "断开"))
import srcImg_rc