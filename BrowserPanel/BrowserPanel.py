import os
import platform
import re

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import *

from ui_Widgets import uni_Widget


class BrowserPanel(QWidget):
    def __init__(self, parent=None):
        super(BrowserPanel, self).__init__(parent, flags=Qt.WindowFlags())
        self.MainBrowser = BrowserWindow(self)
        self.Layouts = QHBoxLayout(self)
        self.Layouts.addWidget(self.MainBrowser)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)


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
        QWebEngineSettings.defaultSettings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True)
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
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.browser.load(
            QUrl('file:///' + pwd + '/Resources/Search/Search.html'))
        self.browser.setZoomFactor(1.5)
        self.setCentralWidget(self.browser)
        self.navigation_bar = QToolBar('Navigation')
        self.navigation_bar.setIconSize(QSize(18, 18))
        self.navigation_bar.setMaximumHeight(35)
        self.navigation_bar.setContentsMargins(1, -1, 1, -1)
        self.navigation_bar.setStyleSheet('QToolBar{border: 1px solid grey;}')
        self.addToolBar(self.navigation_bar)
        osinfo = platform.system()
        if osinfo == 'Windows':
            self.browser.settings().setFontFamily(QWebEngineSettings.StandardFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.FixedFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SansSerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.CursiveFont, '微软雅黑')
        self.back_button = QAction(QIcon('Assets/back.png'), '后退', self)
        self.next_button = QAction(QIcon('Assets/forward.png'), '前进', self)
        self.stop_button = QAction(QIcon('Assets/stop.png'), '停止', self)
        self.refresh_button = QAction(QIcon('Assets/refresh.png'), '刷新', self)
        self.home_button = QAction(QIcon('Assets/home.png'), '主页', self)
        self.enter_button = QAction(QIcon('Assets/enter.png'), '转到', self)
        self.add_button = QAction(QIcon('Assets/new.png'), '新建标签页', self)
        self.ssl_label1 = QLabel(self)
        self.ssl_label1.setPixmap(
            QPixmap("Assets/main.png").scaledToHeight(18))
        self.ssl_label2 = QLabel(self)
        self.ssl_label2.setText(" 欢迎来到ICTFE ")
        self.ssl_label2.setStyleSheet("color:white;")
        self.url_text_bar = uni_Widget.ICTFELineBox(self)
        self.url_text_bar.setMinimumWidth(300)
        self.url_text_bar.resize(1000, 30)
        self.url_text_bar.setStyleSheet(
            'color: white;'
            'border: 1px solid gray;'
            'border-radius: 0px;'
            'padding: 0 0px;'
            'background: rgb(20, 20, 20);'
            'selection-background-color: blue;'
            'font: 18px;')
        self.navigation_bar.addAction(self.back_button)
        self.navigation_bar.addAction(self.next_button)
        self.navigation_bar.addAction(self.refresh_button)
        self.navigation_bar.addAction(self.home_button)
        self.navigation_bar.addAction(self.add_button)
        self.navigation_bar.addWidget(self.ssl_label1)
        self.navigation_bar.addWidget(self.ssl_label2)
        self.navigation_bar.addWidget(self.url_text_bar)
        self.navigation_bar.addAction(self.enter_button)
        self.navigation_bar.setMovable(False)
        self.shortcutd = QShortcut(QKeySequence("Ctrl+="), self)
        self.shortcutd.activated.connect(self.zoom_in_func)
        self.shortcutu = QShortcut(QKeySequence("Ctrl+-"), self)
        self.shortcutu.activated.connect(self.zoom_out_func)

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def navigate_to_url(self):
        s = QUrl(self.url_text_bar.text())
        if s.scheme() == '':
            s.setScheme('http')
        if re.match(
                '((http|ftp|https)://)?(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?',
                self.url_text_bar.text()) != None or self.url_text_bar.text()[:4] == 'file':
            self.browser.load(s)
        else:
            s = QUrl('https://cn.bing.com/search?q=' +
                     self.url_text_bar.text())
            self.browser.load(s)
        self.browser.setZoomFactor(1.2)

    def navigate_to_home(self):
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.browser.load(
            QUrl('file:///' + pwd + '/Resources/Search/Search.html'))
        self.browser.setZoomFactor(1.5)
        self.browser.show()

    def renew_urlbar(self, s):
        prec = s.scheme()
        if prec == 'http':
            self.ssl_label1.setPixmap(
                QPixmap("Assets/unsafe.png").scaledToHeight(18))
            self.ssl_label2.setText(" 不安全 ")
            self.ssl_label2.setStyleSheet("color:red;")
        elif prec == 'https':
            self.ssl_label1.setPixmap(
                QPixmap("Assets/safe.png").scaledToHeight(18))
            self.ssl_label2.setText(" 安全 ")
            self.ssl_label2.setStyleSheet("color:green;")
        self.url_text_bar.setText(s.toString())
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        if s.toString().count('/Resources/Search/Search.html')!=0:
            self.url_text_bar.setText('Home Page~')
        self.url_text_bar.setCursorPosition(0)


class BrowserWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet('''
QTabWidget::pane {
  border: 1px solid rgb(30, 30, 30);
  top:0px;
  background: rgb(30, 30, 30);
}

QTabBar::tab {
  background: rgb(30, 30, 30);
  color: white;
  border: 1px solid rgb(30, 30, 30);
  padding: 1px;
}

QTabBar::tab:selected {
  background: rgb(40, 100, 245);
  margin-bottom: 0px;
}''')
        self.Layouts = QHBoxLayout(self)
        self.Layouts.addWidget(self.tabs)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setTabShape(0)
        self.init_tab = BrowserTab(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.init_tab.browser.load(
            QUrl('file:///' + pwd + '/Resources/Search/Search.html'))
        self.init_tab.browser.setZoomFactor(1.5)
        self.add_new_tab(self.init_tab)
        self.tabs.tabCloseRequested.connect(
            lambda i: self.close_current_tab(i))

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

    #        tab.browser.iconChanged.connect(self.tabs.setTabIcon(i, tab.browser.icon()))

    def close_current_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.setCurrentIndex(i)
            s = self.tabs.currentWidget()
            s.deleteLater()
            self.tabs.removeTab(i)
        else:
            pass
