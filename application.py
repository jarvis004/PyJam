import ui 
from amp import Amp
from board import Board 
from PyQt5.QtWidgets import QFileDialog

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
        
        # events on the matrix 
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
        # end of callback

        i = 0
        for row in self.uiMatrix:
            j = 0
            for cell in row:
                cell.clicked.connect(changeMatrix(i, j))
                j += 1
            i += 1

        # events on the file choosers 
        self.fileSelector0.clicked.connect(self.fileChooser)
        self.fileSelector1.clicked.connect(self.fileChooser)
        self.fileSelector2.clicked.connect(self.fileChooser)


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
        self.fileChooser()


    def fileChooser(self):
        filename, ok = QFileDialog.getOpenFileName(self.widget, caption="Select audio source",\
                                            directory='.', filter="Audio (*.wav)")
        if filename:
            sender = self.widget.sender()
            if (sender == self.fileSelector0):
                self.filelist[0] = filename
            if (sender == self.fileSelector1):
                self.filelist[1] = filename
            if (sender == self.fileSelector1):
                self.filelist[2] = filename

            sender.setText(filename.split('/')[-1][:20])
            self.ampBoard.setFileList(self.filelist)
