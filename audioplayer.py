import simpleaudio as sa
import time

class AudioPlayer:
    """ Audio player which give simple methods to handle the audio player. 
        The audio player is provided by simpleaudio library.
    """
    def __init__(self, filename=None, timeSlice=0.3):
        """ Constructor to create audio player. 
        """
        self.filename = filename
        self.timeSlice = timeSlice
        self.play_obj = None 
            
    def setFile(self, filename):
        """ Set file for this player. 
        """
        self.filename = filename

    def setTimeSlice(self, timeSlice):
        """ Set timeslice for current player. 
        """
        self.timeSlice = timeSlice

    def play(self):
        """ Method to play the file. 
        """
        wave_obj = sa.WaveObject.from_wave_file(self.filename)
        self.play_obj = wave_obj.play()
    
    def stop(self):
        """ Method to stop current playback. 
        """
        if self.play_obj:
            self.play_obj.stop()