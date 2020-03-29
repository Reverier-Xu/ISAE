from Crypto.EscapeModule.ui_EscapeModule import ui_EscapePanel
from urllib import parse


class EscapePanel(ui_EscapePanel):
    def __init__(self):
        super(EscapePanel, self).__init__()
        self.EscapeEncodeButton.clicked.connect(self.EscapeEncode)
        self.EscapeDecodeButton.clicked.connect(self.EscapeDecode)

    def EscapeEncode(self):
        try:
            self.EscapeCipherBox.setText(parse.quote(self.EscapeTextBox.toPlainText().encode(
                'unicode-escape')).replace('%5Cu', '%u'))
        except:
            self.EscapeCipherBox.setText('编码失败.')

    def EscapeDecode(self):
        try:
            self.EscapeTextBox.setText(
                parse.unquote(
                    self.EscapeCipherBox.toPlainText().replace('%u', '\\u').encode().decode('unicode-escape')))
        except:
            self.EscapeTextBox.setText('解码失败.')
