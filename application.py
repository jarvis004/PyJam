import ui 
from amp import Amp
from board import Board 
from PyQt5.QtWidgets import QFileDialog
from ui import ROW_COUNT, COLUMN_COUNT, PLAYING, NOT_PLAYING

class GUI(ui.Ui_Form):
    """ The main GUI application. 
        The GUI layout is designed in Ui_Form class which is 
        inherited and events added here.
    """
    def __init__(self, form):
        """ Create UI and add event listeners 
        """
        super().__init__()
        self.setupUi(form)
        self.uiBoard = Board()
        self.uiBoard.setMatrix(self.uiMatrix)
        self.ampBoard = Board()
        self.ampMatrix = list()
        self.amp = None 
        self.filelist = ['', '','']
        self.setupAmp()
        self.addEventListeners()

    def addEventListeners(self):
        """ Added event listeners to GUI elements. 
        """
        self.playButton.clicked.connect(self.playButtonToggled)
        
        # events on the matrix 
        def changeMatrix(a, b):
            """ Dummy method to generate callbacks for matrix events. 
            """
            def callback():
                print (a, b)
                if self.uiMatrix[a][b].isChecked():
                    self.ampMatrix[a][b] = 1
                    self.uiMatrix[a][b].setStyleSheet(ui.CHECKED)
                else:
                    self.uiMatrix[a][b].setStyleSheet(ui.NOT_CHECKED)
                    self.ampMatrix[a][b] = 0
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
        self.amp.timer.signal.connect(self.updateTimer)

        # timer event 
        self.speedTimer.valueChanged.connect(self.updateSpeed)

    def updateSpeed(self):
        """ Slot to update speed when spinbox changed
        """
        self.amp.timeSlice = self.speedTimer.value()

    def updateTimer(self):
        """ Slot to update the current position. 
        """
        t = self.amp.counter
        self.status[t-1].setStyleSheet(NOT_PLAYING)
        self.status[t].setStyleSheet(PLAYING)

    def setupAmp(self):
        """ Create amp object and give it the matrix required. 
        """
        for i in range(3):
            self.ampMatrix.append(list())
            for j in range(16):
                self.ampMatrix[i].append(0)
        self.ampBoard.setMatrix(self.ampMatrix)
        self.ampBoard.setFileList(self.filelist)
        self.amp = Amp(self.ampBoard, self.speedTimer.value())
        self.amp.makePlayers()
        self.amp.status_elems = self.status

    def playButtonToggled(self):
        """ Slot to handle play button clicks. 
        """
        self.status[self.amp.counter].setStyleSheet(NOT_PLAYING)
        self.amp.setPower(self.playButton.isChecked())
        if self.amp.running:
            self.status[self.amp.counter].setStyleSheet(NOT_PLAYING)
        

    def fileChooser(self):
        """ Slot to choose file to play. 
        """
        filename, ok = QFileDialog.getOpenFileName(self.widget, caption="Select audio source",\
                                            directory='.', filter="Audio (*.wav)")
        if filename:
            sender = self.widget.sender()
            if (sender == self.fileSelector0):
                self.filelist[0] = filename
            if (sender == self.fileSelector1):
                self.filelist[1] = filename
            if (sender == self.fileSelector2):
                self.filelist[2] = filename

            sender.setText(filename.split('/')[-1][:7]+"...")
            self.ampBoard.setFileList(self.filelist)
            isRunning = self.amp.running
            t = self.amp.counter 
            if (isRunning):
                self.amp.setPower(False)
            while (self.amp.running):
                pass 
            self.amp.makePlayers()
            if (isRunning):
                self.amp.setPower(True)
                self.amp.counter = t

            
