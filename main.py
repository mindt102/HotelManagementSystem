from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from dashboard import Dashboard 
from navbar import NavBar
from const import *
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Hotel Management System")

        self.initMainLayout()
        self.initStackedWidget()
        self.initNavBar()

        self.setFixedSize(CONTENT_WIDTH + NAVBAR_WIDTH, WINDOW_HEIGHT)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.mainLayout.addWidget(self.stackedWidget)
    
    def initMainLayout(self):
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")

    def initNavBar(self):
        self.navbar = NavBar()
        self.mainLayout.addWidget(self.navbar)

        for i, btn in enumerate(self.navbar.findChildren(QtWidgets.QPushButton)):
            btn.clicked.connect(lambda t, i=i: self.loadPage(i))

    def loadPage(self, pageName):
        # targetPage = self.stackedWidget.findChild(QtWidgets.QWidget,pageName)
        self.stackedWidget.setCurrentIndex(pageName)

    def initStackedWidget(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self)

        self.stackedWidget.setGeometry(QtCore.QRect(NAVBAR_WIDTH,0,CONTENT_WIDTH,WINDOW_HEIGHT))
        self.stackedWidget.setObjectName("stackedWidget")

        self.initDashboard()
        self.stackedWidget.addWidget(self.dashboard)




    def initDashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.setObjectName("dashboard")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())