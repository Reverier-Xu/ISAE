from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from ui_Widgets import uni_Widget
def errorInfo(self, info, types='错误提示'):
    errorWin = QtWidgets.QDialog(self)
    errorWin.setWindowTitle(types)
    errorWin.setFixedSize(400, 200)
    errorWin.setStyleSheet('background-color: rgb(40, 40, 40)')
    lbl = uni_Widget.ICTFELabel(errorWin)
    lbl.setText(info)
    lbl.move((400-lbl.width())/4, 30)
    btn = uni_Widget.ICTFEButton(errorWin)
    btn.setGeometry(QtCore.QRect(280, 155, 120, 45))
    btn.setText('确定')
    btn.clicked.connect(errorWin.close)
    errorWin.exec()