#!/usr/bin/python3

# This is the main script which starts the application 

from ui import Ui_Form
from application import GUI
from PyQt5.QtWidgets import QApplication, QWidget 
import os

# shouldn't have used... but need to override closeEvent
class PyMixerJ(QWidget):
    """ Main application which inherites QWidget and 
        sets up ui. It has a overriden closeEvent method 
        to make sure no threads are running on exit. 
    """
    def __init__(self):
        """ Create gui object. 
        """
        super().__init__()
        self.gui = GUI(self)
        self.show()
     
    
    def closeEvent(self, event):
        """ Overriden  closeEvent to avoid threads running. 
        """
        self.gui.amp.setPower(False)
        while (self.gui.amp.running):
            pass 
        print("Closing application")
        event.accept()

if __name__=="__main__":
    app = QApplication([])
    p = PyMixerJ()
    os._exit(app.exec_())
