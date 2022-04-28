from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from const import *
import login_qrc

class Login(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        loadUi("login.ui", self)
        self.loginBtn.clicked.connect(self.authenticate)
        
        # self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
    
    def authenticate(self):
        user = {
            "username": "abc",
            "password": "123"

        }
        username = self.username.text()
        password = self.password.text()

        self.username.setText("")
        self.password.setText("")

        print(self.username.text())
        print(self.password.text())
        if ( username == user["username"] and password == user["password"]):
            print("Correct")
        else:
            print("Wrong")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())