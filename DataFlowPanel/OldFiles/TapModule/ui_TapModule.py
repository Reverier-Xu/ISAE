from PyQt5 import QtWidgets, QtCore, QtGui
from ui_Widgets import uni_Widget


class ui_TapPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_TapPanel, self).__init__()

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.TapEncodeButton = uni_Widget.ICTFEButton(self)
        self.TapEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.TapEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.TapEncodeButton.setObjectName("TapEncodeButton")
        self.horizontalLayout.addWidget(self.TapEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.TapTextBox = uni_Widget.ICTFETextBox(self)
        self.TapTextBox.setObjectName("TapTextBox")
        self.verticalLayout.addWidget(self.TapTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.TapDecodeButton = uni_Widget.ICTFEButton(self)
        self.TapDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.TapDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.TapDecodeButton.setObjectName("TapDecodeButton")
        self.horizontalLayout_2.addWidget(self.TapDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.TapCipherBox = uni_Widget.ICTFETextBox(self)
        self.TapCipherBox.setObjectName("TapCipherBox")
        self.verticalLayout_2.addWidget(self.TapCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.TapEncodeButton.setText(_translate("self", "编码"))
        self.TapDecodeButton.setText(_translate("self", "解码"))
        # end Tap panel
