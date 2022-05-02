from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from RequestData import RequestData
from const import *

class Services(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Services, self).__init__(*args, **kwargs)
        loadUi("service.ui", self)
        
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        self.services = RequestData.getServices()
        self.initTabWidget()
        self.initBtns()
        self.initPendingTable()
        self.initHistoryTable()
        self.dateEdit.dateChanged.connect(self.reloadData)


    def initBtns(self):
        self.orderBtn.clicked.connect(self.orderService)
        self.finishBtn.clicked.connect(self.finishHandler)

    def initTabWidget(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tabWidgetChangedHandler)

    def initPendingTable(self):
        header = self.pendingTable.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initHistoryTable(self):
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        header = self.historyTable.horizontalHeader()       
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.reloadData()

    def tabWidgetChangedHandler(self):
        currentIndex = self.tabWidget.currentIndex()
        if currentIndex == 1:
            self.reloadPendingTable()

    def orderService(self):
        roomNum = self.roomNumInput.text()
        serviceSelected = self.serviceOption.currentIndex() + 1
        note = self.noteInput.toPlainText()

        orderData = {
            "roomNumber": roomNum,
            "serviceId": serviceSelected,
            "note": note
        }

        RequestData.createServiceOrder(orderData=orderData)

        self.roomNumInput.setText("")
        self.serviceOption.setCurrentIndex(-1)
        self.noteInput.setText("")

        self.tabWidget.setCurrentIndex(1)
    
    def reloadPendingTable(self):
        self.pendingOrders = RequestData.getTodayOrdersByStatus(2)
        row = 0
        self.pendingTable.setRowCount(len(self.pendingOrders))
        for i in range(len(self.pendingOrders)):
            order = self.pendingOrders[i]
            serviceStr = self.getServiceTitle(serviceId=order["serviceId"])
            orderTimeStr = order["createdAt"]
            roomNumStr = str(RequestData.getBookingById(order["bookingId"])["roomNumber"])
            statusStr = "Serving" if order["status"] == 1 else "Done"
            noteStr = order["note"]

            self.pendingTable.setItem(row, 0, QtWidgets.QTableWidgetItem(serviceStr))
            self.pendingTable.setItem(row, 1, QtWidgets.QTableWidgetItem(orderTimeStr))
            self.pendingTable.setItem(row, 2, QtWidgets.QTableWidgetItem(roomNumStr))
            self.pendingTable.setItem(row, 3, QtWidgets.QTableWidgetItem(statusStr))
            self.pendingTable.setItem(row, 4, QtWidgets.QTableWidgetItem(noteStr))
            self.pendingTable.item(row, 0).setData(QtCore.Qt.UserRole, order["orderId"])

            row += 1

    def getSelectedOrder(self) -> int:
        selectedRow = self.pendingTable.currentRow()
        if selectedRow == -1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("You have to choose a row first")
            msg.setWindowTitle("Error")
            msg.exec_()
            return -1
       
        result = self.pendingTable.item(selectedRow, 0).data(QtCore.Qt.UserRole)
        print(result)
        return result
    
    def finishHandler(self):
        orderId = self.getSelectedOrder()
        if orderId == -1:
            return

        RequestData.finishServiceOrder(orderId=orderId)
        self.tabWidget.setCurrentIndex(2)

    def reloadData(self):
        date = self.dateEdit.date()

        servicesByDate = RequestData.getServiceOrdersByDate(date.toString("yyyy-MM-dd"))
        row = 0
        self.historyTable.setRowCount(len(servicesByDate))
        for i in range(len(servicesByDate)):
            order = servicesByDate[i]
            # serviceStr = RequestData.getServiceById(serviceId=order["serviceId"])["title"]
            serviceStr = self.getServiceTitle(serviceId=order["serviceId"])
            orderTimeStr = order["createdAt"].split("T")[1]
            # updateTimeStr = order["updatedAt"].split("T")[1]
            roomNumStr = str(RequestData.getBookingById(order["bookingId"])["roomNumber"])
            statusStr = "Serving" if order["status"] == 1 else "Done"
            noteStr = order["note"]

            self.historyTable.setItem(row, 0, QtWidgets.QTableWidgetItem(serviceStr))
            self.historyTable.setItem(row, 1, QtWidgets.QTableWidgetItem(orderTimeStr))
            self.historyTable.setItem(row, 2, QtWidgets.QTableWidgetItem(roomNumStr))
            self.historyTable.setItem(row, 3, QtWidgets.QTableWidgetItem(statusStr))
            self.historyTable.setItem(row, 4, QtWidgets.QTableWidgetItem(noteStr))
            row += 1

    def getServiceTitle(self, serviceId: int) -> str:
        return self.services[serviceId - 1]["title"]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Services()
    widget.show()
    sys.exit(app.exec_())