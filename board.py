from custom_classes import UnequalLengthError

class Board:
    """ This class manages the board as a matrix, 
        and provides some methods to handle it. 
    """
    def __init__(self):
        """ The constructor for the board. 
        """
        self.rows = 0
        self.columns = 0
        self.matrix = None 
        self.fileList = None 
    
    def setMatrix(self, matrix):
        """ Method to set the matrix variable with the
            one sent as argument. 
        """
        self.matrix = matrix 
        self.rows = len(matrix)
        if (self.rows > 0):
            self.columns = len(self.matrix[0])

    def setFileList(self, filelist):
        """ Set files for corresponding matrix. 
        """
        if len(filelist) != self.rows:
            raise UnequalLenghtError
        self.filelist = filelist
    