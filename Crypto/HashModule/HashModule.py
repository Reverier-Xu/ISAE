from PyQt5 import QtCore, QtWidgets
from Crypto.HashModule.ui_HashModule import ui_HashPanel


class HashPanel(ui_HashPanel):
    def __init__(self):
        super(HashPanel, self).__init__()
