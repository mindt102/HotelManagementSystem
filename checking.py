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
        self.initSearchBtn()

    def initTitle(self):
        _translate = QtCore.QCoreApplication.translate
        statusStr = "CHECK IN TODAY" if self.status == 1 else "CHECK OUT TODAY"
        self.pageTitleLabel.setText(_translate("Form", statusStr))
    
    def initCheckButton(self):
        _translate = QtCore.QCoreApplication.translate

        if self.status == 1:
            self.checkBtn.setText(_translate("Form", "CHECK IN"))
            
        elif self.status == 2:
            self.checkBtn.setText(_translate("Form", "CHECK OUT"))
        self.checkBtn.clicked.connect(self.updateStatus)

    def getSelectedBookingId(self):
        if (self.tableWidget.currentRow() == -1):
            return
        return self.data[self.tableWidget.currentRow()]["id"]

    def updateStatus(self):
        bookingId = self.getSelectedBookingId()
        if self.status == 1:
            RequestData.checkin(bookingId)
        elif self.status == 2:
            RequestData.checkout(bookingId)
        self.reloadTable()
        self.showBookingDetails(bookingId)

    def initSearchBtn(self):
        self.searchBtn.clicked.connect(self.loadSearchResult)
    
    def loadSearchResult(self):
        self.clientName = self.searchInput.text()
        self.reloadTable()
        self.searchInput.setText("")

    def showBookingDetails(self, bookingId):
        if not bookingId:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("You have to choose a row first")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        self.bookingDetails = BookingDetails(bookingId)
        self.bookingDetails.show()

    def initTables(self):
        self.dateStr = "2022-05-04"
        self.clientName = ""

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.reloadTable()

    def addDataToTable(self):
        columns = ["clientName", "clientNumber", "roomNumber", "checkinDate", "checkoutDate"]
        self.tableWidget.setRowCount(len(self.data))
        
        row = 0
        for _ in range(len(self.data)):
            for item in self.data:
                for i in range(len(columns)):
                    self.tableWidget.setItem(row, i, QtWidgets.QTableWidgetItem(str(item[columns[i]])))
                row += 1

    def reloadTable(self):
        if self.status == 1:
            self.data = RequestData.getBookings(clientName=self.clientName, checkinDate=self.dateStr, status=self.status)
        elif self.status == 2:
            self.data = RequestData.getBookings(clentName=self.clientName, checkoutDate=self.dateStr, status=self.status)
        self.addDataToTable()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Checking(1)
    widget.show()
    sys.exit(app.exec_())