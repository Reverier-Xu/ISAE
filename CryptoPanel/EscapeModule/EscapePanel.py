# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EscapePanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1085, 657)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.EscapeEncodeButton = QtWidgets.QPushButton(Form)
        self.EscapeEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.EscapeEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.EscapeEncodeButton.setObjectName("EscapeEncodeButton")
        self.horizontalLayout.addWidget(self.EscapeEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.EscapeTextBox = QtWidgets.QTextEdit(Form)
        self.EscapeTextBox.setObjectName("EscapeTextBox")
        self.verticalLayout.addWidget(self.EscapeTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.EscapeDecodeButton = QtWidgets.QPushButton(Form)
        self.EscapeDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.EscapeDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.EscapeDecodeButton.setObjectName("EscapeDecodeButton")
        self.horizontalLayout_2.addWidget(self.EscapeDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.EscapeCipherBox = QtWidgets.QTextEdit(Form)
        self.EscapeCipherBox.setObjectName("EscapeCipherBox")
        self.verticalLayout_2.addWidget(self.EscapeCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.EscapeEncodeButton.setText(_translate("Form", "编码"))
        self.EscapeDecodeButton.setText(_translate("Form", "解码"))
