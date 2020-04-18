from ui_Widgets import uni_Widget
from PyQt5 import QtGui, QtCore, QtWidgets


class ui_ROTPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_ROTPanel, self).__init__()
        self.ROTMode = 1

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ROT13Button = uni_Widget.ICTFEButton(self)
        self.ROT13Button.setMinimumSize(QtCore.QSize(120, 45))
        self.ROT13Button.setMaximumSize(QtCore.QSize(120, 45))
        self.ROT13Button.setObjectName("ROT13Button")
        self.horizontalLayout.addWidget(self.ROT13Button)
        self.ROT47Button = uni_Widget.ICTFEButton(self)
        self.ROT47Button.setMinimumSize(QtCore.QSize(120, 45))
        self.ROT47Button.setMaximumSize(QtCore.QSize(120, 45))
        self.ROT47Button.setObjectName("ROT47Button")
        self.horizontalLayout.addWidget(self.ROT47Button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ROTEncodeButton = uni_Widget.ICTFEButton(self)
        self.ROTEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.ROTEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.ROTEncodeButton.setObjectName("ROTEncodeButton")
        self.horizontalLayout.addWidget(self.ROTEncodeButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.ROTTextBox = uni_Widget.ICTFETextBox(self)
        self.ROTTextBox.setObjectName("ROTTextBox")
        self.gridLayout.addWidget(self.ROTTextBox, 1, 0, 1, 1)
        self.ROTCipherBox = uni_Widget.ICTFETextBox(self)
        self.ROTCipherBox.setObjectName("ROTCipherBox")
        self.gridLayout.addWidget(self.ROTCipherBox, 1, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.ROT13Button.setText(_translate("self", "ROT13"))
        self.ROT47Button.setText(_translate("self", "ROT47"))
        self.ROTEncodeButton.setText(_translate("self", "计算!"))
