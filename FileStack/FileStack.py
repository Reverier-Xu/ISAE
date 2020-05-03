__AUTHOR__ = 'Reverier Xu'

import os

from PyQt5.QtCore import QMimeData, QPoint, Qt
from PyQt5.QtGui import QDrag
from PyQt5 import QtWidgets, QtCore

from ui_Widgets import uni_Widget, FileTree
from ui_Widgets.FileTree import file_name
from Config import Settings


class FileStackPanel(QtWidgets.QWidget):
    FileDetectedSingal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None, path='../ICTFE'):
        super(FileStackPanel, self).__init__(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        splitter1 = uni_Widget.ICTFESplitter(QtCore.Qt.Vertical)
        splitter1.setContentsMargins(0, 0, 0, 0)
        self.FileTreePanel = FileTree.FileTree(path=path)
        self.FileTreePanel.setObjectName("FileTreePanel")
        self.FileTreePanel.setMinimumWidth(200)
        splitter1.addWidget(self.FileTreePanel)
        self.FileStackPanel = FileStack(self)
        splitter1.addWidget(self.FileStackPanel)
        splitter1.setSizes([500, 200])
        self.horizontalLayout.addWidget(splitter1, alignment=QtCore.Qt.Alignment())
        self.FileTreePanel.FileDetectedSignal.connect(lambda s: self.CreateFileTree(s))
        self.FileTreePanel.PathSelected.connect(lambda s: self.updateGlobalPath(s))

    def updateGlobalPath(self, s):
        Settings.GlobalPath = os.path.abspath(s)

    def CreateFileTree(self, item):
        path = item.FilePath
        if os.path.isdir(path):
            dirs_new = file_name(path)
            self.FileTreePanel.CreateTree(dirs_new, item, path)
        else:
            self.FileDetectedSingal.emit(path)


class FileStack(uni_Widget.ICTFEList):
    def __init__(self, parent):
        super(FileStack, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.setDropAction(Qt.MoveAction)
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            data = event.mimeData().text()
            text = data
            self.addItem(text)
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def startDrag(self, dropActions, **kwargs):
        item = self.currentItem()
        mime_data = QMimeData()
        mime_data.setText(item.text())
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(QPoint(12, 12))
        drag.exec(Qt.MoveAction)
