from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor


class ICTFEButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(ICTFEButton, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton{"
            "background-color:rgba(40, 40, 40, 100%);"
            "color: white;"
            "border-radius: 0px;"
            "border: 0px groove gray;"
            "border-style: outset;"
            "}"
            "QPushButton:hover{"
            "background-color: rgba(60, 60, 60, 100%);"
            "color: white;"
            "}"
            "QPushButton:pressed{"
            "background-color: rgb(100, 100, 100);"
            "border-style: inset; "
            "}")


class ICTFETextBox(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super(ICTFETextBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.setTextColor(QtGui.QColor(200, 200, 200))
        self.setAcceptDrops(True)
        self.setAcceptRichText(False)


class ICTFELineBox(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(ICTFELineBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'color: white;'
            'border: 2px solid gray;'
            'border-radius: 10px;'
            'padding: 0 8px;'
            'background: rgb(20, 20, 20);'
            'selection-background-color: blue;')


class ICTFECheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        super(ICTFECheckBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'QCheckBox:unchecked{ border:none; color: white; }'
            'QCheckBox:checked{ border:none; color: cyan; }')


class ICTFELabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ICTFELabel, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet('color: white;')


class ICTFEList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(ICTFEList, self).__init__(parent)
        self.setStyleSheet(
            '#FileTempStack{'
            'background-color: rgb(20,20,20);'
            'color: white'
            '}')
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)


class ICTFEScrollArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(ICTFEScrollArea, self).__init__(parent)
        self.setStyleSheet(
            'QScrollArea{'
            'border: none;'
            'background-color:rgb(40, 40, 40);'
            '}')
        self.viewport().setStyleSheet(
            'QScrollArea{'
            'border:none;'
            'background-color:rgb(40,40,40);'
            '}')
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
