import sys, random
from PyQt5 import QtWidgets, QtCore, QtGui
from read_file_IO import ReadFile


class GUI(QtWidgets.QMainWindow):


    def __init__(self, file, type):

        super().__init__()
        my_file = ReadFile()
        if type == 'line':
            self.plot = my_file.load_coordinates(file)
        else:
            print("Feature not yet implemented!")
        self.colors = []
        self.yticks = []
        self.xticks = []
        #self.randomize_color()
        self.bcolor = QtGui.QColor(255, 255, 255)
        self.acolor = QtGui.QColor(0, 0, 0)
        self.square_size = 30
        self.lwidth = 3
        self.xlab = 'x'
        self.ylab = 'y'
        self.grid = True
        self.nos = True
        self.init_window()
        self.show()


    def init_window(self):

        self.setGeometry(60, 60, 800, 600)
        self.setWindowTitle = ('Data visualization')
        self.set_toolBar()
        self.show()


    def boundingRect(self):
        return QtCore.QRectF(0, 0, 800, 600)

    def paintEvent(self, event):

        # Metod to draw the whole graph

        painter = QtGui.QPainter(self)
        if self.grid:
            self.draw_grid(painter)
        else:
            painter.setBrush(self.bcolor)
            painter.drawRect(0,0,self.width(), self.height())
        self.draw_axis(painter)
        g = 0
        for group, points in self.plot.lines.items():
            self.leg = group
            pen = QtGui.QPen()
            linecolor = QtCore.Qt.black
            g += 1
            pen.setColor(linecolor)
            painter.setPen(pen)
            painter.drawText(self.width()*0.8, self.height()*0.1 + g*15, self.leg)
            self.draw_lines(group, points, painter, pen, linecolor)
            self.update()
        painter.end()
    


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

        # Draws x-axis
        painter.drawLine(self.width()*0.05, self.height()*0.95, self.width(), self.height()*0.95)
        # Draws y-axis
        painter.drawLine(self.width()*0.05, 0, self.width()*0.05, self.height()*0.95)


        # Max value of x
        painter.drawLine(self.width()*0.95, self.height()*0.94, self.width()*0.95, self.height()*0.96)
        if self.plot.get_x_range() == 0:
            xmax = str(self.plot.get_x_max() + 1)
        else:
            xmax = str(self.plot.get_x_max())
        painter.drawText(self.width()*0.95, self.height()*0.92, xmax)

        # Max value of y
        painter.drawLine(self.width()*0.04, self.height()*0.15, self.width()*0.06, self.height()*0.15)
        if self.plot.get_y_range() == 0:
            ymax = str(self.plot.get_y_max() + 1)
        else:
            ymax = str(self.plot.get_y_max())
        painter.drawText(self.width()*0.07, self.height()*0.15, ymax)

        # Draw axis labels
        painter.drawText(self.width()*0.85, self.height()*0.98, self.xlab)
        painter.drawText(self.width()*0.07, self.height()*0.1, self.ylab)
    
    def draw_ticks(self, painter, pen, x1, y1, px, py):

            # Method draw ticks and numbers for axis lines

            pen.setColor(QtCore.Qt.black)
            pen.setWidth(2)
            painter.setPen(pen)

            painter.drawLine(x1, self.height()*0.94, x1, self.height()*0.96)
            painter.drawLine(self.width()*0.04, y1, self.width()*0.06, y1)

            if self.nos == True:
                painter.drawText(x1, self.height()*0.92, str(px))
                painter.drawText(self.width()*0.07, y1, str(py))


    def draw_lines(self, group, points, painter, pen, linecolor):

        # Methdod draws lines point by point

        i = 0

        while i < len(points.points)-1:

            pen.setColor(linecolor)
            pen.setWidth(self.lwidth)
            painter.setPen(pen)
            
            if self.plot.get_x_range() == 0:
                a_x1 = 0
                a_x2 = 0
            else:
                a_x1 = (points.points[i].x - self.plot.get_x_min())/self.plot.get_x_range()
                a_x2 = (points.points[i+1].x - self.plot.get_x_min())/self.plot.get_x_range()
            if self.plot.get_y_range() == 0:
                a_y1 = 0
                a_y2 = 0
            else:
                a_y1 = (points.points[i].y - self.plot.get_y_min())/self.plot.get_y_range()
                a_y2 = (points.points[i+1].y - self.plot.get_y_min())/self.plot.get_y_range()

            x1 = a_x1*self.width()*0.9 + self.width()*0.05
            y1 = self.height()*0.95 - a_y1*self.height()*0.8
            x2 = a_x2*self.width()*0.9 + self.width()*0.05
            y2 = self.height()*0.95 - a_y2*self.height()*0.8

            painter.drawLine(x1, y1, x2, y2)

            self.draw_ticks(painter, pen, x1, y1, points.points[i].x, points.points[i].y)

            i += 1
        
            
    '''           
    def randomize_color(self):

        # Method to randomize line colors 

        for i in range(len(self.plot.lines)):
            self.colors.append(QtGui.QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
'''
    def gridon(self):

        # Let user set grid on/off

        if self.grid == True:
            self.grid = False
        else:
            self.grid = True
        self.update()

    def grid_size(self):
        
        # Let user set grid square size

        size, ok = QtWidgets.QInputDialog.getText(self, 'Grid square size', 'Enter grid square size:')
        if size and ok:
            self.square_size = int(size)
        self.update()

    def labelnames(self):

        # Let user change x- and y-label names

        xname, ok = QtWidgets.QInputDialog.getText(self, 'X-label name', 'Enter name for X-label:')
        if xname and ok:
            self.xlab = xname
        yname, ok = QtWidgets.QInputDialog.getText(self, 'Y-label name', 'Enter name for Y-label:')
        if yname and ok:
            self.ylab = yname
        self.update()

        
    def show_numbers(self):

        # Let user choose to show  axis numbers or not (except maximum)

        if self.nos == True:
            self.nos= False
        else:
            self.nos = True
        self.update()


    def linewidth(self):

        # Let user change graph line width

        wdth, ok = QtWidgets.QInputDialog.getText(self, 'Line width', 'Enter line width as a integer:')
        if wdth and ok:
            self.lwidth = int(wdth)
        self.update()



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

        numberAction = QtWidgets.QAction('&ShowNumbers', self)
        numberAction.triggered.connect(self.show_numbers)
        toolbar.addAction(numberAction)

        widthAction = QtWidgets.QAction('&LineWidth', self)
        widthAction.triggered.connect(self.linewidth)
        toolbar.addAction(widthAction)

        bcolorAction = QtWidgets.QAction('&BackgroundColor', self)
        bcolorAction.triggered.connect(self.backgroundcolor)
        toolbar.addAction(bcolorAction)

        acolorAction = QtWidgets.QAction('&AxisColor', self)
        acolorAction.triggered.connect(self.axiscolor)
        toolbar.addAction(acolorAction)

        exitAction = QtWidgets.QAction('&Exit', self)
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        toolbar.addAction(exitAction)





    