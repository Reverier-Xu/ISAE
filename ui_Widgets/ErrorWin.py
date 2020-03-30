from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


def errorInfo(self, info, types='错误提示'):
    errorWin = QtWidgets.QDialog()
    errorWin.setWindowTitle(types)
    errorWin.setFixedSize(400, 300)
    errorWin.setStyleSheet('background-color: rgb(40, 40, 40)')
    lbl = uni_Widget.ICTFETextBox(errorWin)
    lbl.setText(info)
    lbl.setGeometry(QtCore.QRect(1, 1, 398, 253))
    btn = uni_Widget.ICTFEButton(errorWin)
    btn.setGeometry(QtCore.QRect(280, 255, 120, 45))
    btn.setText('确定')
    btn.clicked.connect(errorWin.close)
    errorWin.exec()