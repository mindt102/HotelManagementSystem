from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from const import *
import login_qrc

class Login(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        loadUi("login.ui", self)
        
        # self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())