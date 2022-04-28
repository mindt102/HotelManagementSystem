from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Dashboard 
from booking import Booking
from navbar import NavBar
from revenue import Revenue
from example import Example
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

        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)

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

    def loadPage(self, pageIndex):
        # targetPage = self.stackedWidget.findChild(QtWidgets.QWidget,pageIndex)
        self.stackedWidget.setCurrentIndex(pageIndex)

    def initStackedWidget(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self)

        self.stackedWidget.setGeometry(QtCore.QRect(NAVBAR_WIDTH,0,CONTENT_WIDTH,WINDOW_HEIGHT))
        self.stackedWidget.setObjectName("stackedWidget")

        self.initDashboard()
        self.stackedWidget.addWidget(self.dashboard)
        
        self.initBooking()
        self.stackedWidget.addWidget(self.booking)

        self.initCheckin()
        self.stackedWidget.addWidget(self.checkin)

        self.initCheckout()
        self.stackedWidget.addWidget(self.checkout)

        self.initRevenue()
        self.stackedWidget.addWidget(self.revenue)

        self.initServices()
        self.stackedWidget.addWidget(self.services)

    def initDashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.setObjectName("dashboard")

    def initBooking(self): 
        self.booking = Booking()
        self.booking.setObjectName("booking")

        self.booking.cancelBtn.clicked.connect(lambda t: self.loadPage(0))

    def initCheckin(self):
        self.checkin = Example()
        self.checkin.setObjectName("checkin")

    def initCheckout(self):
        self.checkout = Example()
        self.checkout.setObjectName("checkout")
    
    def initRevenue(self):
        self.revenue = Revenue()
        self.revenue.setObjectName("revenue")
    
    def initServices(self):
        self.services = Example()
        self.services.setObjectName("services")
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
