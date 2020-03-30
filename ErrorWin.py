from PyQt5 import QtCore, QtWidgets, QtGui, Qt
def errorInfo(self, info):
    errorWin = QtWidgets.QDialog(self)
    errorWin.setWindowTitle('错误提示')
    errorWin.setFixedSize(400,130)
    lbl = QtWidgets.QLabel(info,errorWin)
    lbl.move((400-lbl.width())/4,30)
    btn = QtWidgets.QPushButton('确定',errorWin)
    btn.move(230,80)
    btn.clicked.connect(errorWin.close)
    errorWin.exec()