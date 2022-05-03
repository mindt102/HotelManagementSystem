# This Python file uses the following encoding: utf-8
from pathlib import Path
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from RequestData import RequestData

class BookingDetails(QtWidgets.QWidget):
    def __init__(self, bookingId, *args, **kwargs):
        super(BookingDetails, self).__init__(*args, **kwargs)
        self.setWindowTitle("Details")
        self.bookingId = bookingId
        loadUi("bookingdetail.ui", self)
        self.loadData()
        self.initBtn()

    def loadData(self):
        self.booking = RequestData.getBookingById(self.bookingId)
        
        _translate = QtCore.QCoreApplication.translate
        
        self.clientNameLabel.setText(_translate("BookingDetails", f"{self.booking['clientName']}"))
        self.phoneNumberLabel.setText(_translate("BookingDetails", f"{self.booking['clientNumber']}"))
        self.clientCheckInLabel.setText(_translate("BookingDetails", f"{self.booking['checkinDate']}"))
        self.clientCheckOutLabel.setText(_translate("BookingDetails", f"{self.booking['checkoutDate']}"))
        roomTypeStr = RequestData.getRoomTypeByRoomNumber(self.booking["roomNumber"])['type']
        roomNumStr = str(self.booking["roomNumber"])
        
        statusStr = "Booked"
        billStr = ""
        if self.booking["status"] == 2:
            statusStr = "Checked In"
            billStr = f"Current Bill: ${RequestData.getRevenueByBookingId(self.booking['id'])}"
        elif self.booking["status"] == 3:
            statusStr = "Checked Out"
            billStr = f"Total: ${RequestData.getRevenueByBookingId(self.booking['id'])}"

        self.bedTypeLabel.setText(_translate("BookingDetails", f"No. {roomNumStr} - {roomTypeStr}"))
        self.statusLabel.setText(_translate("BookingDetails", statusStr))
        self.billLabel.setText(_translate("BookingDetails", billStr))
        self.loadService()

    def loadService(self):
        self.services = RequestData.getServiceOrdersByBookingId(self.bookingId)

        header = self.serviceTable.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.serviceTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        row = 0
        self.serviceTable.setRowCount(len(self.services))

        for service in self.services:
            serviceStr = RequestData.getServiceById(service["serviceId"])["title"]
            statusStr = "Pending" if service["status"] == 1 else "Done"
            
            self.serviceTable.setItem(row, 0, QtWidgets.QTableWidgetItem(serviceStr))
            self.serviceTable.setItem(row, 1, QtWidgets.QTableWidgetItem(service["createdAt"]))
            self.serviceTable.setItem(row, 2, QtWidgets.QTableWidgetItem(statusStr))
            row += 1

    def initBtn(self):
        status = self.booking["status"]
        if status == 1:
            btnText = "CHECK IN"
            btnFunc = self.checkinHandler
        elif status == 2:
            btnText = "CHECK OUT"
            btnFunc = self.checkoutHandler
        else:
            btnText = "DONE"
            btnFunc = lambda: self.close()
        self.btn.setText(btnText)
        self.btn.clicked.connect(btnFunc)
    
    def checkinHandler(self):
        RequestData.checkin(self.bookingId)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Check in successfully")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.close()

    def checkoutHandler(self):
        RequestData.checkout(self.bookingId)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Check out successfully")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = BookingDetails(bookingId=3)
    widget.show()
    sys.exit(app.exec_())
