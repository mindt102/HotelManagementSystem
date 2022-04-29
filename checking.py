from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from bookingdetail import BookingDetails
from RequestData import RequestData
from const import *
import datetime

class Checking(QtWidgets.QWidget):
    def __init__(self, status: int, *args, **kwargs):
        super(Checking, self).__init__(*args, **kwargs)
        loadUi("checking.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        self.status = status
        self.initTitle()
        self.initTables()
        self.initCheckButton()

    def initTitle(self):
        _translate = QtCore.QCoreApplication.translate
        statusStr = "Reservation" if self.status == 0 else "Guests"
        self.pageTitleLabel.setText(_translate("Form", statusStr))
    
    def initCheckButton(self):
        _translate = QtCore.QCoreApplication.translate

        if self.status == 0:
            self.checkBtn.setText(_translate("Form", "CHECK IN"))
        elif self.status == 1:
            self.checkBtn.setText(_translate("Form", "CHECK OUT"))
        self.checkBtn.clicked.connect(self.showBookingDetails)

    def getSelectedBookingId(self):
        print(self.tableWidget.currentRow())
        return self.data[self.tableWidget.currentRow()]["id"]

    #Event of button
    def showBookingDetails(self):
        bookingId = self.getSelectedBookingId()
        self.bookingDetails = BookingDetails(bookingId)
        self.bookingDetails.show()

    def initTables(self):
        table = self.tableWidget
        header = table.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.loadCheckinTable()

    def loadTable(self, table, columns: list[str]):
        table.setRowCount(len(self.data))
        
        row = 0
        for _ in range(len(self.data)):
            for item in self.data:
                for i in range(len(columns)):
                    table.setItem(row, i, QtWidgets.QTableWidgetItem(str(item[columns[i]])))
                row += 1

    def loadCheckinTable(self):
        dateStr = datetime.datetime.today().strftime("%Y-%m-%d")
        if self.status == 0:
            self.data = RequestData.getBookings(checkinDate=dateStr, status=self.status, sortBy="checkinTime")
            self.loadTable(self.tableWidget, ["clientName", "clientNumber", "roomNumber", "checkinTime"])
        elif self.status == 1:
            self.data = RequestData.getBookings(checkoutDate=dateStr, status=self.status, sortBy="checkoutTime")
            self.loadTable(self.tableWidget, ["clientName", "clientNumber", "roomNumber", "checkoutTime"])
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Checking(1)
    widget.show()
    sys.exit(app.exec_())