# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

class BookingDetails(QtWidgets.QWidget):
    def __init__(self, bookingId, *args, **kwargs):
        super(BookingDetails, self).__init__(*args, **kwargs)
        # self.load_ui()
        loadUi("bookingdetail.ui", self)
        self.loadData(bookingId)

    def loadData(self, bookingId):
        data = {
            "id": 1,
            "clientName": "Shayne Feest",
            "clientNumber": "0933505646",
            "checkinDate": "2022-04-12",
            "checkoutDate": "2022-04-18",
            "checkinTime": "12:24:45",
            "checkoutTime": "14:42:18",
            "createdAt": "2022-03-01T11:16:34Z",
            "status": 3,
            "roomNumber": 200
        }
        _translate = QtCore.QCoreApplication.translate

        self.clientNameLabel.setText(_translate("BookingDetails", f"{data['clientName']}"))
        self.phoneNumberLabel.setText(_translate("BookingDetails", f"{data['clientNumber']}"))
            

            

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "bookingdetail.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = BookingDetails(bookingId=1)
    widget.show()
    sys.exit(app.exec_())
