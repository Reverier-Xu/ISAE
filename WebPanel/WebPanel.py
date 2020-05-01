import os

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
import platform
from PyQt5.QtWebEngineWidgets import QWebEngineSettings


class WebPanel(QtWidgets.QWidget):
    def __init__(self):
        super(WebPanel, self).__init__(flags=Qt.WindowFlags())
        self.WebBrowserPanel = WebBrowserPanelWidget(self)
        self.WebBrowserPanel.setObjectName('WebBrowserPanel')
        self.WebBrowserPanel.setStyleSheet('background-color: transparent;')
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.WebBrowserPanel, alignment=Qt.Alignment())
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)


class WebBrowserPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WebBrowserPanelWidget, self).__init__(parent, flags=Qt.WindowFlags())
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.browser.load(QtCore.QUrl('https://postwoman.io/'))
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.browser, alignment=Qt.Alignment())
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.browser.urlChanged.connect(lambda link: self.SuitLocalWeb(link))
        self.browser.show()
        self.browser.setZoomFactor(1)
        self.setLayout(self.Layouts)
        osinfo = platform.system()
        if osinfo == 'Windows':
            self.browser.settings().setFontFamily(QWebEngineSettings.StandardFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.FixedFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SansSerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.CursiveFont, '微软雅黑')
        self.shortcutd = QShortcut(QKeySequence("Ctrl+="), self)
        self.shortcutd.activated.connect(self.zoom_in_func)
        self.shortcutu = QShortcut(QKeySequence("Ctrl+-"), self)
        self.shortcutu.activated.connect(self.zoom_out_func)

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def SuitLocalWeb(self, qlink):
        pass
