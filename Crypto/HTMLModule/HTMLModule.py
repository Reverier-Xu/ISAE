from Crypto.HTMLModule.ui_HTMLModule import ui_HTMLPanel
import html


class HTMLPanel(ui_HTMLPanel):
    def __init__(self):
        super(HTMLPanel, self).__init__()

        self.HTMLEncodeButton.clicked.connect(self.HTMLEncode)
        self.HTMLDecodeButton.clicked.connect(self.HTMLDecode)

    def HTMLEncode(self):
        text = self.HTMLTextBox.toPlainText()
        try:
            output = html.escape(text)
            self.HTMLCipherBox.setText(output)
        except:
            self.HTMLCipherBox.setText('编码时出现错误!')

    def HTMLDecode(self):
        text = self.HTMLCipherBox.toPlainText()
        try:
            output = html.unescape(text)
            self.HTMLTextBox.setText(output)
        except:
            self.HTMLTextBox.setText('解码时出现错误!')
