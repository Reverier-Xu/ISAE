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
        self.setStyleSheet('background-color: rgb(40, 40, 40); color: rgb(40, 40, 40);')
        # 设置浏览器
        self.browser = MyEngineView(self)
        self.browser.setGeometry(QRect(0, 45, 1428, 768 - 45))
        # config = configparser.ConfigParser()
        # config.readfp(open('url.ini'))
        # url= config.get("URL","url")
        url = "https://xdsec.org"
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 使用QToolBar创建导航栏，并使用QAction创建按钮
        # 添加导航栏
        self.navigationBar = QToolBar(self)
        self.navigationBar.setGeometry(QRect(0, 0, 1428, 45))
        # 设定图标的大小
        self.navigationBar.setIconSize(QSize(16, 16))
        # QAction类提供了抽象的用户界面action，这些action可以被放置在窗口部件中
        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QAction(QIcon('./Resources/icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('./Resources/icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('./Resources/icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('./Resources/icons/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # 将按钮添加到导航栏上
        self.navigationBar.addAction(back_button)
        self.navigationBar.addAction(next_button)
        self.navigationBar.addAction(stop_button)
        self.navigationBar.addAction(reload_button)
        # 添加URL地址栏
        self.urlbar = uni_Widget.ICTFELineBox()
        self.urlbar.setText(url)
        # 让地址栏能响应回车按键信号
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.navigationBar.addSeparator()
        self.navigationBar.addWidget(self.urlbar)
        # 让浏览器相应url地址的变化
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        # 将当前网页的链接更新到地址栏
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


class MyEngineView(QWebEngineView):
    '''
    浏览器类。
    '''

    def __init__(self, parent=None, ):
        super(MyEngineView, self).__init__(parent)
        self.parent = parent
        # 有下载信号发起
        self.page().profile().downloadRequested.connect(self.on_downloadRequested)

    def createWindow(self, type):
        '''
        实现点击跳转链接。
        '''
        return self
        # 以下函数里的 ：后为注释，无实际作用
        # 下载信号连接到的槽

    def on_downloadRequested(self, download: "QWebEngineDownloadItem"):
        # download是QWebEngineDownloadItem对象；
        # 下载文件的保存路径及文件名
        old_path = download.path()
        suffix = QFileInfo(old_path).suffix()
        # 下载文件类型
        filttype = download.mimeType()
        # 后缀切割
        unkonw_suffix = filttype.split(r'/')[-1]
        path, _ = QFileDialog.getSaveFileName(self, "Save File", old_path,
                                              "*." + unkonw_suffix + ";;" + "*." + suffix)
        print(old_path, suffix)
        if path != "":
            download.setPath(path)
            download.accept()
