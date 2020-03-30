from PyQt5 import QtCore, QtWidgets, QtGui
from CryptoPanel.HashModule.ui_HashModule import ui_HashPanel
from hashlib import sha1, sha224, sha3_256, sha384, sha512, sha3_224, sha3_384, sha3_512, sha256


class HashPanel(ui_HashPanel):
    def __init__(self):
        super(HashPanel, self).__init__()
        self.HashEncodeButton.clicked.connect(self.HashEncode)
        self.HashTextInputButton.clicked.connect(self.HashTextInput)

    def HashEncode(self):
        pass

    def HashTextInput(self):
        pass
