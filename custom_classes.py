class UnequalLengthError(Exception):
    """ Custom error raised when the number of files 
        is not equal to the number of rows in the matrix. 
    """
    pass


from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

class UpdateTimer(QWidget):
    """ Custom signal emitted by amplifier thread 
        to update the counter label in GUI 
    """
    signal = pyqtSignal()

    def update(self):
        """ Method which emits the signal. 
        """
        self.signal.emit()