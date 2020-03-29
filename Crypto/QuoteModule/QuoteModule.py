from Crypto.QuoteModule import ui_QuoteModule
from PyQt5 import QtWidgets, QtGui
import quopri


class QuotePanel(ui_QuoteModule.ui_QuotePanel):
    def __init__(self):
        super(QuotePanel, self).__init__()
        self.QuoteEncodeButton.clicked.connect(self.QuoteEnc)
        self.QuoteDecodeButton.clicked.connect(self.QuoteDec)
        self.QuoteTextInputButton.clicked.connect(self.QuoteTextInputFunction)
        self.QuoteCipherInputButton.clicked.connect(
            self.QuoteCipherInputFunction)
        self.QuoteTextOutputButton.clicked.connect(
            self.QuoteTextOutputFunction)
        self.QuoteCipherOutputButton.clicked.connect(
            self.QuoteCipherOutputFunction)
        self.QuoteCipherBox.textChanged.connect(self.setFontColorCipher)
        self.QuoteTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.QuoteCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.QuoteTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def QuoteEnc(self):
        if self.QuoteTextEvalCheckBox.isChecked():
            try:
                text = eval(self.QuoteTextBox.toPlainText())
            except:
                self.QuoteCipherBox.setText(
                    '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
                return
        else:
            text = self.QuoteTextBox.toPlainText().encode()
        try:
            cipher = quopri.encodestring(text).decode()
        except:
            cipher = '编码时出现错误!'
        self.QuoteCipherBox.setText(cipher)

    def QuoteDec(self):
        text = self.QuoteCipherBox.toPlainText()
        try:
            cipher = quopri.decodestring(text)
        except:
            self.QuoteTextBox.setText('解码时出现错误!')
            return
        try:
            self.QuoteTextBox.setText(cipher.decode())
        except:
            self.QuoteTextBox.setText(str(cipher))

    def QuoteTextInputFunction(self):
        self.QuoteTextInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.QuoteTextInputPath == "":
            return
        with open(self.QuoteTextInputPath, 'rb') as inp:
            self.QuoteTextBox.setText(str(inp.read()))
        self.QuoteTextEvalCheckBox.setChecked(True)

    def QuoteTextOutputFunction(self):
        self.QuoteTextOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                   "保存文件",
                                                                                   '',
                                                                                   "All Files (*)")
        if self.QuoteTextOutputPath == "":
            return
        if self.QuoteTextBox.toPlainText()[0:2] == 'b\'':
            with open(self.QuoteTextOutputPath, 'wb') as out:
                out.write(eval(self.QuoteTextBox.toPlainText()))
        else:
            with open(self.QuoteTextOutputPath, 'w') as out:
                out.write(self.QuoteTextBox.toPlainText())

    def QuoteCipherOutputFunction(self):
        self.QuoteCipherOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                     "保存文件",
                                                                                     '',
                                                                                     "All Files (*)")
        if self.QuoteCipherOutputPath == "":
            return
        with open(self.QuoteCipherOutputPath, 'w') as out:
            out.write(self.QuoteCipherBox.toPlainText())

    def QuoteCipherInputFunction(self):
        self.QuoteCipherInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.QuoteCipherInputPath == "":
            return
        with open(self.QuoteCipherInputPath, 'r') as inp:
            try:
                self.QuoteCipherBox.setText(inp.read())
            except:
                self.QuoteCipherBox.setText('文件读取错误.')

