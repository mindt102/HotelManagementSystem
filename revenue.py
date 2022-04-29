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
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        #set length of columns in table
        self.table_Revenue.setColumnWidth(0,225)
        self.table_Revenue.setColumnWidth(1,135)
        self.table_Revenue.setColumnWidth(2,135)
        self.table_Revenue.setColumnWidth(3,135)
        self.table_Revenue.setColumnWidth(4,135)

        self.reloadData()

        #Connect calendar to the function
        self.calendarWidget.selectionChanged.connect(self.reloadData)
        self.detailsBtn.clicked.connect(self.showBookingDetails)

    
    def reloadData(self):
        _translate = QtCore.QCoreApplication.translate

        self.date = self.calendarWidget.selectedDate()
        self.calendarLabel.setText(_translate("Revenue", self.date.toString()))
        self.loadData()

    def loadData(self):
        # data = [{'booking id':'777' ,'name':"Cristiano Ronaldo",'room_num':201,'room_fee': 200, 'services_fee':200},
        # {'booking id': '10','name': 'Lionel Messi', 'room_num':202,'room_fee':200,'services_fee':200},
        # {'booking id': '9','name': 'Zlatan Imbrahimovic', 'room_num': 203, 'room_fee':400, 'services_fee': 450}]
        self.data = RequestData.getRevenueByDate(self.date.toString("yyyy-MM-dd"))
        row = 0
        self.table_Revenue.setRowCount(len(self.data))
        for i in range(len(self.data)):
            #self.table_Revenue.setItem(row, -1, QtWidgets.QTableWidgetItem(str(self.data[i]["booking id"])))
            self.table_Revenue.setItem(row, 0, QtWidgets.QTableWidgetItem(self.data[i]["clientName"]))
            self.table_Revenue.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.data[i]['roomNumber'])))
            self.table_Revenue.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.data[i]['roomFee'])))
            self.table_Revenue.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.data[i]['serviceFee'])))
            self.table_Revenue.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.data[i]['totalBill'])))
            row = row + 1
        
    def getSelectedBookingId(self):
        return self.data[self.table_Revenue.currentRow()]["bookingId"]

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