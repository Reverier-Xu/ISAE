from ui_Widgets import uni_Widget
from PyQt5 import QtGui, QtCore, QtWidgets


class ui_ROTPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_ROTPanel, self).__init__()
        self.ROTMode = 1

        # ROT Change Button
        self.ROT13Button = uni_Widget.ICTFEButton(self)
        self.ROT13Button.setObjectName('ROT13Button')
        self.ROT13Button.setGeometry(QtCore.QRect(20, 20, 120, 45))
        self.ROT13Button.setText('ROT13')

        self.ROT47Button = uni_Widget.ICTFEButton(self)
        self.ROT47Button.setObjectName('ROT47Button')
        self.ROT47Button.setGeometry(QtCore.QRect(150, 20, 120, 45))
        self.ROT47Button.setText('ROT47')

        self.ROTChooserBox = [0, 20, 150]
        self.ROTChooser = QtWidgets.QLabel(self)
        self.ROTChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.ROTChooser.setGeometry(QtCore.QRect(
            self.ROTChooserBox[self.ROTMode], 65, 120, 8))

        # ROT Encode button
        self.ROTEncodeButton = uni_Widget.ICTFEButton(self)
        self.ROTEncodeButton.setObjectName('ROTEncodeButton')
        self.ROTEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.ROTEncodeButton.setText('计算')

        self.ROTTextBox = uni_Widget.ICTFETextBox(self)
        self.ROTTextBox.setObjectName('ROTTextBox')
        self.ROTTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.ROTTextBox.setPlaceholderText('ROT Encode\n这里输入')

        self.ROTCipherBox = uni_Widget.ICTFETextBox(self)
        self.ROTCipherBox.setObjectName('ROTCipherBox')
        self.ROTCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.ROTCipherBox.setPlaceholderText('ROT Decode\n这里输出')
        # end ROT panel

