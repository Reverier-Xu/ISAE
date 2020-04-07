import os

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


class WikiPanel(QtWidgets.QWidget):
    def __init__(self):
        super(WikiPanel, self).__init__()
        self.WikiBrowserPanel = WikiBrowserPanelWidget(self)
        self.WikiBrowserPanel.setObjectName('WikiBrowserPanel')
        self.WikiBrowserPanel.setStyleSheet('background-color: transparent;')
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.WikiBrowserPanel)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)


class WikiBrowserPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WikiBrowserPanelWidget, self).__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        print('file:///' + pwd + '/Resources/Wiki/index.html')
        self.browser.load(QtCore.QUrl(
            'file:///' + pwd + '/Resources/Wiki/index.html'))
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.browser)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.browser.urlChanged.connect(lambda link: self.SuitLocalWiki(link))
        self.browser.show()
        self.browser.setZoomFactor(1.1)
        self.setLayout(self.Layouts)

        self.shortcutd = QShortcut(QKeySequence("Ctrl+="), self)
        self.shortcutd.activated.connect(self.zoom_in_func)
        self.shortcutu = QShortcut(QKeySequence("Ctrl+-"), self)
        self.shortcutu.activated.connect(self.zoom_out_func)

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def SuitLocalWiki(self, qlink):
        link = qlink.toString()
        if link[-1] == '/':
            link += 'index.html'
            out = QtCore.QUrl(link)
            self.browser.load(QtCore.QUrl(out))
