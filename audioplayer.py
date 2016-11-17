import simpleaudio as sa
import time

class AudioPlayer:
    def __init__(self, filename=None, timeSlice=0.5):
        self.filename = filename
        self.timeSlice = timeSlice
        self.play_obj = None 
            
    def setFile(self, filename):
        self.filename = filename

    def setTimeSlice(self, timeSlice):
        self.timeSlice = timeSlice

    def play(self):
        wave_obj = sa.WaveObject.from_wave_file(self.filename)
        self.play_obj = wave_obj.play()
    
    def stop(self):
        if self.play_obj:
            self.play_obj.stop()