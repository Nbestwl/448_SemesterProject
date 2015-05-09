from os import listdir
from os.path import isfile, join

class ImageDatabase:

    def __init__(self,view):
        print('Image Database initialized')
        self.view = view
        self.leftPage = 0
        self.rightPage = 1
        self.Images = []
        self.Directory = None

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

    def nextPage(self):
        self.leftPage += 2
        self.rightPage = self.leftPage + 1
        self.updateView()

    def prevPage(self):
        self.leftPage -= 2
        self.rightPage = self.leftPage + 1
        self.updateView()

    def updateView(self):
        self.view.setPixmap(self.Images[self.leftPage],self.Images[self.rightPage])
