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
        self.model.nextPage()

    def prevPage(self):
        print('prevPage()')
        self.model.prevPage()

    def zoomIn(self):
        print('zoomIn()')
        self.model.zoomIn()

    def zoomOut(self):
        print('zoomOut()')
        self.model.zoomOut()
