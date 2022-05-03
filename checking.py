from sqlite3 import DateFromTicks
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
from bookingdetail import BookingDetails
from RequestData import RequestData
from const import *
import datetime

class Checking(QtWidgets.QWidget):
    def __init__(self, status: int, *args, **kwargs):
        super(Checking, self).__init__(*args, **kwargs)
        loadUi("checking.ui", self)
        
        self.status = status
        self.initTitle()
        self.initCheckButton()
        self.initSearchBtn()
        self.initDateEdit()
        self.initTables()

    def initTitle(self):
        _translate = QtCore.QCoreApplication.translate
        statusStr = "Reservations" if self.status == 1 else "CURRENT GUESTS"
        self.pageTitleLabel.setText(_translate("Form", statusStr))
    
    def initCheckButton(self):
        _translate = QtCore.QCoreApplication.translate

        if self.status == 1:
            self.checkBtn.setText(_translate("Form", "CHECK IN"))
            self.checkBtn.setIcon(QtGui.QIcon('.\images\in-32.png'))
            
        elif self.status == 2:
            self.checkBtn.setText(_translate("Form", "CHECK OUT"))
            self.checkBtn.setIcon(QtGui.QIcon('.\images\out-32.png'))
        self.checkBtn.clicked.connect(self.updateStatus)

    def initDateEdit(self):
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.dateChanged.connect(self.dateChangedHandler) 

    def getSelectedBookingId(self):
        if (self.tableWidget.currentRow() == -1):
            return
        selectedRow = self.tableWidget.currentRow()
        result = self.tableWidget.item(selectedRow, 0).data(QtCore.Qt.UserRole)
        return result

    def updateStatus(self):
        bookingId = self.getSelectedBookingId()
        self.showBookingDetails(bookingId)
        self.reloadTable()

    def initSearchBtn(self):
        self.searchBtn.clicked.connect(self.loadSearchResult)
    
    def loadSearchResult(self):
        self.clientName = self.searchInput.text().title()
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
        self.bookingDetails.btn.clicked.connect(self.reloadTable)
        self.bookingDetails.show()
    
    def initTables(self):
        self.dateStr = datetime.datetime.today().strftime("%Y-%m-%d")
        self.clientName = ""

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.reloadTable()

    def addDataToTable(self):
        columns = ["clientName", "clientNumber", "roomNumber", "checkinDate", "checkoutDate"]
        self.tableWidget.setRowCount(len(self.data))
        
        row = 0
        for item in self.data:
            for i in range(len(columns)):
                self.tableWidget.setItem(row, i, QtWidgets.QTableWidgetItem(str(item[columns[i]])))
            self.tableWidget.item(row, 0).setData(QtCore.Qt.UserRole, item["id"])
            row += 1
            
    def reloadTable(self):
        if self.status == 1:
            self.data = RequestData.getBookings(clientName=self.clientName, checkinDate=self.dateStr, status=self.status)
        elif self.status == 2:
            self.data = RequestData.getBookings(clientName=self.clientName, checkoutDate=self.dateStr, status=self.status)
        self.addDataToTable()

    def dateChangedHandler(self):
        self.dateStr = self.dateEdit.date().toString("yyyy-MM-dd")
        self.reloadTable()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Checking(1)
    widget.show()
    sys.exit(app.exec_())