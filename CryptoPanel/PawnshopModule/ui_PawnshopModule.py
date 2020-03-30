from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_PawnshopPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_PawnshopPanel, self).__init__()

        # Pawnshop Decrypt button
        self.PawnshopDecryptButton = uni_Widget.ICTFEButton(self)
        self.PawnshopDecryptButton.setObjectName('PawnshopDecryptButton')
        self.PawnshopDecryptButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.PawnshopDecryptButton.setText('解密')

        self.PawnshopTextBox = uni_Widget.ICTFETextBox(self)
        self.PawnshopTextBox.setObjectName('PawnshopTextBox')
        self.PawnshopTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.PawnshopTextBox.setPlaceholderText('Pawnshop Encrypt\n这里写明文')

        self.PawnshopCipherBox = uni_Widget.ICTFETextBox(self)
        self.PawnshopCipherBox.setObjectName('PawnshopCipherBox')
        self.PawnshopCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.PawnshopCipherBox.setPlaceholderText('Pawnshop Decrypt\n这里写编码')
        # end Pawnshop panel