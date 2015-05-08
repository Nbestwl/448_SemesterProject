import sys
from PyQt4 import QtGui, QtCore
from imagedatabase import ImageDatabase
from controller import Controller

class Toolbar(QtGui.QWidget):

    def __init__(self,model,controller):
        super(Toolbar,self).__init__()
        self.model = model
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.resize(600,40)
        self.setFixedSize(600,40)
        self.setWindowTitle('ComicViewer Controls')

        self.btnSelect = QtGui.QPushButton('Select Comic',self)
        self.btnSelect.move(5,10)
        self.btnSelect.clicked.connect(self.controller.selectComic)

        self.btnPrevious = QtGui.QPushButton('Previous',self)
        self.btnPrevious.move(105,10)
        self.btnPrevious.clicked.connect(self.controller.prevPage)

        self.btnNext = QtGui.QPushButton('Next',self)
        self.btnNext.move(205,10)
        self.btnNext.clicked.connect(self.controller.nextPage)

        self.btnZoomIn = QtGui.QPushButton('Zoom in',self)
        self.btnZoomIn.move(305,10)
        self.btnZoomIn.clicked.connect(self.controller.zoomIn)

        self.btnZoomOut = QtGui.QPushButton('Zoom out',self)
        self.btnZoomOut.move(405,10)
        self.btnZoomOut.clicked.connect(self.controller.zoomOut)

        self.btnExit = QtGui.QPushButton('Exit',self)
        self.btnExit.move(505,10)
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

    def showDialog(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, 'Select Comic Folder')
        return directory

class ComicViewer(QtGui.QWidget):

    def __init__(self):
        super(ComicViewer,self).__init__()
        print('ComicViewer is now initialized')
        self.model = ImageDatabase()
        self.controller = Controller(self.model,self)        
        self.width = 6*175
        self.height = 4*175
        self.initUI()
 
    def initUI(self):
        self.resize(self.width,self.height)
        self.setWindowTitle('ComicViewer: Untitled')

        self.labelLeftPage = QtGui.QLabel('Left Page',self)
        self.labelLeftPage.resize(self.width*0.5,self.height)
        self.labelLeftPage.move(0,0)

        self.labelRightPage = QtGui.QLabel('Right Page',self)
        self.labelRightPage.resize(self.labelLeftPage.size())
        self.labelRightPage.move(self.labelLeftPage.width(),0)

        self.show()

        self.toolbar = Toolbar(self.model,self.controller)

    def setPixmap(self,leftImage,rightImage):

        # DEBUG
        self.leftPixmap = QtGui.QPixmap('an12/an12(1000)fc.jpg')
        self.leftPixmap = self.leftPixmap.scaled(self.labelLeftPage.size(), QtCore.Qt.KeepAspectRatio)
        # DEBUG
        self.rightPixmap = QtGui.QPixmap('an12/an12(1001).jpg')
        self.rightPixmap = self.rightPixmap.scaled(self.labelRightPage.size(), QtCore.Qt.KeepAspectRatio)

        self.labelLeftPage.setPixmap(self.leftPixmap)
        self.labelRightPage.setPixmap(self.rightPixmap)
        self.resize(self.labelLeftPage.width()*2,self.labelRightPage.height())

        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    comicViewer = ComicViewer()
    comicViewer.setPixmap('duck.jpg','stuff.jpg')

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
