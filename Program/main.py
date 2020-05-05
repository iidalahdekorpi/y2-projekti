import sys
from PyQt5 import QtWidgets
from gui import GUI

def main():
    ''
    #file = input("Insert filename: \n")
    file = 'Program/esim.txt'
    global app
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    gui = GUI(file)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()