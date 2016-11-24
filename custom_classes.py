class UnequalLengthError(Exception):
    pass


from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

class UpdateTimer(QWidget):
    signal = pyqtSignal()

    def update(self):
        self.signal.emit()