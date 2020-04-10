# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ROTPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1177, 681)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ROT13Button = QtWidgets.QPushButton(Form)
        self.ROT13Button.setMinimumSize(QtCore.QSize(120, 45))
        self.ROT13Button.setMaximumSize(QtCore.QSize(120, 45))
        self.ROT13Button.setObjectName("ROT13Button")
        self.horizontalLayout.addWidget(self.ROT13Button)
        self.ROT47Button = QtWidgets.QPushButton(Form)
        self.ROT47Button.setMinimumSize(QtCore.QSize(120, 45))
        self.ROT47Button.setMaximumSize(QtCore.QSize(120, 45))
        self.ROT47Button.setObjectName("ROT47Button")
        self.horizontalLayout.addWidget(self.ROT47Button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ROTEncodeButton = QtWidgets.QPushButton(Form)
        self.ROTEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.ROTEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.ROTEncodeButton.setObjectName("ROTEncodeButton")
        self.horizontalLayout.addWidget(self.ROTEncodeButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.ROTTextBox = QtWidgets.QTextEdit(Form)
        self.ROTTextBox.setObjectName("ROTTextBox")
        self.gridLayout.addWidget(self.ROTTextBox, 1, 0, 1, 1)
        self.ROTCipherBox = QtWidgets.QTextEdit(Form)
        self.ROTCipherBox.setObjectName("ROTCipherBox")
        self.gridLayout.addWidget(self.ROTCipherBox, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ROT13Button.setText(_translate("Form", "ROT13"))
        self.ROT47Button.setText(_translate("Form", "ROT47"))
        self.ROTEncodeButton.setText(_translate("Form", "计算!"))
