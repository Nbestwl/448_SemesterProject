import sys
from PyQt4 import QtGui, QtCore

class Toolbar(QtGui.QWidget):

    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,400)
        self.setFixedSize(300,400)
        self.setWindowTitle('Viewer Controls')
        self.show()

class ComicViewer:

    def __init__(self):
        print('ComicViewer is now initialized')
        self.initUI()
 
    def initUI(self):
        self.viewer = QtGui.QMainWindow()
        self.viewer.resize(800,350)
        self.viewer.setWindowTitle('ComicViewer: Untitled')
        self.viewer.show()

        self.toolbar = Toolbar()

def main():
    app = QtGui.QApplication(sys.argv)
    comicViewer = ComicViewer()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
