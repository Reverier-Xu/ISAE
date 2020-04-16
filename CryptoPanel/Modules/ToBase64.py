from PyQt5.QtWidgets import QWidget

import CryptoPanel.CryptoNodeBasic as BasicNode
from ui_Widgets import uni_Widget
from CryptoPanel.BaseModule import BaseModuleUtils


class ToBase64(BasicNode.CryptoNode11):
    name = 'To Base64'

    def __init__(self):
        super(ToBase64, self).__init__()
        self.tableBox = uni_Widget.ICTFELineBox()

    def embedded_widget(self) -> QWidget:
        return self.tableBox

    def compute(self, prop=None):
        self._result1 = BaseModuleUtils.ChangeTableBase64Encode(self._string1, self.tableBox.text())
