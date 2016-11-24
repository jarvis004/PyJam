#!/usr/bin/python3

from ui import Ui_Form
from application import GUI
from PyQt5.QtWidgets import QApplication, QDialog 

import os

# shouldn't have used... but need to override closeEvent
class PyMixerJ(QDialog):
    def __init__(self):
        super().__init__()
        self.gui = GUI(self)
        self.show()
     
    
    def closeEvent(self, event):
        self.gui.amp.setPower(False)
        while (self.gui.amp.running):
            pass 
        print("Closing application")
        event.accept()

if __name__=="__main__":
    app = QApplication([])
    p = PyMixerJ()
    os._exit(app.exec_())
