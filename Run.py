#!/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
import MainWindow


class MainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    #QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    Win = MainWindow()
    Win.setWindowTitle('ICTFE')
    Win.TypeStack.setCurrentWidget(Win.WelcomePanel)
    Win.show()
    sys.exit(app.exec_())
