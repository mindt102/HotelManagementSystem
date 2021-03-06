from PyQt5 import QtCore, QtWidgets
from dashboard import Dashboard 
from checking import Checking
from service import Services
from revenue import Revenue
from booking import Booking
from navbar import NavBar
from const import *
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Hotel Management System")
        self.setMinimumSize(CONTENT_WIDTH + NAVBAR_WIDTH, WINDOW_HEIGHT)
        self.initNavBar()
        self.initStackedWidget()
        self.initMainLayout()
        self.initNavBarBtns()
        self.initLogoutBtn()

    def loadUser(self, user):
        self.user = user
        _translate = QtCore.QCoreApplication.translate
        self.navbar.userLabel.setText(_translate("MainWindow", f"""<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#ffffff;">{user['firstName']} {user['lastName']}</span></p></body></html>"""))
    def initMainLayout(self):
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName("mainLayout")
        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.navbar, 0, 0, 1, 2)
        self.mainLayout.addWidget(self.stackedWidget, 0, 1, 1, 2)

    def initNavBar(self):
        self.navbar = NavBar()
    
    def initNavBarBtns(self):
        for i, btn in enumerate(self.navbar.findChildren(QtWidgets.QPushButton)):
            btn.clicked.connect(lambda t, i=i: self.loadPage(i))

    def loadPage(self, pageIndex):
        self.stackedWidget.setCurrentIndex(pageIndex)


    def initStackedWidget(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self)
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
        currIndex = self.stackedWidget.currentIndex()
        if currIndex == 0:
            self.dashboard.reload()
        elif currIndex == 2:
            self.checkin.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.checkin.reloadTable()
        elif currIndex == 3:
            self.checkout.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.checkout.reloadTable()
        elif currIndex == 4:
            self.revenue.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())
            self.revenue.reloadData()
        elif currIndex == 5:
            self.services.tabWidget.setCurrentIndex(0)
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
    
    def initLogoutBtn(self):
        self.close()
    
if __name__ == "__main__":
    from login import Login

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()

    loginWidget = Login(mainWindow=mainWindow)
    loginWidget.show()

    sys.exit(app.exec_())
