from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_HTMLPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HTMLPanel, self).__init__()

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
        self.HTMLEncodeButton = uni_Widget.ICTFEButton(self)
        self.HTMLEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HTMLEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HTMLEncodeButton.setObjectName("HTMLEncodeButton")
        self.horizontalLayout.addWidget(self.HTMLEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.HTMLTextBox = uni_Widget.ICTFETextBox(self)
        self.HTMLTextBox.setObjectName("HTMLTextBox")
        self.verticalLayout.addWidget(self.HTMLTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.HTMLDecodeButton = uni_Widget.ICTFEButton(self)
        self.HTMLDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.HTMLDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.HTMLDecodeButton.setObjectName("HTMLDecodeButton")
        self.horizontalLayout_2.addWidget(self.HTMLDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.HTMLCipherBox = uni_Widget.ICTFETextBox(self)
        self.HTMLCipherBox.setObjectName("HTMLCipherBox")
        self.verticalLayout_2.addWidget(self.HTMLCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.HTMLEncodeButton.setText(_translate("self", "编码"))
        self.HTMLDecodeButton.setText(_translate("self", "解码"))
