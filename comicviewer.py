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

        self.btnReload = QtGui.QPushButton('Select Comic',self)
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
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

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

        self.labelLeftPage = QtGui.QLabel('Left Page',self)
        self.labelLeftPage.resize(self.width*0.25,self.height*0.5)
        self.labelLeftPage.move(0,0)

        self.labelRightPage = QtGui.QLabel('Right Page',self)
        self.labelRightPage.resize(self.width*0.25,self.height*0.5)
        self.labelRightPage.move(3*self.width,0)

        self.show()

        self.toolbar = Toolbar()

    def setPixmap(self,leftImage,rightImage):
        # DEBUG
        self.leftPixmap = QtGui.QPixmap('an12/an12(1000)fc.jpg')
        self.leftPixmap = self.leftPixmap.scaled(200, QtCore.Qt.KeepAspectRatio)
        # DEBUG
        self.rightPixmap = QtGui.QPixmap('an12/an12(1001).jpg')
        self.rightPixmap = self.rightPixmap.scaled(200, QtCore.Qt.KeepAspectRatio)
        self.rightPixmap.scaledToWidth(self.width*0.5)
        self.rightPixmap.scaledToHeight(self.height*0.5)

        self.labelLeftPage.setPixmap(self.leftPixmap)
        self.labelRightPage.setPixmap(self.rightPixmap)
        leftSizeHint = self.labelLeftPage.sizeHint()
        rightSizeHint = self.labelRightPage.sizeHint()
        self.labelLeftPage.resize(leftSizeHint)
        self.labelRightPage.resize(rightSizeHint)
        self.resize(leftSizeHint + rightSizeHint)


def main():
    app = QtGui.QApplication(sys.argv)
    comicViewer = ComicViewer()
    comicViewer.setPixmap('duck.jpg','stuff.jpg')

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
