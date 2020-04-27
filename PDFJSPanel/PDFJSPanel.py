import os

from PDFJSPanel.ui_PDFJSPanel import ui_PDFJSPanel
from PyQt5 import QtCore
import os
from urllib import parse

def file_name(path):
    return os.listdir(path)

class PDFJSPanel(ui_PDFJSPanel):
    def __init__(self, parent=None):
        super(PDFJSPanel, self).__init__(parent)
        self.PDFFileTreePanel.tree.doubleClicked.connect(
            lambda x: self.PDFFileTreePanel.EmitFilePath(self.PDFFileTreePanel.tree.itemFromIndex(x)))
        self.PDFFileTreePanel.actionFileOpen.triggered.connect(self.PDFFileTreePanel.Open_Folder)
        self.PDFFileTreePanel.FileDetectedSignal.connect(lambda s: self.ChangePDFViewer(s))

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
