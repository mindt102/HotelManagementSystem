import json
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
from const import *
from ui_references.ui_booking import Ui_Form
class Booking(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(Booking, self).__init__(*args, **kwargs)
        loadUi("booking.ui", self)
        for data in self.getAllRoomType():
            self.addRoom(data)
        self.clearTabWidget()

    def clearTabWidget(self):
        for _ in range(2):
            self.roomTypeTabWidget.removeTab(0)
        # self.roomTypeTabWidget.removeTab(1)
    
    def addRoom(self, roomData: dict):
        roomName = roomData["type"] + " Room"

        _translate = QtCore.QCoreApplication.translate

        # Create new room widget
        roomWidget = QtWidgets.QWidget()
        roomWidget.setObjectName(roomName)

        # Create widget layout
        verticalLayout = QtWidgets.QVBoxLayout(roomWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(0)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem2)
        
        # Create a new room type frame
        roomTypeFrame = QtWidgets.QFrame(roomWidget)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        roomTypeFrame.setFont(font)
        roomTypeFrame.setStyleSheet("background-color: white; border-radius: 10;")
        roomTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        roomTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        roomTypeFrame.setObjectName("roomTypeFrame")
        
        # Create grid layout from the frame
        gridLayout = QtWidgets.QGridLayout(roomTypeFrame)
        gridLayout.setVerticalSpacing(30)
        
        # Add text labels
        for i, s in enumerate(["Available room:", "Area:", "Price", "Free Services:", "Description:", "Number of room:"]):
            label = QtWidgets.QLabel(roomTypeFrame)
            label.setFont(font)
            gridLayout.addWidget(label, i, 0, 1, 1)
            label.setText(_translate("Form", s))

        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        # Create info labels
        price = QtWidgets.QLabel(roomTypeFrame)
        price.setFont(font)
        price.setObjectName("price")
        gridLayout.addWidget(price, 2, 1, 1, 1)
        
        bookAmount = QtWidgets.QSpinBox(roomTypeFrame)
        bookAmount.setFont(font)
        bookAmount.setStyleSheet("background-color: #dddddd; padding: 5px;")
        bookAmount.setObjectName("bookAmount")
        gridLayout.addWidget(bookAmount, 5, 1, 1, 1)
        
        area = QtWidgets.QLabel(roomTypeFrame)
        area.setFont(font)
        area.setObjectName("area")
        gridLayout.addWidget(area, 1, 1, 1, 1)
        
        description = QtWidgets.QLabel(roomTypeFrame)
        description.setFont(font)
        description.setWordWrap(True)
        description.setObjectName("description")
        gridLayout.addWidget(description, 4, 1, 1, 1)
        
        services = QtWidgets.QLabel(roomTypeFrame)
        services.setFont(font)
        services.setWordWrap(True)
        services.setObjectName("services")
        gridLayout.addWidget(services, 3, 1, 1, 1)
        
        availroom = QtWidgets.QLabel(roomTypeFrame)
        availroom.setFont(font)
        availroom.setObjectName("availroom")
        gridLayout.addWidget(availroom, 0, 1, 1, 1)

        # Add frame to widget
        verticalLayout.addWidget(roomTypeFrame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem3)

        # Add widget to tab widget
        self.roomTypeTabWidget.addTab(roomWidget, "")
        
        price.setText(_translate("Form", f"${roomData['price']} per night"))
        area.setText(_translate("Form", f"{roomData['area']} square meters"))
        description.setText(_translate("Form", roomData["description"]))

        serviceInfo = ""
        if len(roomData["promoServices"]) == 0:
            serviceInfo = "None"
        else:
            for serviceId in roomData["promoServices"]:
                sv = self.getServiceById(serviceId)
                serviceInfo += sv["title"] + ", "   
            serviceInfo = serviceInfo[:-2]
        services.setText(_translate("Form", serviceInfo))

        availroom.setText(_translate("Form", f"{self.getAvailableRoom()} rooms"))

        self.roomTypeTabWidget.setTabText(self.roomTypeTabWidget.indexOf(roomWidget), _translate("Form", roomName))
    
    def getAvailableRoom(self):
        return random.randint(10, 29)

    def getServiceById(self, serviceId):
        with open("./sample-data/services.json", "r", encoding="utf8") as f:
            services = json.load(f)
            for service in services:
                if service["id"] == serviceId:
                    return service
            else:
                return None
    def getAllRoomType(self):
        with open("./sample-data/roomType.json", "r", encoding="utf8") as f:
            return json.load(f)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Booking()
    widget.show()
    sys.exit(app.exec_())