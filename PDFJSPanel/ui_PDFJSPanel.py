import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl

from PDFJSPanel.file_tree import Tree


class ui_PDFJSPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ui_PDFJSPanel, self).__init__(parent)
        self.setObjectName("self")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter1.setContentsMargins(0, 0, 0, 0)
        splitter1.setStyleSheet("QSplitter::handle { background-color: grey; }")
        splitter1.setHandleWidth(1)
        self.PDFFileTreePanel = Tree()
        self.PDFFileTreePanel.setObjectName("PDFFileTreePanel")
        self.PDFFileTreePanel.setMinimumWidth(200)
        splitter1.addWidget(self.PDFFileTreePanel)
        self.PDFViewerPanel = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.PDFViewerPanel.load(
            QUrl.fromUserInput('file:///' + pwd + '/Resources/PDFJS/web/viewer.html'))
        self.PDFViewerPanel.setMinimumWidth(500)
        splitter1.addWidget(self.PDFViewerPanel)
        splitter1.setSizes([200, 500])
        self.horizontalLayout.addWidget(splitter1)

        QtCore.QMetaObject.connectSlotsByName(self)
