from os import listdir
from os.path import isfile, join

class ImageDatabase:

    def __init__(self):
        print('Image Database initialized')
        self.Directory = None
        self.Images = []

    def selectFolder(self, path):
        self.Images = []
        self.Directory = path
        print('Folder select at {}'.format(path))
        #self.Images = self.loadFolder(path)

    def loadFolder(self, path):
        if path != None:
            files = [ f for f in listdir(path) if isfile(join(path,f)) ]
            print(files)
            return files
