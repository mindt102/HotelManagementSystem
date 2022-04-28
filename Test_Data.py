from unicodedata import name
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from const import *
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QWidget, QCalendarWidget, QLabel



class Revenue(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Revenue, self).__init__(*args, **kwargs)
        loadUi("Manage_Revenue.ui", self)
        self.setFixedSize(CONTENT_WIDTH, WINDOW_HEIGHT)
        #set length of columns in table
        self.table_Revenue.setColumnWidth(0,225)
        self.table_Revenue.setColumnWidth(1,160)
        self.table_Revenue.setColumnWidth(2,160)
        self.table_Revenue.setColumnWidth(3,160)

        #Set calandar up
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "Calendar_label")

        #Connect calendar to the function
        self.calendar.selectionChanged.connect(self.grab_date)
        #load data
        self.loaddata()
        self.Button_booking()

    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        #Put date on label
        self.label.setText(str(dateSelected.toString()))    
    
    #Button
    def Button_booking(self):
        self.Btn_booking.clicked.connect(self.Booking_Details)
    
    def loaddata(self):
        data = [{'booking id':777 ,'name':"Cristiano Ronaldo",'room_num':201,'room_fee': 200, 'services_fee':200},
        {'booking id': 10,'name': 'Lionel Messi', 'room_num':202,'room_fee':200,'services_fee':200},
        {'booking id': 9,'name': 'Zlatan Imbrahimovic', 'room_num': 203, 'room_fee':400, 'services_fee': 450}]
        row = 0
        self.table_Revenue.setRowCount(len(data))
        for i in range(len(data)):
            #self.table_Revenue.setItem(row, -1, QtWidgets.QTableWidgetItem(str(data[i]["booking id"])))
            self.table_Revenue.setItem(row, 0, QtWidgets.QTableWidgetItem(data[i]["name"]))
            self.table_Revenue.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[i]['room_num'])))
            self.table_Revenue.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[i]['room_fee'])))
            self.table_Revenue.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[i]['services_fee'])))
            row = row + 1
    
    #Event of button
    def Booking_Details(self):
        row = self.table_Revenue.currentRow()
        current_name = (self.table_Revenue.data['booking id'].text())
        print(current_name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rev = Revenue()
    widget = Revenue()
    widget.show()
    sys.exit(app.exec_())