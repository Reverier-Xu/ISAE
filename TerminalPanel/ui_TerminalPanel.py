from PyQt5.QtCore import QUrl

from ui_Widgets import uni_Widget
from ui_Widgets.ErrorWin import errorInfo
from PyQt5 import Qt, QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import os


class ui_TerminalPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_TerminalPanel, self).__init__()

        self.CyberChefPanel = CyberChefPanelWidget(self)
        self.CyberChefPanel.setObjectName('CyberChefPanel')
        self.CyberChefPanel.setStyleSheet('background-color: transparent;')
        self.CyberChefPanel.setGeometry(0, 0, 1428, 768)


class CyberChefPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CyberChefPanelWidget, self).__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        print('file:///' + pwd + '/CyberChef/CyberChef.html')
        self.browser.load(QtCore.QUrl('file:///' + pwd + '/CyberChef/CyberChef.html'))
        self.browser.setGeometry(QtCore.QRect(0, 0, 1428, 768))
        self.browser.show()
