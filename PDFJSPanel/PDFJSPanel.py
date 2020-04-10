import os

from PDFJSPanel.ui_PDFJSPanel import ui_PDFJSPanel
from PyQt5 import QtCore


class PDFJSPanel(ui_PDFJSPanel):
    def __init__(self, parent=None):
        super(PDFJSPanel, self).__init__(parent)
        self.PDFFileTreePanel.FileDetectedSignal.connect(lambda s: self.ChangePDFViewer(s))

    def ChangePDFViewer(self, path):
        if path[-4:] == '.pdf':
            pwd = os.getcwd()
            pwd = pwd.replace('\\', '/')
            if path[0] == '.':
                path = pwd + path[1:]
            print('file:///' + pwd + '/Resources/PDFJS/web/viewer.html?file=file:///' + path)
            self.PDFViewerPanel.load(
                QtCore.QUrl.fromUserInput('file:///' + pwd + '/Resources/PDFJS/web/viewer.html?file=file:///' + path))
