import datetime
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem, QWebEngineSettings
from ui_Widgets import uni_Widget
import sys
import socket
import re


class BrowserPanel(QWidget):
    def __init__(self, parent=None):
        super(BrowserPanel, self).__init__(parent)
        self.MainBrowser = BrowserWindow(self)
        self.MainBrowser.setGeometry(QRect(0, 0, 1428, 768))


class BrowserEngineView(QWebEngineView):
    tabs = []

    def __init__(self, Main, parent=None):
        super(BrowserEngineView, self).__init__(parent)
        self.mainWindow = Main

    def createWindow(self, QWebPage_WebWindowType):
        webview = BrowserEngineView(self.mainWindow)
        tab = BrowserTab(self.mainWindow)
        webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        webview.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        webview.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        tab.browser = webview
        tab.setCentralWidget(tab.browser)
        self.tabs.append(tab)
        self.mainWindow.add_new_tab(tab)
        return webview


class BrowserTab(QMainWindow):
    def __init__(self, Main, parent=None):
        super(BrowserTab, self).__init__(parent)
        self.mainWindow = Main
        self.browser = BrowserEngineView(self.mainWindow)
        self.browser.load(QUrl("about:blank"))
        self.setCentralWidget(self.browser)
        self.navigation_bar = QToolBar('Navigation')
        self.navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(self.navigation_bar)

        self.back_button = QAction(QIcon('Assets/back.png'), '后退', self)
        self.next_button = QAction(QIcon('Assets/forward.png'), '前进', self)
        self.stop_button = QAction(QIcon('Assets/stop.png'), '停止', self)
        self.refresh_button = QAction(QIcon('Assets/refresh.png'), '刷新', self)
        self.home_button = QAction(QIcon('Assets/home.png'), '主页', self)
        self.enter_button = QAction(QIcon('Assets/enter.png'), '转到', self)
        self.add_button = QAction(QIcon('Assets/new.png'), '新建标签页', self)
        self.ssl_label1 = QLabel(self)
        self.ssl_label2 = QLabel(self)
        self.url_text_bar = QLineEdit(self)
        self.url_text_bar.setMinimumWidth(300)
        self.url_text_bar.resize(1000, 30)
        self.url_text_bar.setStyleSheet(
            'color: white;'
            'border: 1px solid gray;'
            'border-radius: 0px;'
            'padding: 0 0px;'
            'background: rgb(20, 20, 20);'
            'selection-background-color: blue;')
        self.navigation_bar.addAction(self.back_button)
        self.navigation_bar.addAction(self.next_button)
        self.navigation_bar.addAction(self.refresh_button)
        self.navigation_bar.addAction(self.home_button)
        self.navigation_bar.addAction(self.add_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addWidget(self.ssl_label1)
        self.navigation_bar.addWidget(self.ssl_label2)
        self.navigation_bar.addWidget(self.url_text_bar)
        self.navigation_bar.addAction(self.enter_button)
        self.navigation_bar.setMovable(False)

    def navigate_to_url(self):
        s = QUrl(self.url_text_bar.text())
        if s.scheme() == '':
            s.setScheme('http')
        if re.match('((http|ftp|https)://)?(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?',
                    self.url_text_bar.text()) != None:
            self.browser.load(s)
        else:
            s = QUrl('https://cn.bing.com/search?q=' + self.url_text_bar.text())
            self.browser.load(s)

    def navigate_to_home(self):
        s = QUrl("https://www.bilibili.com/")
        self.browser.load(s)

    def renew_urlbar(self, s):
        prec = s.scheme()
        if prec == 'http':
            self.ssl_label1.setPixmap(QPixmap("Assets/unsafe.png").scaledToHeight(16))
            self.ssl_label2.setText(" 不安全 ")
            self.ssl_label2.setStyleSheet("color:red;")
        elif prec == 'https':
            self.ssl_label1.setPixmap(QPixmap("Assets/safe.png").scaledToHeight(16))
            self.ssl_label2.setText(" 安全 ")
            self.ssl_label2.setStyleSheet("color:green;")
        self.url_text_bar.setText(s.toString())
        self.url_text_bar.setCursorPosition(0)


class BrowserWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet('background-color: rgb(40, 40, 40);')
        self.tabs.setGeometry(QRect(0, 0, 1428, 768))
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setTabShape(0)
        self.init_tab = BrowserTab(self)
        self.init_tab.browser.load(QUrl("https://www.bilibili.com/"))
        self.add_new_tab(self.init_tab)
        self.tabs.tabCloseRequested.connect(lambda i: self.close_current_tab(i))

    def add_blank_tab(self):
        blank_tab = BrowserTab(self)
        self.add_new_tab(blank_tab)

    def add_new_tab(self, tab):
        i = self.tabs.addTab(tab, "新建")
        self.tabs.setCurrentIndex(i)
        self.tabs.setTabIcon(i, QIcon('Assets/main.png'))
        tab.back_button.triggered.connect(tab.browser.back)
        tab.next_button.triggered.connect(tab.browser.forward)
        tab.stop_button.triggered.connect(tab.browser.stop)
        tab.refresh_button.triggered.connect(tab.browser.reload)
        tab.home_button.triggered.connect(tab.navigate_to_home)
        tab.enter_button.triggered.connect(tab.navigate_to_url)
        tab.add_button.triggered.connect(self.add_blank_tab)
        tab.url_text_bar.returnPressed.connect(tab.navigate_to_url)
        tab.browser.urlChanged.connect(tab.renew_urlbar)
        tab.browser.titleChanged.connect(lambda title: (self.tabs.setTabText(i, title),
                                                        self.tabs.setTabToolTip(i, title)))
        # tab.browser.iconChanged.connect(self.tabs.setTabIcon(i, tab.browser.icon()))

    def close_current_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.setCurrentIndex(i)
            s = self.tabs.currentWidget()
            s.deleteLater()
            self.tabs.removeTab(i)
        else:
            pass
