from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_StrokesPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_StrokesPanel, self).__init__()

        # Strokes Decrypt button
        self.StrokesDecryptButton = uni_Widget.ICTFEButton(self)
        self.StrokesDecryptButton.setObjectName('StrokesDecryptButton')
        self.StrokesDecryptButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.StrokesDecryptButton.setText('解密')

        self.StrokesTextBox = uni_Widget.ICTFETextBox(self)
        self.StrokesTextBox.setObjectName('StrokesTextBox')
        self.StrokesTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.StrokesTextBox.setPlaceholderText('Strokes Encrypt\n这里写明文')

        self.StrokesCipherBox = uni_Widget.ICTFETextBox(self)
        self.StrokesCipherBox.setObjectName('StrokesCipherBox')
        self.StrokesCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.StrokesCipherBox.setPlaceholderText('Strokes Decrypt\n这里写编码')
        # end Strokes panel