import sys
from PyQt5 import QtWidgets
from gui import GUI

def main():
    ''
    file = input("Insert filename: \n")
    #file = 'Program/esim.txt'
    type = input("Insert graph type (line/pie/column): \n")
    #type = 'line'
    global app
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    gui = GUI(file, type)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()