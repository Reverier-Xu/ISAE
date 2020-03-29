from Crypto.UrlModule import ui_UrlModule
from urllib import parse
from PyQt5 import QtWidgets


class UrlPanel(ui_UrlModule.ui_UrlPanel):
    def __init__(self):
        super(UrlPanel, self).__init__()
        self.UrlEncodeButton.clicked.connect(self.UrlEncode)
        self.UrlDecodeButton.clicked.connect(self.UrlDecode)

    def UrlEncode(self):
        text = self.UrlTextBox.toPlainText()
        try:
            self.UrlCipherBox.setText(
                parse.quote(text, encoding=self.UrlTableBox.text()))
        except:
            self.UrlCipherBox.setText('出现错误!')

    def UrlDecode(self):
        text = self.UrlCipherBox.toPlainText()
        try:
            self.UrlTextBox.setText(parse.unquote(
                text, encoding=self.UrlTableBox.text()))
        except:
            self.UrlTextBox.setText('出现错误!')
