from os import listdir
from os.path import isfile, join

class ImageDatabase:

    def __init__(self):
        print('Image Database initialized')

    def loadFolder(self, path):
        files = [ f for f in listdir(path) if isfile(join(path,f)) ]
        print(files)
