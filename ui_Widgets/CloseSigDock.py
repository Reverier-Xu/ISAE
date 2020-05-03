from PyQt5 import QtCore, QtWidgets


class CloseSigDock(QtWidgets.QDockWidget):
    closeSig = QtCore.pyqtSignal()

    def __init__(self, title: str, parent: QtWidgets.QWidget = None):
        super(CloseSigDock, self).__init__(title, parent)

    def closeEvent(self, QCloseEvent):
        self.closeSig.emit()
        super(CloseSigDock, self).closeEvent(QCloseEvent)
