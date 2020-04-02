from PyQt5.QtCore import QUrl

from ui_Widgets import uni_Widget
from ui_Widgets.ErrorWin import errorInfo
from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from PyQt5.QtWebEngineWidgets import *
import os


class ui_TerminalPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_TerminalPanel, self).__init__()

        # change buttons
        self.CyberChefButton = uni_Widget.ICTFEButton(self)
        self.CyberChefButton.setObjectName('CyberChefButton')
        self.CyberChefButton.setGeometry(QtCore.QRect(0, 0, 128, 128))
        self.CyberChefButton.setText('CyberChef')

        self.TerminalStack = QtWidgets.QStackedWidget(self)
        self.TerminalStack.setObjectName('TerminalStack')
        self.TerminalStack.setGeometry(QtCore.QRect(0, 132, 1428, 635))

        self.CyberChefPanel = CyberChefPanelWidget()
        self.CyberChefPanel.setObjectName('CyberChefPanel')
        self.TerminalStack.addWidget(self.CyberChefPanel)
        self.CyberChefButton.clicked.connect(
            lambda: self.TerminalStack.setCurrentWidget(self.CyberChefPanel))


class CyberChefPanelWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CyberChefPanelWidget, self).__init__()
        self.browser = QWebEngineView(self)
        pwd = os.getcwd()
        self.browser.load(QtCore.QUrl('file://' + pwd + '/CyberChef/CyberChef.html'))
        self.browser.show()
        self.browser.setGeometry(QtCore.QRect(0, 0, 1428, 630))
