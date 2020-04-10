from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_StrokesPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_StrokesPanel, self).__init__()

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.StrokesDecryptButton = uni_Widget.ICTFEButton(self)
        self.StrokesDecryptButton.setMinimumSize(QtCore.QSize(120, 45))
        self.StrokesDecryptButton.setMaximumSize(QtCore.QSize(120, 45))
        self.StrokesDecryptButton.setObjectName("StrokesDecryptButton")
        self.horizontalLayout.addWidget(self.StrokesDecryptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.StrokesTextBox = uni_Widget.ICTFETextBox(self)
        self.StrokesTextBox.setObjectName("StrokesTextBox")
        self.gridLayout.addWidget(self.StrokesTextBox, 1, 0, 1, 1)
        self.StrokesCipherBox = uni_Widget.ICTFETextBox(self)
        self.StrokesCipherBox.setObjectName("StrokesCipherBox")
        self.gridLayout.addWidget(self.StrokesCipherBox, 1, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.StrokesDecryptButton.setText(_translate("self", "计算!"))