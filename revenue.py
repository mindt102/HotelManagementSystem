import json
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from const import *
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QWidget, QCalendarWidget, QLabel
from RequestData import RequestData
from bookingdetail import BookingDetails

class Revenue(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Revenue, self).__init__(*args, **kwargs)
        loadUi("revenue.ui", self)

        self.initTable()
        self.reloadData()

        #Connect calendar to the function
        self.calendarWidget.selectionChanged.connect(self.reloadData)
        self.detailsBtn.clicked.connect(self.showBookingDetails)

    def initTable(self):
        header = self.table_Revenue.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def reloadData(self):
        _translate = QtCore.QCoreApplication.translate

        self.date = self.calendarWidget.selectedDate()
        self.calendarLabel.setText(_translate("Revenue", self.date.toString()))
        self.loadData()

    def loadData(self):
        self.data = RequestData.getRevenueByDate(self.date.toString("yyyy-MM-dd"))
        row = 0
        self.table_Revenue.setRowCount(len(self.data))
        for item in self.data:
            self.table_Revenue.setItem(row, 0, QtWidgets.QTableWidgetItem(item["clientName"]))
            self.table_Revenue.setItem(row, 1, QtWidgets.QTableWidgetItem(str(item['roomNumber'])))
            self.table_Revenue.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item['roomFee'])))
            self.table_Revenue.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item['serviceFee'])))
            self.table_Revenue.setItem(row, 4, QtWidgets.QTableWidgetItem(str(item['totalBill'])))
            
            self.table_Revenue.item(row, 0).setData(QtCore.Qt.UserRole, item["bookingId"])
            
            row = row + 1
        
    def getSelectedBookingId(self):
        if (self.table_Revenue.currentRow() == -1):
            return
        selectedRow = self.table_Revenue.currentRow()
        result = self.table_Revenue.item(selectedRow, 0).data(QtCore.Qt.UserRole)
        return result

    #Event of button
    def showBookingDetails(self):
        bookingId = self.getSelectedBookingId()
        self.bookingDetails = BookingDetails(bookingId)
        self.bookingDetails.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rev = Revenue()
    widget = Revenue()
    widget.show()
    sys.exit(app.exec_())