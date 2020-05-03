__AUTHOR__ = 'Reverier Xu'

import os

from Config import Settings
from PDFJSPanel.ui_PDFJSPanel import ui_PDFJSPanel
from PyQt5 import QtCore
import os
from urllib import parse


def file_name(path):
    return os.listdir(path)


class PDFJSPanel(ui_PDFJSPanel):
    def __init__(self, parent=None):
        super(PDFJSPanel, self).__init__(parent)
        self.PDFFileTreePanel.FileDetectedSignal.connect(lambda s: self.ChangePDFViewer(s))
        self.PDFFileTreePanel.PathSelected.connect(lambda s: self.updatePDFPath(s))

    def ChangePDFViewer(self, item):
        path = item.FilePath
        if path[-4:] == '.pdf':
            pwd = os.getcwd()
            pwd = pwd.replace('\\', '/')
            path = parse.quote(path, encoding='UTF-8')
            if path[0] == '.':
                path = pwd + path[1:]
            self.PDFViewerPanel.load(
                QtCore.QUrl.fromUserInput('file:///' + pwd + '/Resources/PDFJS/web/viewer.html?file=file:///' + path))
        elif os.path.isdir(path):
            dirs_new = file_name(path)
            self.PDFFileTreePanel.CreateTree(dirs_new, item, path)

    def updatePDFPath(self, s):
        Settings.PDFPath = s
