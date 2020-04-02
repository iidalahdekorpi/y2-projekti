from PyQt5 import QtWidgets, QtCore, QtGui
from read_file_IO import ReadFile


class GUI(QtWidgets.QMainWindow):


    def __init__(self, file):
        my_file = ReadFile()
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.plot = my_file.load_coordinates(file)
        self.title = file
        self.init_window()



    def init_window(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle = self.title
        self.show()

'''
    
    def draw_grid(self):

    def draw_axis(self):
    
    def draw_lines(self):

'''