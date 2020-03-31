from PyQt5 import QtCore, QtWidgets, QtGui
from CryptoPanel.HashModule.ui_HashModule import ui_HashPanel
from CryptoPanel.HashModule.HashModuleUtils import *
from ui_Widgets.ErrorWin import errorInfo


class HashPanel(ui_HashPanel):
    def __init__(self):
        super(HashPanel, self).__init__()
        self.HashEncodeButton.clicked.connect(self.HashEncode)
        self.HashTextInputButton.clicked.connect(self.HashTextInput)
        self.HashTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorText(self):
        self.HashTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def HashEncode(self):
        if self.HashTextInputFlag:
            self.MD5ValueBox.setText(str(generate_file_md5(self.HashTextInputPath)))
            self.SHA1ValueBox.setText(str(generate_file_sha1(self.HashTextInputPath)))
            self.SHA224ValueBox.setText(str(generate_file_sha224(self.HashTextInputPath)))
            self.SHA256ValueBox.setText(str(generate_file_sha256(self.HashTextInputPath)))
            self.SHA384ValueBox.setText(str(generate_file_sha384(self.HashTextInputPath)))
            self.SHA512ValueBox.setText(str(generate_file_sha512(self.HashTextInputPath)))
            self.SHA3224ValueBox.setText(str(generate_file_sha3_224(self.HashTextInputPath)))
            self.SHA3256ValueBox.setText(str(generate_file_sha3_256(self.HashTextInputPath)))
            self.SHA3384ValueBox.setText(str(generate_file_sha3_384(self.HashTextInputPath)))
            self.SHA3512ValueBox.setText(str(generate_file_sha3_512(self.HashTextInputPath)))
            self.HashTextInputPath = ''
            self.HashTextInputFlag = False
            self.HashTextBox.setText('')
        else:
            text = ''
            if self.HashEvalCheckBox.isChecked():
                try:
                    text = eval(self.HashTextBox.toPlainText())
                except:
                    errorInfo(self, 'Eval执行失败!\n非有效Python语句!')
                    return
            else:
                try:
                    text = self.HashTextBox.toPlainText()
                    text = text.encode(self.HashEncodingBox.text())
                except:
                    errorInfo(self, '无效的编码!')
                    return
            try:
                salt = int(self.HashSaltBox.text())
            except:
                salt = 0
                if self.HashSaltBox.text() != '':
                    errorInfo(self, '加盐的长度不应该包含除了数字之外的符号!')
            self.HashValueBox.setText(hex(hash(text + addSalt(salt))))
            self.MD5ValueBox.setText(str(generate_md5(text, salt)))
            self.SHA1ValueBox.setText(str(generate_sha1(text, salt)))
            self.SHA224ValueBox.setText(str(generate_sha224(text, salt)))
            self.SHA256ValueBox.setText(str(generate_sha256(text, salt)))
            self.SHA384ValueBox.setText(str(generate_sha384(text, salt)))
            self.SHA512ValueBox.setText(str(generate_sha512(text, salt)))
            self.SHA3224ValueBox.setText(str(
                generate_sha3_224(text, salt)))
            self.SHA3256ValueBox.setText(str(
                generate_sha3_256(text, salt)))
            self.SHA3384ValueBox.setText(str(
                generate_sha3_384(text, salt)))
            self.SHA3512ValueBox.setText(str(
                generate_sha3_512(text, salt)))

    def HashTextInput(self):
        self.HashTextInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.HashTextInputPath == '':
            return
        self.HashTextBox.setText('Opened: ' + self.HashTextInputPath)
        self.HashEvalCheckBox.setChecked(True)
        self.HashTextInputFlag = True
