from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_RailFencePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_RailFencePanel, self).__init__()

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RailFenceDivTips = uni_Widget.ICTFELabel(self)
        self.RailFenceDivTips.setObjectName("RailFenceDivTips")
        self.horizontalLayout.addWidget(self.RailFenceDivTips)
        self.RailFenceDivBox = uni_Widget.ICTFELineBox(self)
        self.RailFenceDivBox.setObjectName("RailFenceDivBox")
        self.horizontalLayout.addWidget(self.RailFenceDivBox)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RailFenceEncryptButton = uni_Widget.ICTFEButton(self)
        self.RailFenceEncryptButton.setMinimumSize(QtCore.QSize(120, 45))
        self.RailFenceEncryptButton.setMaximumSize(QtCore.QSize(120, 45))
        self.RailFenceEncryptButton.setObjectName("RailFenceEncryptButton")
        self.horizontalLayout.addWidget(self.RailFenceEncryptButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.RailFenceTextBox = uni_Widget.ICTFETextBox(self)
        self.RailFenceTextBox.setObjectName("RailFenceTextBox")
        self.verticalLayout.addWidget(self.RailFenceTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.RailFenceDecryptButton = uni_Widget.ICTFEButton(self)
        self.RailFenceDecryptButton.setMinimumSize(QtCore.QSize(120, 45))
        self.RailFenceDecryptButton.setMaximumSize(QtCore.QSize(120, 45))
        self.RailFenceDecryptButton.setObjectName("RailFenceDecryptButton")
        self.horizontalLayout_2.addWidget(self.RailFenceDecryptButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.RailFenceCipherBox = uni_Widget.ICTFETextBox(self)
        self.RailFenceCipherBox.setObjectName("RailFenceCipherBox")
        self.verticalLayout_2.addWidget(self.RailFenceCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.RailFenceDivTips.setText(_translate("self", "组数:"))
        self.RailFenceEncryptButton.setText(_translate("self", "加密"))
        self.RailFenceDecryptButton.setText(_translate("self", "解密"))
