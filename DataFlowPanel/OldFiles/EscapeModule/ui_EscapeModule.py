from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_EscapePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_EscapePanel, self).__init__()
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.EscapeEncodeButton = uni_Widget.ICTFEButton(self)
        self.EscapeEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.EscapeEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.EscapeEncodeButton.setObjectName("EscapeEncodeButton")
        self.horizontalLayout.addWidget(self.EscapeEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.EscapeTextBox = uni_Widget.ICTFETextBox(self)
        self.EscapeTextBox.setObjectName("EscapeTextBox")
        self.verticalLayout.addWidget(self.EscapeTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.EscapeDecodeButton = uni_Widget.ICTFEButton(self)
        self.EscapeDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.EscapeDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.EscapeDecodeButton.setObjectName("EscapeDecodeButton")
        self.horizontalLayout_2.addWidget(self.EscapeDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.EscapeCipherBox = uni_Widget.ICTFETextBox(self)
        self.EscapeCipherBox.setObjectName("EscapeCipherBox")
        self.verticalLayout_2.addWidget(self.EscapeCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.EscapeEncodeButton.setText(_translate("self", "编码"))
        self.EscapeDecodeButton.setText(_translate("self", "解码"))
