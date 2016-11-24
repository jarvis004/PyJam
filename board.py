from custom_classes import UnequalLengthError

class Board:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.matrix = None 
        self.fileList = None 
    
    def setMatrix(self, matrix):
        self.matrix = matrix 
        self.rows = len(matrix)
        if (self.rows > 0):
            self.columns = len(self.matrix[0])

    def setFileList(self, filelist):
        if len(filelist) != self.rows:
            raise UnequalLenghtError
        self.filelist = filelist
    