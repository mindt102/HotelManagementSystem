from const import CONTENT_WIDTH, WINDOW_HEIGHT
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from const import *
import sys
import datetime
import json

class Dashboard(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Dashboard, self).__init__(*args, **kwargs)
        loadUi("dashboard.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        
        self.setWindowTitle("Dashboard")
        self.initStatsFrame()
        self.updateUpcomingFrame(self.arrivalsListFrame, "a")
        self.updateUpcomingFrame(self.departuresListFrame, "d")
    
    def initStatsFrame(self):
        for child in self.statsFrame.children():
            if isinstance(child, QtWidgets.QFrame):
                child.setStyleSheet(
                """ border-width: 1;
                    border-style: none;
                    border-radius: 10;
                    background-color: white;
                """     
                )
                childBtn = child.findChild(QtWidgets.QPushButton)
                childBtn.setStyleSheet(
                    """
                    QPushButton:hover{
                        background-color: #eeeeee
                    }""")
    def updateUpcomingFrame(self, frame: QtWidgets.QFrame, prefix: str):
        with open(DATAPATH + "upcoming.json", "r", encoding="utf8") as f:
            data = json.load(f) 

        _translate = QtCore.QCoreApplication.translate
        for i in range(1, 6):
            infos = data[i - 1]
            
            bookingId = infos["bookingId"]
            name = infos["clientName"]
            checkinTime = datetime.datetime.fromisoformat(infos["checkinTime"].replace("Z", "+00:00")).strftime("%d %b")
            checkoutTime = datetime.datetime.fromisoformat(infos["checkoutTime"].replace("Z", "+00:00")).strftime("%d %b")
            roomNum = infos["roomNumber"]

            dName = frame.findChild(QtWidgets.QLabel, prefix + f"Name_{i}")
            dInfo = frame.findChild(QtWidgets.QLabel, prefix + f"Info_{i}")
            dBut = frame.findChild(QtWidgets.QPushButton, prefix + f"But_{i}")
            
            dName.setText(_translate("Dashboard", f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">{name}</span></p></body></html>"))
            dInfo.setText(_translate("Dashboard", f"Room {roomNum}: {checkinTime} - {checkoutTime}"))

            dBut.clicked.connect(lambda ch, bId=bookingId: self.loadBookingInfo(bId))
            dBut.setStyleSheet("""QPushButton:hover{background-color: #eeeeee}""")
            butSP = dBut.sizePolicy()
            butSP.setVerticalPolicy(QtWidgets.QSizePolicy.Preferred)
            dBut.setSizePolicy(butSP)
    
    def loadBookingInfo(self, bookingId):
        print(bookingId)

    # def initTables(self):
    #     for table in (self.checkinTable, self.checkoutTable):
    #         header = table.horizontalHeader()       
    #         header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    #         header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    #         header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    #         header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

    #         table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    #     self.loadCheckinTable()
    #     self.loadCheckoutTable()

    # def loadTable(self, table, data: dict, columns: list[str]):
    #     table.setRowCount(len(data))
        
    #     row = 0
    #     for _ in range(5):
    #         for item in data:
    #             for i in range(len(columns)):
    #                 table.setItem(row, i, QtWidgets.QTableWidgetItem(str(item[columns[i]])))
    #             row += 1

    # def loadCheckinTable(self):
    #     data = [
    #         {
    #         "checkinTime": "2022-04-23T07:23:54.638Z",
    #         "roomNumber": 201,
    #         "clientName": "Nguyễn Tiến Công",
    #         "clientNumber": "0901234567",
    #         },
    #         {
    #         "checkinTime": "2022-04-23T07:23:54.638Z",
    #         "roomNumber": 202,
    #         "clientName": "Nguyễn Việt Hưng",
    #         "clientNumber": "0901234567",
    #         },
    #     ]
    #     self.loadTable(self.checkinTable, data, ["checkinTime", "roomNumber", "clientName", "clientNumber"])
        
    # def loadCheckoutTable(self):
        # data = [
        #     {
        #     "checkinTime": "2022-04-23T07:23:54.638Z",
        #     "roomNumber": 201,
        #     "clientName": "Nguyễn Tiến Công",
        #     "clientNumber": "0901234567",
        #     },
        #     {
        #     "checkinTime": "2022-04-23T07:23:54.638Z",
        #     "roomNumber": 202,
        #     "clientName": "Nguyễn Việt Hưng",
        #     "clientNumber": "0901234567",
        #     },
        # ]
        # self.loadTable(self.checkoutTable, data, ["checkinTime", "roomNumber", "clientName", "clientNumber"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Dashboard()
    widget.show()
    sys.exit(app.exec_())