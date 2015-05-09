from os import listdir
from os.path import isfile, join

class ImageDatabase:

    def __init__(self,view):
        print('Image Database initialized')
        self.view = view
        self.leftPage = 0
        self.rightPage = 1
        self.magnification = 1.0
        self.Images = []
        self.Directory = None

    # Selects folder for a set of images
    def selectFolder(self, path):
        self.leftPage = 0
        self.rightPage = 1
        self.Images = []
        self.Directory = path
        print('Folder select at {}'.format(path))
        # Typecast to utilize String.endswith() method
        self.Images = self.loadFolder(str(path))
        self.updateView()

    # Returns all the absolute filepaths of all images in path
    def loadFolder(self, path):
        if path != None:
            files = [ join(path,f) for f in listdir(path) if isfile(join(path,f)) and f.endswith('.jpg') ]
            files.sort()
            print(files)
            return files

    # Selects images in an incrementing behavior
    def nextPage(self):
        if len(self.Images) > 0:
            self.leftPage += 1
            # Left Page incrementing with consideration to boundary
            if self.leftPage > len(self.Images)-1:
                self.leftPage = 0

            # Right Page incrementing with consideration to boundary
            if self.leftPage == len(self.Images)-1:
                self.rightPage = 0
            else:
                self.rightPage = self.leftPage + 1
            self.updateView()

    # Selects images in a decrementing behavior
    def prevPage(self):
        if len(self.Images) > 0:
            self.leftPage -= 1
            # Left Page decrementing with conisderation to boundary
            if self.leftPage < 0:
                self.leftPage = len(self.Images)-1
        
            if self.leftPage == len(self.Images)-1:
                self.rightPage = 0
            else:
                self.rightPage = self.leftPage + 1
            self.updateView()

    # Enlargens image
    def zoomIn(self):
        self.magnification += 0.1
        self.view.zoom(self.magnification) 
        self.updateView()

    # Shrinks image
    def zoomOut(self):
        if self.magnification - 0.1 > 0.5:
            self.magnification -= 0.1
            self.view.zoom(self.magnification)
            self.updateView()
        else:
            print('Cannot zoom out any further')

    # Updates the view with new current images
    def updateView(self):
        if len(self.Images) > 0:
            self.view.setPixmap(self.Images[self.leftPage],self.Images[self.rightPage])


