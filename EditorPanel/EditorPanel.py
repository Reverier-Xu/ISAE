from EditorPanel.MonacoEditor import Editor
from PyQt5 import QtGui, QtCore, QtWidgets


class EditorPanel(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.layouts = QtWidgets.QVBoxLayout()
        self.layouts.setContentsMargins(0, 0, 0, 0)
        self.editor = Editor(None)
        self.editor.setZoomFactor(1.5)
        self.editor.change_language('python')
        self.layouts.addWidget(self.editor)
        self.setLayout(self.layouts)
        self.save_action = QtWidgets.QAction(self)
        self.save_action.setShortcut(QtGui.QKeySequence('Ctrl+S'))
        self.save_action.triggered.connect(self.editor.save)
        self.editor.addAction(self.save_action)
