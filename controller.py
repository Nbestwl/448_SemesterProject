class Controller:

    def __init__(self,model,view):
        print('Controller initialized')
        self.model = model
        self.view = view

    def selectComic(self):
        print('selectComic()')
        comicDir = self.view.toolbar.showDialog()
        if comicDir != None:
            print(comicDir)
            self.model.selectFolder(comicDir)

    def nextPage(self):
        print('nextPage()')

    def prevPage(self):
        print('prevPage()')

    def zoomIn(self):
        print('zoomIn()')

    def zoomOut(self):
        print('zoomOut()')
