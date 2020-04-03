import os

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets


class WikiPanel(QtWidgets.QWidget):
    def __init__(self):
        super(WikiPanel, self).__init__()

        self.WikiBrowserPanel = WikiBrowserPanelWidget(self)
        self.WikiBrowserPanel.setObjectName('WikiBrowserPanel')
        self.WikiBrowserPanel.setStyleSheet('background-color: transparent;')
        self.WikiBrowserPanel.setGeometry(0, 0, 1428, 768)


class WikiBrowserPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WikiBrowserPanelWidget, self).__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        print('file:///' + pwd + '/Resources/Wiki/index.html')
        self.browser.load(QtCore.QUrl('file:///' + pwd + '/Resources/Wiki/index.html'))
        self.browser.setGeometry(QtCore.QRect(0, 0, 1428, 768))
        self.browser.urlChanged.connect(lambda link: self.SuitLocalWiki(link))
        self.browser.show()

    def SuitLocalWiki(self, qlink):
        link = qlink.toString()
        if link[-1] == '/':
            link += 'index.html'
            out = QtCore.QUrl(link)
            self.browser.load(QtCore.QUrl(out))
