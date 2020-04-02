import sys
from PyQt5 import QtWidgets
from gui import GUI

def main():
    
    file = input("Inset filename: \n")
    global app
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI(file)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
