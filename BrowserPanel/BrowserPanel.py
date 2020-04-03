from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem
from ui_Widgets import uni_Widget
import configparser
import sys


class BrowserPanel(QWidget):
    def __init__(self):
        super(BrowserPanel, self).__init__()
        self.UrlBox = QLineEdit(self)
        self.UrlBox.setGeometry(QRect(210, 5, 1210, 30))
        self.UrlBox.setObjectName('UrlBox')
        self.UrlBox.setStyleSheet(
            'color: white;'
            'border: 1px solid gray;'
            'border-radius: 15px;'
            'padding: 0 15px;'
            'background: rgb(20, 20, 20);'
            'selection-background-color: blue;')
        self.NextButton = uni_Widget.ICTFEButton(self)
        self.NextButton.setGeometry(QRect(80, 0, 40, 40))
        self.NextButton.setText('>')
        self.NextButton.setObjectName('NextButton')
        self.BackButton = uni_Widget.ICTFEButton(self)
        self.BackButton.setGeometry(QRect(40, 0, 40, 40))
        self.BackButton.setText('<')
        self.BackButton.setObjectName('BackButton')
        self.RefreshButton = uni_Widget.ICTFEButton(self)
        self.RefreshButton.setGeometry(QRect(120, 0, 40, 40))
        self.RefreshButton.setText('Re')
        self.RefreshButton.setObjectName('RefreshButton')
        self.HomeButton = uni_Widget.ICTFEButton(self)
        self.HomeButton.setGeometry(QRect(160, 0, 40, 40))
        self.HomeButton.setText('XD')
        self.HomeButton.setObjectName('HomeButton')
