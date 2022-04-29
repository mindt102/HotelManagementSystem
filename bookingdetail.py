# This Python file uses the following encoding: utf-8
from imp import load_dynamic
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from RequestData import RequestData

class BookingDetails(QtWidgets.QWidget):
    def __init__(self, bookingId, *args, **kwargs):
        super(BookingDetails, self).__init__(*args, **kwargs)
        self.bookingId = bookingId
        loadUi("bookingdetail.ui", self)
        self.loadData()

    def loadData(self):
        data = RequestData.getBookingById(self.bookingId)
        _translate = QtCore.QCoreApplication.translate

        self.clientNameLabel.setText(_translate("BookingDetails", f"{data['clientName']}"))
        self.phoneNumberLabel.setText(_translate("BookingDetails", f"{data['clientNumber']}"))

if __name__ == "__main__":
    app = QApplication([])
    widget = BookingDetails(bookingId=1)
    widget.show()
    sys.exit(app.exec_())
