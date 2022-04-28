from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from const import *

class Example(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        loadUi("example.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Example()
    widget.show()
    sys.exit(app.exec_())