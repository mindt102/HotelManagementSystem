from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from const import *

class Checking(QtWidgets.QWidget):
    def __init__(self, status: int, *args, **kwargs):
        super(Checking, self).__init__(*args, **kwargs)
        loadUi("checking.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        self.status = status
        self.initTitle()
        self.initTables()

    def initTitle(self):
        _translate = QtCore.QCoreApplication.translate
        statusStr = "Reservation" if self.status == 0 else "Guests"
        self.pageTitleLabel.setText(_translate("Form", statusStr))
    
    

    def initTables(self):
        table = self.tableWidget
        header = table.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.loadCheckinTable()

    def loadTable(self, table, data: dict, columns: list[str]):
        table.setRowCount(len(data))
        
        row = 0
        for _ in range(5):
            for item in data:
                for i in range(len(columns)):
                    table.setItem(row, i, QtWidgets.QTableWidgetItem(str(item[columns[i]])))
                row += 1

    def loadCheckinTable(self):
        data = [
            {
            "checkinTime": "2022-04-23T07:23:54.638Z",
            "clientName": "Nguyễn Tiến Công",
            "clientNumber": "0901234567",
            "roomNumber": 201,
            },
            {
            "checkinTime": "2022-04-23T07:23:54.638Z",  
            "clientName": "Nguyễn Việt Hưng",
            "clientNumber": "0901234567",
            "roomNumber": 202,
            },
        ]
        self.loadTable(self.tableWidget, data, ["checkinTime", "clientName", "clientNumber","roomNumber"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Checking(1)
    widget.show()
    sys.exit(app.exec_())