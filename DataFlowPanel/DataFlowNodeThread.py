__AUTHOR__ = 'Reverier Xu'

from copy import copy

from PyQt5.QtCore import QThread


class ComputeThread(QThread):
    func = None
    inp = None
    settings = None
    results = None

    def __init__(self, func, parent=None):
        super().__init__(parent=parent)
        self.func = func

    def run(self):
        try:
            self.results = self.func(self.inp, self.settings)
        except:
            self.results = None

    def getResult(self):
        return copy(self.results)

    def setData(self, inp, settings):
        self.inp = inp
        self.settings = settings
