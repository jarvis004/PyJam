from board import Board
from amp import Amp

b = Board()
matrix = list()
row_0 = [1, 0, 0, 1, 1, 0]
row_1 = [1, 1, 0, 1, 1, 0]
row_2 = [1, 0, 1, 0, 0, 0]
matrix.append(row_0)
matrix.append(row_1)
matrix.append(row_2)

b.setMatrix(matrix)
filelist = ['audio.wav', 'hihat.wav', 'audio.wav']
b.setFileList(filelist)
a = Amp(b)
a.makePlayers()