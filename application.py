import ui 
from amp import Amp
from board import Board 

class GUI(ui.Ui_Form):
    def __init__(self, form):
        super().__init__()
        self.setupUi(form)
        self.uiBoard = Board()
        self.uiBoard.setMatrix(self.uiMatrix)
        self.ampBoard = Board()
        self.ampMatrix = list()
        self.amp = None 
        self.filelist = ['hihat.wav', '','']
        self.setupAmp()
        self.addEventListeners()

    def addEventListeners(self):
        self.playButton.clicked.connect(self.playButtonToggled)
        def changeMatrix(a, b):
            print (a, b)
            def callback():
                print (a, b)
                if self.uiMatrix[a][b].isChecked():
                    self.ampMatrix[a][b] = 1
                    self.uiMatrix[a][b].setStyleSheet(ui.CHECKED)
                else:
                    self.uiMatrix[a][b].setStyleSheet(ui.NOT_CHECKED)
                    self.ampMatrix[a][b] = 0
                print (a, b, self.ampMatrix[a][b], self.ampMatrix[a])
            return callback 

        i = 0
        for row in self.uiMatrix:
            j = 0
            for cell in row:
                cell.clicked.connect(changeMatrix(i, j))
                j += 1
            i += 1



    def setupAmp(self):
        for i in range(3):
            self.ampMatrix.append(list())
            for j in range(16):
                self.ampMatrix[i].append(0)
        self.ampBoard.setMatrix(self.ampMatrix)
        self.ampBoard.setFileList(self.filelist)
        self.amp = Amp(self.ampBoard)
        self.amp.makePlayers()
        self.amp.status_elems = self.status

    def changeFileList(self):
        self.filelist[0] = ""

    def playButtonToggled(self):
        self.amp.setPower(self.playButton.isChecked())


from PyQt5.QtWidgets import QDialog, QApplication
import sys 
app = QApplication([])
window = QDialog()
g = GUI(window)
window.show()
sys.exit(app.exec_())