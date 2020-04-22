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
        self.width = 700
        self.height = 700
        self.square_size = 30



    def init_window(self):

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle = self.title
        self.show()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 600, 600)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

        self.view.show()


    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        self.draw_grid()
        self.draw_axis(painter)

    def draw_grid(self):

        # Draw_grid metodi piirtää gridin kuvaajaan

        for x in range(self.width):
            for y in range(self.height):
                gridi = QtWidgets.QGraphicsRectItem(self.square_size*(x), self.square_size*(y), self.square_size, self.square_size)
                self.scene.addItem(gridi)


    def draw_axis(self, painter):

        # Draw_axis metodi piirtää x- ja y-akselit kuvaajaan 

        pen = QtGui.QPen()
        pen.setWidth(3)
        #pen.setBrush(QtGui.QColor.green)
        self.x_axis = QtWidgets.QGraphicsLineItem(0, 300, 600, 300)
        self.y_axis = QtWidgets.QGraphicsLineItem(300, 0, 300, 600)
        self.scene.addItem(self.x_axis)
        self.scene.addItem(self.y_axis)
        self.x_axis.setPen(pen)
        self.y_axis.setPen(pen)

        

'''
        self.r_arrow1 = QtWidgets.QGraphicsLineItem(580, 280, 600, 300)
        self.r_arrow1.setPen(pen)
        self.r_arrow2 = QtWidgets.QGraphicsLineItem(580, 320, 600, 300)
        self.r_arrow2.setPen(pen)
        self.scene.addItem(self.r_arrow1)
        self.scene.addItem(self.r_arrow2)

        self.l_arrow1 = QtWidgets.QGraphicsLineItem(280, 580, 300, 600)
        self.l_arrow1.setPen(pen)
        self.l_arrow2 = QtWidgets.QGraphicsLineItem(300, 600, 320, 580)
        self.l_arrow2.setPen(pen)
        self.scene.addItem(self.l_arrow1)
        self.scene.addItem(self.l_arrow2)
        
'''



'''    
    def draw_lines(self):

    def menu_bar(self):
'''

    