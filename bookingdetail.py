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
        data["services"] = RequestData.getServicesByBookingId(self.bookingId)
        
        _translate = QtCore.QCoreApplication.translate
        
        # self.clientBookingIDLabel.setText(_translate("Booking", f"{data['id']}"))
        self.clientNameLabel.setText(_translate("BookingDetails", f"{data['clientName']}"))
        self.phoneNumberLabel.setText(_translate("BookingDetails", f"{data['clientNumber']}"))
        self.clientCheckInLabel.setText(_translate("BookingDetails", f"{data['checkinDate']}"))
        self.clientCheckOutLabel.setText(_translate("BookingDetails", f"{data['checkoutDate']}"))

    # def loadService(self):
    #     order = RequestData.getBookingServiceByOrderID(self.order)
    #     _translate = QtCore.QCoreApplication.translate
        
    #     row = 0
    #     rowPosition = self.clientTableService.setRowCount(self.order)
    #     self.clientTableService.setItem(row, 0, QtWidgets.QTableWidgetItem(str(order["orderId"])))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = BookingDetails(bookingId=1, order=1)
    widget.show()
    sys.exit(app.exec_())
