import threading
import time 
from audioplayer import AudioPlayer
from ui import PLAYING, NOT_PLAYING
from custom_classes import UpdateTimer

class Amp:
    """ This class mimics the amplifier.
        It is responsible to start certain number of audio tracks
        and synchronize them. 
    """
    def __init__(self, board, timeSlice=0.5):    
        """ The constructor of this class """
        self.board = board 
        self.playerCount = board.rows 
        self.timeSlice = timeSlice
        self.running = False
        self.powerOn = True  
        self.counter = 0
        self.ampThread = None 
        self.players = None
        self.status_elems = None 
        self.timer = UpdateTimer()

    def makePlayers(self):
        """ Make instances of audio players required for different tracks. 
        """
        if self.players:
            del self.players
        self.players = list()
        for i in range(self.playerCount):
            self.players.append(AudioPlayer())
            self.players[i].setFile(self.board.filelist[i])
        
    def updateSpeeds(self, speed):
        """ Method to update speed of different players.
            It modifies the time slice for single beat for all players. 
        """
        for player in self.players:
            player.timeSlice = speed 

    def setPower(self, status):
        """ Start or stop the amp / Mixer.
            The boolean value of status is the required state. 
        """
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
        """ Thread which is managed by setPower method.
            It runs as long as the amp is running. 
            Synchronized by runinng, counter and powerOn variables.
        """
        self.running = True 
        self.counter = -1
        while self.powerOn:
            if self.running:
                self.counter = (self.counter + 1) % self.board.columns
                for i in range(self.playerCount):
                    if self.board.matrix[i][self.counter]:
                        if self.board.filelist[i]:
                            self.players[i].play()

                time.sleep(self.timeSlice)
                self.timer.update()
                # stop all players 
                i = 0
                for player in self.players:
                    if self.board.filelist[i]:
                        player.stop()
                    i+=1
        
        self.running = False 