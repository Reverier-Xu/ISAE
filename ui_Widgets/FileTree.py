import os

from PyQt5 import Qt, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from ui_Widgets.ui_FileTree import ui_FileWindow
from Config import Settings


def file_name(path):
    return os.listdir(path)


class FileTreeItem(QtWidgets.QTreeWidgetItem):
    FilePath = ''

    def __init__(self, parent=None):
        super(FileTreeItem, self).__init__(parent)

    def setFilePath(self, path):
        self.FilePath = path


class FileTree(QMainWindow, ui_FileWindow):
    FileDetectedSignal = QtCore.pyqtSignal(FileTreeItem)
    PathSelected = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, path='../ICTFE'):
        super(FileTree, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("File_Tree")

        dirs = file_name(path)
        file_info = Qt.QFileInfo(path)
        file_icon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(file_icon.icon(file_info))
        root = FileTreeItem(self.tree)
        root.setText(0, path.split('/')[-1])
        root.setIcon(0, QtGui.QIcon(icon))
        self.CreateTree(dirs, root, path)
        self.actionFileOpen.clicked.connect(self.Open_Folder)
        QApplication.processEvents()
        self.tree.doubleClicked.connect(
            lambda x: self.EmitFilePath(self.tree.itemFromIndex(x)))

    def Open_Folder(self):
        path = QFileDialog.getExistingDirectory(self, "选取文件夹", Settings.GlobalPath)
        if path == '':
            return
        self.tree.clear()
        dirs = file_name(path)

        file_info = Qt.QFileInfo(path)
        file_icon = Qt.QFileIconProvider()
        icon = QtGui.QIcon(file_icon.icon(file_info))
        root = FileTreeItem(self.tree)
        root.setText(0, path.split('/')[-1])
        root.setIcon(0, QtGui.QIcon(icon))
        self.CreateTree(dirs, root, path)
        QApplication.processEvents()
        self.PathSelected.emit(path)

    def CreateTree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '/' + i
            if os.path.isdir(path_new):
                file_info = Qt.QFileInfo(path_new)
                file_icon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(file_icon.icon(file_info))
                child = FileTreeItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))
                child.setFilePath(path_new)
            else:
                file_info = Qt.QFileInfo(path_new)
                file_icon = Qt.QFileIconProvider()
                icon = QtGui.QIcon(file_icon.icon(file_info))
                child = FileTreeItem(root)
                child.setText(0, i)
                child.setIcon(0, QtGui.QIcon(icon))
                child.setFilePath(path_new)

    def EmitFilePath(self, item):
        self.FileDetectedSignal.emit(item)
