from CryptoPanel.HexModule.ui_HexModule import ui_HexPanel
from CryptoPanel.HexModule.HexModuleUtils import *
from PyQt5 import QtGui


class HexPanel(ui_HexPanel):
    def __init__(self):
        super(HexPanel, self).__init__()
        self.HexEncodeButton.clicked.connect(self.HexEncode)
        self.HexDecodeButton.clicked.connect(self.HexDecode)
        self.HexCipherBox.textChanged.connect(self.setFontColorCipher)
        self.HexTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.HexCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.HexTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def HexEncode(self):
        text = self.HexTextBox.toPlainText()
        try:
            temp = char2hex(text).decode()
            j = 0
            output = ''
            for i in temp:
                if j % 2 == 0:
                    output += self.HexSplitBox.text()
                output += i
                j += 1
            self.HexCipherBox.setText(output)
        except:
            self.HexCipherBox.setText('编码时出现错误!')

    def HexDecode(self):
        text = self.HexCipherBox.toPlainText()
        try:
            temp = []
            if self.HexSplitBox.text() != '':
                temp = text.split(self.HexSplitBox.text())
            else:
                temp = text.split()
            output = ''.join(temp)
            self.HexTextBox.setText(hex2char(output).decode())
        except:
            self.HexTextBox.setText('解码时出现错误!')
