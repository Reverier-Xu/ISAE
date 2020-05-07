import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from ui_Widgets.ErrorWin import errorInfo
from PyQt5.QtGui import QKeySequence
from Config import Settings

class Editor(QWebEngineView):
    value = None
    path = None
    def __init__(self, par):
        super().__init__(par)
        self.editor_flag = []

        # 这里是本地html路径,需根据实际情况进行修改.
        self.editor_index = os.path.abspath('./Resources/Editor/index.html')
        self.load(QUrl.fromLocalFile(self.editor_index))

    def get_value(self, callback):
        """获取编辑器内容"""
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def getit(self, value):
        self.value = value
        if self.path == None or not os.path.exists(self.path):
            self.path, _ = QtWidgets.QFileDialog.getSaveFileName(
                None, "保存", Settings.GlobalPath,
                "All Files (*.*)")
        if self.path == None or not os.path.exists(self.path):
            return
        with open(self.path, 'w') as out:
            out.write(self.value)

    def set_value(self, path):
        """设置编辑器内容"""
        import base64
        try:
            data = open(path, 'r').read()
        except:
            errorInfo(self, '所选文件不是文本文件.')
            return
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.path = path
        self.page().runJavaScript(
            "monaco.editor.getModels()[0].setValue(Base64.decode('{}'))".format(data))
        if path[-3:] == '.py':
            self.change_language('python')
        elif path[-3:] == '.md':
            self.change_language('markdown')
        elif path[-3:] == '.js':
            self.change_language('jsvascript')
        elif path[-3:] == '.json':
            self.change_language('json')
        else:
            self.change_language('text')

    def change_language(self, lan):
        """切换智能提示语言"""
        self.page().runJavaScript(
            "monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{}')".format(lan))

    def save(self):
        self.get_value(self.getit)
