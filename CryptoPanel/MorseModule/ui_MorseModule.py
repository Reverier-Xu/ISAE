from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_MorsePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_MorsePanel, self).__init__()

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MorseSpiltTips = uni_Widget.ICTFELabel(self)
        self.MorseSpiltTips.setObjectName("MorseSpiltTips")
        self.horizontalLayout.addWidget(self.MorseSpiltTips)
        self.MorseSpiltBox = uni_Widget.ICTFELineBox(self)
        self.MorseSpiltBox.setObjectName("MorseSpiltBox")
        self.horizontalLayout.addWidget(self.MorseSpiltBox)
        self.MorseChineseCheckBox = uni_Widget.ICTFECheckBox(self)
        self.MorseChineseCheckBox.setMinimumSize(QtCore.QSize(120, 45))
        self.MorseChineseCheckBox.setMaximumSize(QtCore.QSize(120, 45))
        self.MorseChineseCheckBox.setObjectName("MorseChineseCheckBox")
        self.horizontalLayout.addWidget(self.MorseChineseCheckBox)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.MorseEncodeButton = uni_Widget.ICTFEButton(self)
        self.MorseEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.MorseEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.MorseEncodeButton.setObjectName("MorseEncodeButton")
        self.horizontalLayout.addWidget(self.MorseEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MorseTextBox = uni_Widget.ICTFETextBox(self)
        self.MorseTextBox.setObjectName("MorseTextBox")
        self.verticalLayout.addWidget(self.MorseTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.MorseDecodeButton = uni_Widget.ICTFEButton(self)
        self.MorseDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.MorseDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.MorseDecodeButton.setObjectName("MorseDecodeButton")
        self.horizontalLayout_2.addWidget(self.MorseDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.MorseCipherBox = uni_Widget.ICTFETextBox(self)
        self.MorseCipherBox.setObjectName("MorseCipherBox")
        self.verticalLayout_2.addWidget(self.MorseCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MorseSpiltTips.setText(_translate("self", "分隔符:"))
        self.MorseChineseCheckBox.setText(_translate("self", "中文"))
        self.MorseEncodeButton.setText(_translate("self", "编码"))
        self.MorseDecodeButton.setText(_translate("self", "解码"))
