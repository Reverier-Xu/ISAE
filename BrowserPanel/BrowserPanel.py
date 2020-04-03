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
        self.UrlBox.setGeometry(200, 0, 1228, 30)