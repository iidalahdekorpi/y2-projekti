import sys, random
from PyQt5 import QtWidgets, QtCore, QtGui
from read_file_IO import ReadFile


class GUI(QtWidgets.QMainWindow):


    def __init__(self, file):

        super().__init__()
        my_file = ReadFile()

        self.plot = my_file.load_coordinates(file)
        self.bcolor = QtGui.QColor(255, 255, 255)
        self.acolor = QtGui.QColor(0, 0, 0)
        self.linecolor = self.randomize_color()
        self.square_size = 30
        self.xlab = 'x'
        self.ylab = 'y'
        self.grid = True
        self.init_window()
        self.set_toolBar()
        self.show()


    def init_window(self):

        self.setGeometry(60, 60, 800, 600)
        self.setWindowTitle = ('Data visualization')
        self.show()


    def boundingRect(self):
        return QtCore.QRectF(0, 0, 800, 600)

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        if self.grid:
            self.draw_grid(painter)
        self.draw_axis(painter)
        for group, points in self.plot.lines.items():
            pen = QtGui.QPen()
            pen.setWidth(3)
            pen.setColor(self.linecolor)
            painter.setPen(pen)
            self.draw_lines(group, points, painter)
            painter.drawText(self.width()*0.8, self.height()*0.1, group)
            self.update()
    


    def draw_grid(self, painter):

        # Method draws grid

        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.DotLine)
        painter.setPen(pen)
        painter.setBrush(self.bcolor)
        for x in range(self.width()):
            for y in range(self.height()):
                painter.drawRect(self.square_size*(x), self.square_size*(y), self.square_size, self.square_size)
  
             

    def draw_axis(self, painter):

        # Method draws axis lines, label names and axis

        pen = QtGui.QPen()
        pen.setWidth(2)
        pen.setColor(self.acolor)
        painter.setPen(pen)

        painter.drawLine(self.width()*0.05, self.height()*0.95, self.width(), self.height()*0.95)
        painter.drawLine(self.width()*0.05, 0, self.width()*0.05, self.height()*0.95)
        

        painter.drawText(self.width()*0.03, self.height()*0.95, str(self.plot.get_x_min()))
        painter.drawText(self.width()*0.06, self.height()*0.97, str(self.plot.get_y_min()))

        painter.drawLine(self.width()*0.95, self.height()*0.94, self.width()*0.95, self.height()*0.96)
        painter.drawText(self.width()*0.95, self.height()*0.92, str(self.plot.get_x_max()))

        painter.drawLine(self.width()*0.04, self.height()*0.15, self.width()*0.06, self.height()*0.15)
        painter.drawText(self.width()*0.07, self.height()*0.15, str(self.plot.get_y_max()))

        painter.drawText(self.width()*0.97, self.height()*0.9, self.xlab)
        painter.drawText(self.width()*0.03, self.height()*0.1, self.ylab)
    
        


    def draw_lines(self, group, points, painter):

        # Methdod draws linegraph

        i = 0
        while i < len(points.points)-1:

            a_x = abs((points.points[i+1].x - points.points[i].x))/self.plot.get_x_range()
            a_y = abs((points.points[i+1].y - points.points[i].y))/self.plot.get_y_range()

            x1 = a_x*self.width()*0.9*i + self.width()*0.05
            y1 = self.height()*0.95 - a_y*self.height()*0.8*points.points[i].y
            x2 = a_x*(i+1)*self.width()*0.9 + self.width()*0.05
            y2 = self.height()*0.95 - a_y*self.height()*0.8*points.points[i+1].y
            painter.drawLine(x1, y1, x2, y2)

            i += 1
        
            
               
    def randomize_color(self):
        return QtGui.QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def gridon(self):

        # Let user set grid on/off

        if self.grid == True:
            self.grid = False
        self.grid = True
        self.update()

    def grid_size(self):
        
        # Let user set grid square size

        size, ok = QtWidgets.QInputDialog.getText(self, 'Grid square size', 'Enter grid square size:')
        if size and ok:
            self.square_size = int(size)
        self.update()

    def labelnames(self):
        xname, ok = QtWidgets.QInputDialog.getText(self, 'X-label name', 'Enter name for X-label:')
        if xname and ok:
            self.xlab = xname
        yname, ok = QtWidgets.QInputDialog.getText(self, 'Y-label name', 'Enter name for Y-label:')
        if yname and ok:
            self.ylab = yname


    def backgroundcolor(self):

        # Let user change background color

        color = QtWidgets.QColorDialog.getColor()
        self.bcolor = color
        self.update()

    def axiscolor(self):

        # Let user change axis line color

        color = QtWidgets.QColorDialog.getColor()
        self.acolor = color
        self.update()



    def set_toolBar(self):

        # Method sets up the toolbar in the upper side of the graph

        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)

        gridAction = QtWidgets.QAction('&Grid', self)
        gridAction.triggered.connect(self.gridon)
        toolbar.addAction(gridAction)

        gridsizeAction = QtWidgets.QAction('&Gridsize', self)
        gridsizeAction.triggered.connect(self.grid_size)
        toolbar.addAction(gridsizeAction)

        labelAction = QtWidgets.QAction('&Labels', self)
        labelAction.triggered.connect(self.labelnames)
        toolbar.addAction(labelAction)

        bcolorAction = QtWidgets.QAction('&BackgroundColor', self)
        bcolorAction.triggered.connect(self.backgroundcolor)
        toolbar.addAction(bcolorAction)

        acolorAction = QtWidgets.QAction('&AxisColor', self)
        acolorAction.triggered.connect(self.axiscolor)
        toolbar.addAction(acolorAction)

        exitAction = QtWidgets.QAction('&Exit', self)
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        toolbar.addAction(exitAction)





    