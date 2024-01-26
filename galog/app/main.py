from PyQt5.QtWidgets import *
from os.path import expanduser

def runApp():
    home_directory = expanduser('~')
    app = QApplication([])
    model = QDirModel()
    view = QTreeView()
    view.setModel(model)
    view.setRootIndex(model.index(home_directory))
    view.show()
    app.exec()
