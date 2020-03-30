from CryptoPanel.BaseModule.ui_BaseModule import ui_BasePanel
from CryptoPanel.BaseModule.BaseModuleUtils import *
from PyQt5 import QtCore, QtWidgets, Qt, QtGui
from ui_Widgets.ErrorWin import errorInfo


class BasePanel(ui_BasePanel):
    def __init__(self):
        super(BasePanel, self).__init__()
        self.Base16Button.clicked.connect(self.ChangeBase16)
        self.Base32Button.clicked.connect(self.ChangeBase32)
        self.Base64Button.clicked.connect(self.ChangeBase64)
        self.Base85Button.clicked.connect(self.ChangeBase85)
        self.Base85RFCButton.clicked.connect(self.ChangeBase85RFC)
        self.BaseEncButton.clicked.connect(self.BaseEnc)
        self.BaseDecButton.clicked.connect(self.BaseDec)
        self.BaseTextInputButton.clicked.connect(self.BaseTextInputFunction)
        self.BaseCipherInputButton.clicked.connect(
            self.BaseCipherInputFunction)
        self.BaseTextOutputButton.clicked.connect(self.BaseTextOutputFunction)
        self.BaseCipherOutputButton.clicked.connect(
            self.BaseCipherOutputFunction)
        self.BaseEButton.clicked.connect(self.BaseEDecodeFunction)
        self.BaseTranslateButton.clicked.connect(self.BaseTranslateFunction)
        self.BaseCipherBox.textChanged.connect(self.setFontColorCipher)
        self.BaseTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.BaseCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.BaseTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def BaseEDecodeFunction(self):
        text = self.BaseCipherBox.toPlainText()
        lines = text.splitlines()
        aim = base64_ste(lines)
        self.BaseTextBox.setText(aim)

    def BaseTranslateFunction(self):
        text = self.BaseCipherBox.toPlainText()
        self.BaseCipherBox.setText(self.BaseTextBox.toPlainText())
        self.BaseTextBox.setText(text)

    def BaseTextInputFunction(self):
        self.BaseTextInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.BaseTextInputPath == '':
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked():
            self.BaseTextBox.setText('Opened: ' + self.BaseTextInputPath +
                                     '\n由于你选中了大文件, 文本框不会将其加载.')
            self.BaseTextEvalCheckBox.setChecked(True)
            return
        with open(self.BaseTextInputPath, 'rb') as inp:
            self.BaseTextBox.setText(str(inp.read()))
        self.BaseTextEvalCheckBox.setChecked(True)

    def BaseTextOutputFunction(self):
        self.BaseTextOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                  "保存文件",
                                                                                  '',
                                                                                  "All Files (*)")
        if self.BaseTextOutputPath == "":
            return
        if self.BaseTextBox.toPlainText()[0:2] == 'b\'':
            with open(self.BaseTextOutputPath, 'wb') as out:
                out.write(eval(self.BaseTextBox.toPlainText()))
        else:
            with open(self.BaseTextOutputPath, 'w') as out:
                out.write(self.BaseTextBox.toPlainText())

    def BaseCipherOutputFunction(self):
        self.BaseCipherOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                    "保存文件",
                                                                                    '',
                                                                                    "All Files (*)")
        if self.BaseCipherOutputPath == "":
            return
        with open(self.BaseCipherOutputPath, 'w') as out:
            out.write(self.BaseCipherBox.toPlainText())

    def BaseCipherInputFunction(self):
        self.BaseCipherInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.BaseCipherInputPath == "":
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked():
            self.BaseCipherBox.setText('Opened: ' + self.BaseCipherInputPath +
                                       '\n由于你选中了大文件, 文本框不会将其加载.')
            return
        with open(self.BaseCipherInputPath, 'r') as inp:
            try:
                self.BaseCipherBox.setText(inp.read())
            except:
                errorInfo('文件读取错误!')

    def ChangeBase16(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 3
        self.BaseTableBox.setText(Base16StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase32(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 2
        self.BaseTableBox.setText(Base32StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase64(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 1
        self.BaseTableBox.setText(Base64StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase85(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 4
        self.BaseTableBox.setText(Base85StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase85RFC(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 5
        self.BaseTableBox.setText(Base85ReverseTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def BaseEnc(self):
        if self.BaseMode == 1:
            self.Base64Enc()
        elif self.BaseMode == 2:
            self.Base32Enc()
        elif self.BaseMode == 3:
            self.Base16Enc()
        elif self.BaseMode == 4:
            self.Base85Enc()
        elif self.BaseMode == 5:
            self.Base85RFCEnc()
        else:
            pass
        if self.BaseAutoLoadCheckBox.isChecked():
            self.BaseTextBox.setText(self.BaseCipherBox.toPlainText())
        self.BaseTextInputPath = ''

    def BaseDec(self):
        if self.BaseMode == 1:
            self.Base64Dec()
        elif self.BaseMode == 2:
            self.Base32Dec()
        elif self.BaseMode == 3:
            self.Base16Dec()
        elif self.BaseMode == 4:
            self.Base85Dec()
        elif self.BaseMode == 5:
            self.Base85RFCDec()
        else:
            pass
        if self.BaseAutoLoadCheckBox.isChecked():
            self.BaseCipherBox.setText(self.BaseTextBox.toPlainText())
        self.BaseCipherInputPath = ''

    def CheckBaseCipher(self, x, newtable):
        if self.BaseMode == 1:
            try:
                ChangeTableBase64Decode(x, newtable)
            except:
                return False
            return True
        elif self.BaseMode == 2:
            try:
                ChangeTableBase32Decode(x, newtable)
            except:
                return False
            return True
        elif self.BaseMode == 3:
            try:
                ChangeTableBase16Decode(x, newtable)
            except:
                return False
            return True
        elif self.BaseMode == 4:
            try:
                ChangeTableBase85Decode(x, newtable)
            except:
                return False
        elif self.BaseMode == 5:
            try:
                ChangeTableBase85RFCDecode(x, newtable)
            except:
                return False
            return True

    def Base64Dec(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            file = open(self.BaseCipherInputPath, 'r')
            text = file.read()
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择文件.')
            return
        else:
            text = self.BaseCipherBox.toPlainText()
        padding = len(text) % 4
        if padding != 0:
            text += '=' * padding
        if self.CheckBase64Table(self.BaseTableBox.text()) is False or self.CheckBaseCipher(text,
                                                                                            self.BaseTableBox.text()) is False:
            errorInfo(self,
                      '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseCipherInputPath + '.out', '文件已保存')
            try:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()))
            except:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()).encode())
            return
        self.BaseTextBox.setText(str(ChangeTableBase64Decode(
            text, self.BaseTableBox.text())))

    def Base32Dec(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            file = open(self.BaseCipherInputPath, 'r')
            text = file.read()
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择文件.')
            return
        else:
            text = self.BaseCipherBox.toPlainText()
        padding = len(text) % 8
        if padding != 0:
            text += '=' * padding
        if self.CheckBase32Table(self.BaseTableBox.text()) is False or self.CheckBaseCipher(text,
                                                                                            self.BaseTableBox.text()) is False:
            errorInfo(self,
                      '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseCipherInputPath + '.out', '文件已保存')
            try:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()))
            except:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()).encode())
            return
        self.BaseTextBox.setText(str(ChangeTableBase32Decode(
            text, self.BaseTableBox.text())))

    def Base16Dec(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            file = open(self.BaseCipherInputPath, 'r')
            text = file.read()
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择文件.')
            return
        else:
            text = self.BaseCipherBox.toPlainText()
        if self.CheckBase16Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text,
                                                                                            self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseCipherInputPath + '.out', '文件已保存')
            try:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()))
            except:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()).encode())
            return
        self.BaseTextBox.setText(str(ChangeTableBase16Decode(
            text, self.BaseTableBox.text())))

    def Base85Dec(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            file = open(self.BaseCipherInputPath, 'r')
            text = file.read()
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择文件.')
            return
        else:
            text = self.BaseCipherBox.toPlainText()
        if self.CheckBase85Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text,
                                                                                            self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseCipherInputPath + '.out', '文件已保存')
            try:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()))
            except:
                with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                    out.write(ChangeTableBase64Decode(
                        text, self.BaseTableBox.text()).encode())
            return
        self.BaseTextBox.setText(str(ChangeTableBase85Decode(
            text, self.BaseTableBox.text())))

    def Base85RFCDec(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
            file = open(self.BaseCipherInputPath, 'r')
            text = file.read()
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择文件.')
            return
        else:
            text = self.BaseCipherBox.toPlainText()
        try:
            if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseCipherInputPath != '':
                errorInfo(self, '已保存至: ' + self.BaseCipherInputPath + '.out', '文件已保存')
                try:
                    with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                        out.write(ChangeTableBase64Decode(
                            text, self.BaseTableBox.text()))
                except:
                    with open(self.BaseCipherInputPath + '.out', 'wb') as out:
                        out.write(ChangeTableBase64Decode(
                            text, self.BaseTableBox.text()).encode())
                return
            self.BaseTextBox.setText(str(ChangeTableBase85RFCDecode(
                text, self.BaseTableBox.text())))
        except:
            errorInfo(self, '解码失败.')

    def CheckBase64Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 64:
            return False
        return True

    def Base64Enc(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            file = open(self.BaseTextInputPath, 'rb')
            text = str(file.read())
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择路径!')
            return
        else:
            text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked():
            try:
                text = eval(text)
            except:
                errorInfo(self,
                          '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase64Table(self.BaseTableBox.text()) is False:
            errorInfo(self,
                      '编码表无效!!\nTable Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseTextInputPath + '.out', '文件已保存')
            with open(self.BaseTextInputPath + '.out', 'wb') as out:
                out.write(ChangeTableBase64Encode(
                    text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()).encode())
            return
        self.BaseCipherBox.setText(ChangeTableBase64Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase32Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 32:
            return False
        return True

    def Base32Enc(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            file = open(self.BaseTextInputPath, 'rb')
            text = str(file.read())
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择路径!')
            return
        else:
            text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                errorInfo(self,
                          '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase32Table(self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效!!\nTable Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseTextInputPath + '.out', '文件已保存')
            with open(self.BaseTextInputPath + '.out', 'wb') as out:
                out.write(ChangeTableBase64Encode(
                    text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()).encode())
            return
        self.BaseCipherBox.setText(ChangeTableBase32Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase16Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 16:
            return False
        return True

    def Base16Enc(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            file = open(self.BaseTextInputPath, 'rb')
            text = str(file.read())
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择路径!')
            return
        else:
            text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                errorInfo(self,
                          '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase16Table(self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效!!\nTable Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseTextInputPath + '.out', '文件已保存')
            with open(self.BaseTextInputPath + '.out', 'wb') as out:
                out.write(ChangeTableBase64Encode(
                    text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()).encode())
            return
        self.BaseCipherBox.setText(ChangeTableBase16Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase85Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 85:
            return False
        return True

    def CheckBase85RFCTable(self, x):
        checkx = set(list(x))
        if len(checkx) != 85:
            return False
        return True

    def Base85Enc(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            file = open(self.BaseTextInputPath, 'rb')
            text = str(file.read())
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择路径!')
            return
        else:
            text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                errorInfo(self,
                          '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase85Table(self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效!!\nTable Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseTextInputPath + '.out', '文件已保存')
            with open(self.BaseTextInputPath + '.out', 'wb') as out:
                out.write(ChangeTableBase64Encode(
                    text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()).encode())
            return
        self.BaseCipherBox.setText(ChangeTableBase85Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def Base85RFCEnc(self):
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            file = open(self.BaseTextInputPath, 'rb')
            text = str(file.read())
        elif self.BaseDoNotLoadFileCheckBox.isChecked():
            errorInfo(self, '请重新选择路径!')
            return
        else:
            text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                errorInfo(self,
                          '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase85RFCTable(self.BaseTableBox.text()) == False:
            errorInfo(self,
                      '编码表无效!!\nTable Error!!!!!!!')
            return
        if self.BaseDoNotLoadFileCheckBox.isChecked() and self.BaseTextInputPath != '':
            errorInfo(self, '已保存至: ' + self.BaseTextInputPath + '.out', '文件已保存')
            with open(self.BaseTextInputPath + '.out', 'wb') as out:
                out.write(ChangeTableBase64Encode(
                    text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))
            return
        self.BaseCipherBox.setText(ChangeTableBase85RFCEncode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))
