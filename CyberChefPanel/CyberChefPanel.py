import os
import platform

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem, QWebEngineSettings
from PyQt5.QtWidgets import QFileDialog, QShortcut


class CyberChefPanel(QtWidgets.QWidget):
    def __init__(self):
        super(CyberChefPanel, self).__init__(flags=QtCore.Qt.WindowFlags())

        self.CyberChefPanel = CyberChefPanelWidget(self)
        self.CyberChefPanel.setObjectName('CyberChefPanel')
        self.CyberChefPanel.setStyleSheet('background-color: transparent;')
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.CyberChefPanel)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)


class CyberChefPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CyberChefPanelWidget, self).__init__(parent, flags=QtCore.Qt.WindowFlags())
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.browser.load(QtCore.QUrl(
            'file:///' + pwd + '/Resources/CyberChef/CyberChef.html'))
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.browser)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)
        self.browser.show()
        self.browser.setZoomFactor(1.2)
        self.browser.page().profile().downloadRequested.connect(self.on_downloadRequested)
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

    def on_downloadRequested(self, download: "QWebEngineDownloadItem"):
        # download是QWebEngineDownloadItem对象；
        # 下载文件的保存路径及文件名
        old_path = download.path()
        suffix = QFileInfo(old_path).suffix()
        # 下载文件类型
        file_type = download.mimeType()
        # 后缀切割
        unknown_suffix = file_type.split(r'/')[-1]
        path, _ = QFileDialog.getSaveFileName(
            self, "保存到", old_path, "*." + unknown_suffix + ";;" + "*." + suffix)
        if path != "":
            download.setPath(path)
            download.accept()
