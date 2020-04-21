from DataFlowPanel.EscapeModule.ui_EscapeModule import ui_EscapePanel
from urllib import parse
from PyQt5 import QtGui
from ui_Widgets.ErrorWin import errorInfo


class EscapePanel(ui_EscapePanel):
    def __init__(self):
        super(EscapePanel, self).__init__()
        self.EscapeEncodeButton.clicked.connect(self.EscapeEncode)
        self.EscapeDecodeButton.clicked.connect(self.EscapeDecode)
        self.EscapeCipherBox.textChanged.connect(self.setFontColorCipher)
        self.EscapeTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.EscapeCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.EscapeTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def EscapeEncode(self):
        try:
            self.EscapeCipherBox.setText(parse.quote(self.EscapeTextBox.toPlainText().encode(
                'unicode-escape')).replace('%5Cu', '%u'))
        except:
            errorInfo(self, '编码失败.')

    def EscapeDecode(self):
        try:
            self.EscapeTextBox.setText(
                parse.unquote(
                    self.EscapeCipherBox.toPlainText().replace('%u', '\\u').encode().decode('unicode-escape')))
        except:
            errorInfo(self, '解码失败.')
