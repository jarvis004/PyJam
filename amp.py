import threading
import time 
from audioplayer import AudioPlayer
from ui import PLAYING, NOT_PLAYING

class Amp:
    def __init__(self, board, timeSlice=0.5):    
        self.board = board 
        self.playerCount = board.rows 
        self.timeSlice = timeSlice
        self.running = False
        self.powerOn = True  
        self.counter = 0
        self.ampThread = None 
        self.players = None
        self.status_elems = None 

    def makePlayers(self):
        if self.players:
            del self.players
        self.players = list()
        for i in range(self.playerCount):
            self.players.append(AudioPlayer())
            self.players[i].setFile(self.board.filelist[i])

    def setPower(self, status):
        if status:
            if not self.ampThread:
                del self.ampThread
                self.powerOn = True 
                self.ampThread = threading.Thread(target=self.playIndefinitely)
                self.ampThread.start()
        else:
            self.powerOn = False 
            while self.running:
                pass 
            self.ampThread = None

    def playIndefinitely(self):
        self.running = True 
        self.counter = -1
        while self.powerOn:
            if self.running:
                self.counter = (self.counter + 1) % self.board.columns
                for i in range(self.playerCount):
                    if self.board.matrix[i][self.counter]:
                        if self.board.filelist[i]:
                            self.players[i].play()
                        print(i, '-', self.counter)

                self.status_elems[self.counter].setStyleSheet(PLAYING)
                time.sleep(self.timeSlice)
                self.status_elems[self.counter].setStyleSheet(NOT_PLAYING)
                # stop all players 
                i = 0
                for player in self.players:
                    if self.board.filelist[i]:
                        player.stop()
                    i+=1
        
        self.running = False 