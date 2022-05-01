from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from RequestData import RequestData
from const import *
from main import MainWindow
import login_qrc

class Login(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        loadUi("login.ui", self)
        self.setWindowTitle("Hotel Management System")
        self.loginBtn.clicked.connect(self.authenticate)
        self.setFixedSize(935, 806)
        # self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
    
    def authenticate(self):
        username = self.username.text()
        password = self.password.text()

        self.username.setText("")
        self.password.setText("")

        print(self.username.text())
        print(self.password.text())
        res = RequestData.login(username=username, password=password)
        if (not res["isError"]):
            self.close()
            widget = MainWindow()
            widget.show()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Invalid username or password")
            msg.setWindowTitle("Wrong Credentials")
            msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())