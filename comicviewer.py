import sys
from PyQt4 import QtGui, QtCore

class Toolbar(QtGui.QWidget):

    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(600,40)
        self.setFixedSize(600,40)
        self.setWindowTitle('ComicViewer Controls')

        self.btnReload = QtGui.QPushButton('Reload',self)
        self.btnReload.move(5,10)

        self.btnPrevious = QtGui.QPushButton('Previous',self)
        self.btnPrevious.move(105,10)

        self.btnNext = QtGui.QPushButton('Next',self)
        self.btnNext.move(205,10)

        self.btnZoomIn = QtGui.QPushButton('Zoom in',self)
        self.btnZoomIn.move(305,10)

        self.btnZoomOut = QtGui.QPushButton('Zoom out',self)
        self.btnZoomOut.move(405,10)

        self.btnExit = QtGui.QPushButton('Exit',self)
        self.btnExit.move(505,10)

        self.show()

class ComicViewer(QtGui.QWidget):

    def __init__(self):
        super(ComicViewer,self).__init__()
        print('ComicViewer is now initialized')
        self.width = 400
        self.height = 800
        self.initUI()
 
    def initUI(self):
        self.resize(self.width,self.height)
        self.setWindowTitle('ComicViewer: Untitled')
        self.show()

        self.labelImage = QtGui.QLabel('Image',self)
        self.labelImage.resize(self.width,self.height)
        self.labelImage.move(0,0)
        self.labelImage.show()

        self.toolbar = Toolbar()

    def setPixmap(self,image):
        pixmap = QtGui.QPixmap('duck.jpg')
        pixmap.scaledToWidth(self.width)
        pixmap.scaledToHeight(self.height)
        self.labelImage.setPixmap(pixmap)
        sizeHint = self.labelImage.sizeHint()
        self.labelImage.resize(sizeHint)
        self.resize(sizeHint)

def main():
    app = QtGui.QApplication(sys.argv)
    comicViewer = ComicViewer()
    comicViewer.setPixmap('duck.jpg')

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
