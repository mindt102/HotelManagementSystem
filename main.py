from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Dashboard 
from booking import Booking
from navbar import NavBar
from revenue import Revenue
from example import Example
from checking import Checking
from const import *
import sys

from service import Services

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
    
        self.stackedWidget.currentChanged.connect(self.changeWidget)

    def changeWidget(self):
        if self.stackedWidget.currentIndex() == 0:
            self.dashboard.reload()

    def initDashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.setObjectName("dashboard")

        self.dashboard.bookBtn.clicked.connect(lambda t: self.loadPage(1))
        self.dashboard.checkinBtn.clicked.connect(lambda t: self.loadPage(2))
        self.dashboard.checkoutBtn.clicked.connect(lambda t: self.loadPage(3))
        self.dashboard.revenueBtn.clicked.connect(lambda t: self.loadPage(4))

    def initBooking(self): 
        self.booking = Booking()
        self.booking.setObjectName("booking")

        self.booking.cancelBtn.clicked.connect(lambda t: self.loadPage(0))

    def initCheckin(self):
        self.checkin = Checking(1)
        self.checkin.setObjectName("checkin")

    def initCheckout(self):
        self.checkout = Checking(2)
        self.checkout.setObjectName("checkout")
    
    def initRevenue(self):
        self.revenue = Revenue()
        self.revenue.setObjectName("revenue")
    
    def initServices(self):
        self.services = Services()
        self.services.setObjectName("services")
        
    
if __name__ == "__main__":
    from login import Login

    app = QtWidgets.QApplication(sys.argv)
    loginWidget = Login()
    loginWidget.show()

    sys.exit(app.exec_())
