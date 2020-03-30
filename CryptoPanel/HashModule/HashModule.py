from PyQt5 import QtCore, QtWidgets, QtGui
from CryptoPanel.HashModule.ui_HashModule import ui_HashPanel
from CryptoPanel.HashModule.HashModuleUtils import *
from ui_Widgets.ErrorWin import errorInfo


class HashPanel(ui_HashPanel):
    def __init__(self):
        super(HashPanel, self).__init__()
        self.HashEncodeButton.clicked.connect(self.HashEncode)
        self.HashTextInputButton.clicked.connect(self.HashTextInput)

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
        else:
            if self.HashEvalCheckBox.isChecked():
                try:
                    text = eval(self.HashTextBox)
                except:
                    errorInfo('Eval执行失败!\n非有效Python语句!')
            else:
                text = self.HashTextBox.toPlainText()


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
