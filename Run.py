#!/bin/python3

import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindow
import sys
import time
from PyQt5.Qt import QPixmap


class MainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./Resources/icon.png'))
        self.m_flag = False

    def closeEvent(self, QCloseEvent):
        self.StatusThread.terminate()
        super(MainWindow, self).closeEvent(QCloseEvent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.MaxFlag is False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag and self.MaxFlag is False:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


class SplashScreen(QtWidgets.QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap("./Resources/splash.png"))


if __name__ == "__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    sys.setrecursionlimit(1000000)
    splash = SplashScreen()
    splash.show()
    sleep(0.5)
    QtWidgets.qApp.processEvents()
    Win = MainWindow()
    Win.setWindowTitle('ICTFE')
    Win.TypeStack.setCurrentWidget(Win.WelcomeLabel)
    Win.show()
    splash.finish(Win)
    sys.exit(app.exec_())
