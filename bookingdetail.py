# This Python file uses the following encoding: utf-8
from pathlib import Path
import sys

#PySide2.QtWidgets   QApplication,QWidget,
#PySide2.QtCore
#PySide2.QtUiTools
        
from PyQt5 import QtWidgets, QtCore
#from PyQt5 import QFile
#from PyQt5 import QUiLoader
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from RequestData import RequestData

class BookingDetails(QtWidgets.QWidget):
    def __init__(self, bookingId, *args, **kwargs):
        super(BookingDetails, self).__init__(*args, **kwargs)
        self.bookingId = bookingId
        loadUi("bookingdetail.ui", self)
        self.loadData()
        # self.loadService()

    def loadData(self):
        data = RequestData.getBookingById(self.bookingId)
        # data["services"] = RequestData.getServicesByBookingId(self.bookingId)
        
        _translate = QtCore.QCoreApplication.translate
        
        # self.clientBookingIDLabel.setText(_translate("Booking", f"{data['id']}"))
        self.clientNameLabel.setText(_translate("BookingDetails", f"{data['clientName']}"))
        self.phoneNumberLabel.setText(_translate("BookingDetails", f"{data['clientNumber']}"))
        self.clientCheckInLabel.setText(_translate("BookingDetails", f"{data['checkinDate']}"))
        self.clientCheckOutLabel.setText(_translate("BookingDetails", f"{data['checkoutDate']}"))
        roomTypeStr = RequestData.getRoomTypeByRoomNumber(data["roomNumber"])
        self.bedTypeLabel.setText(_translate("BookingDetails", roomTypeStr))
        self.billLabel.setText(_translate("BookingDetails", f"${RequestData.getRevenueByBookingId(data['id'])}"))
        print(roomTypeStr)
        self.loadService()

    def loadService(self):
        services = RequestData.getServicesByBookingId(self.bookingId)
        # print(services)
        header = self.serviceTable.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.serviceTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        row = 0
        self.serviceTable.setRowCount(len(services))

        for service in services:
            print()
            print(service["status"])
            print(service["createdAt"])

        # rowPosition = self.clientTableService.setRowCount(self.order)
            serviceStr = RequestData.getServiceById(service["serviceId"])["title"]
            statusStr = "Pending" if service["status"] == 1 else "Done"
            
            self.serviceTable.setItem(row, 0, QtWidgets.QTableWidgetItem(serviceStr))
            self.serviceTable.setItem(row, 1, QtWidgets.QTableWidgetItem(service["createdAt"]))
            self.serviceTable.setItem(row, 2, QtWidgets.QTableWidgetItem(statusStr))
            row += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = BookingDetails(bookingId=3)
    widget.show()
    sys.exit(app.exec_())
