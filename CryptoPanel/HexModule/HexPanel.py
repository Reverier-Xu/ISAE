# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HexPanel.ui'
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
        self.HexSplitTips = QtWidgets.QLabel(Form)
        self.HexSplitTips.setObjectName("HexSplitTips")
        self.horizontalLayout.addWidget(self.HexSplitTips)
        self.HexSplitBox = QtWidgets.QLineEdit(Form)
        self.HexSplitBox.setObjectName("HexSplitBox")
        self.horizontalLayout.addWidget(self.HexSplitBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.HexEncodeButton = QtWidgets.QPushButton(Form)
        self.HexEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HexEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HexEncodeButton.setObjectName("HexEncodeButton")
        self.horizontalLayout.addWidget(self.HexEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.HexTextBox = QtWidgets.QTextEdit(Form)
        self.HexTextBox.setObjectName("HexTextBox")
        self.verticalLayout.addWidget(self.HexTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.HexDecodeButton = QtWidgets.QPushButton(Form)
        self.HexDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HexDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HexDecodeButton.setObjectName("HexDecodeButton")
        self.horizontalLayout_2.addWidget(self.HexDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.HexCipherBox = QtWidgets.QTextEdit(Form)
        self.HexCipherBox.setObjectName("HexCipherBox")
        self.verticalLayout_2.addWidget(self.HexCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.HexSplitTips.setText(_translate("Form", "TextLabel"))
        self.HexEncodeButton.setText(_translate("Form", "PushButton"))
        self.HexDecodeButton.setText(_translate("Form", "PushButton"))
