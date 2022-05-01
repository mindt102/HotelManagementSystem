from RequestData import RequestData
from const import CONTENT_WIDTH, WINDOW_HEIGHT
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from const import *
import sys
import datetime
import json

class Dashboard(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Dashboard, self).__init__(*args, **kwargs)
        loadUi("dashboard.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        
        self.setWindowTitle("Dashboard")
        self.initStatsFrame()
        
        self.reload()
    
    def reload(self):
        self.updateUpcomingFrame(RequestData.getUpcomingArrivals(), self.arrivalsListFrame, "a")
        self.updateUpcomingFrame(RequestData.getUpcomingDeparture(), self.departuresListFrame, "d")
        self.updateStats()
    
    def updateStats(self):
        _translate = QtCore.QCoreApplication.translate
        dateString = datetime.datetime.today().strftime("%Y-%m-%d")
        self.totalArrivalLabel.setText(_translate("Dashboard", str(RequestData.getTotalCheckinByDate(dateString))))
        self.totalDepartureLabel.setText(_translate("Dashboard", str(RequestData.getTotalCheckoutByDate(dateString))))
        self.totalBookingLabel.setText(_translate("Dashboard", str(RequestData.getTotalBookingByDate(dateString))))
        self.totalRevenueLabel.setText(_translate("Dashboard", str(RequestData.getTotalRevenueByDate(dateString))))

    def initStatsFrame(self):
        for child in self.statsFrame.children():
            if isinstance(child, QtWidgets.QFrame):
                child.setStyleSheet(
                """ border-width: 1;
                    border-style: none;
                    border-radius: 10;
                    background-color: white;
                """     
                )
                childBtn = child.findChild(QtWidgets.QPushButton)
                childBtn.setStyleSheet(
                    """
                    QPushButton:hover{
                        background-color: #eeeeee
                    }""")
    
    def updateUpcomingFrame(self, data: list, frame: QtWidgets.QFrame, prefix: str):
        _translate = QtCore.QCoreApplication.translate
        for i in range(1, 6):
            infos = data[i - 1]
            
            bookingId = infos["bookingId"]
            name = infos["clientName"]
            checkinTime = datetime.datetime.fromisoformat(infos["checkinTime"].replace("Z", "+00:00")).strftime("%d %b")
            checkoutTime = datetime.datetime.fromisoformat(infos["checkoutTime"].replace("Z", "+00:00")).strftime("%d %b")
            roomNum = infos["roomNumber"]

            dName = frame.findChild(QtWidgets.QLabel, prefix + f"Name_{i}")
            dInfo = frame.findChild(QtWidgets.QLabel, prefix + f"Info_{i}")
            dBut = frame.findChild(QtWidgets.QPushButton, prefix + f"But_{i}")
            
            dName.setText(_translate("Dashboard", f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">{name}</span></p></body></html>"))
            dInfo.setText(_translate("Dashboard", f"Room {roomNum}: {checkinTime} - {checkoutTime}"))

            dBut.clicked.connect(lambda ch, bId=bookingId: self.loadBookingInfo(bId))
            dBut.setStyleSheet("""QPushButton:hover{background-color: #eeeeee}""")
            butSP = dBut.sizePolicy()
            butSP.setVerticalPolicy(QtWidgets.QSizePolicy.Preferred)
            dBut.setSizePolicy(butSP)
    
    def loadBookingInfo(self, bookingId):
        # print(bookingId)
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Dashboard()
    widget.show()
    sys.exit(app.exec_())