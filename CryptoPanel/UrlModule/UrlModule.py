from CryptoPanel.UrlModule import ui_UrlModule
from urllib import parse
from PyQt5 import QtGui
from ui_Widgets.ErrorWin import errorInfo


class UrlPanel(ui_UrlModule.ui_UrlPanel):
    def __init__(self):
        super(UrlPanel, self).__init__()
        self.UrlEncodeButton.clicked.connect(self.UrlEncode)
        self.UrlDecodeButton.clicked.connect(self.UrlDecode)
        self.UrlCipherBox.textChanged.connect(self.setFontColorCipher)
        self.UrlTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.UrlCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.UrlTextBox.setTextColor(QtGui.QColor(200, 200, 200))
    def UrlEncode(self):
        text = self.UrlTextBox.toPlainText()
        try:
            self.UrlCipherBox.setText(
                parse.quote(text, encoding=self.UrlTableBox.text()))
        except:
            errorInfo(self, '出现错误!')

    def UrlDecode(self):
        text = self.UrlCipherBox.toPlainText()
        try:
            self.UrlTextBox.setText(parse.unquote(
                text, encoding=self.UrlTableBox.text()))
        except:
            errorInfo(self, '出现错误!')
