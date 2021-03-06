from const import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from ui_references.ui_booking import Ui_Form
from RequestData import RequestData
from bookingdetail import BookingDetails
class Booking(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(Booking, self).__init__(*args, **kwargs)
        loadUi("booking.ui", self)
        self.services = RequestData.getServices()
        self.initTabWidget()
        self.initButtons()
        self.resetInputs()

    def resetInputs(self):
        self.nameLine.setFocus()
        
        self.nameLine.setText("")
        self.phoneLine.setText("")

        self.inDateLine.setDate(QtCore.QDate.currentDate())
        self.outDateLine.setDate(QtCore.QDate.currentDate())

    def initTabWidget(self):
        for data in RequestData.getAllRoomType():
            self.addRoomTypeDetails(data)
        self.clearTabWidget(2)

    def reloadTabWidget(self):
        for data in RequestData.getAllRoomType():
            self.addRoomTypeDetails(data)
        self.clearTabWidget(10)
    
    def initButtons(self):
        self.cancelBtn.clicked.connect(self.cancelHandler)
        self.bookBtn.clicked.connect(self.bookHandler)
    
    def cancelHandler(self):
        self.resetInputs()

    def bookHandler(self):
        bookingId = RequestData.createBooking(self.getInput())
        self.reloadTabWidget()
        self.resetInputs()
        self.bookingDetails = BookingDetails(bookingId)
        self.bookingDetails.show()

    def getInput(self) -> dict:
        self.nameLine.setPlaceholderText("Client name")

        name = self.nameLine.text()
        phoneNumber = self.phoneLine.text()

        checkInDate = self.inDateLine.date().toString("yyyy-MM-dd")
        checkOutDate = self.outDateLine.date().toString("yyyy-MM-dd")

        result = {
            "clientName": name,
            "clientNumber": phoneNumber,
            "checkinDate": checkInDate,
            "checkoutDate": checkOutDate,
            "roomType": self.getSelectedRoomType()
        }
        
        return result

    def getSelectedRoomType(self) -> int:
        return self.roomTypeTabWidget.currentIndex() + 1

    def clearTabWidget(self, numWidgets):
        for _ in range(numWidgets):
            self.roomTypeTabWidget.removeTab(0)
    
    def addRoomTypeDetails(self, roomData: dict):
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
        gridLayout.setContentsMargins(50, 11, 50, 11)
        
        # Add text labels
        for i, s in enumerate(["Available room:", "Area:", "Price", "Free Services:", "Description:"]):
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
        if len(roomData["promo"]) == 0:
            serviceInfo = "None"
        else:
            for serviceId in roomData["promo"]:
                sv = self.getServiceById(serviceId)
                serviceInfo += sv["title"] + ", "   
            serviceInfo = serviceInfo[:-2]
        services.setText(_translate("Form", serviceInfo))

        availroom.setText(_translate("Form", f"{RequestData.getAvailableRoomByTypeId(roomData['id'])} rooms"))

        self.roomTypeTabWidget.setTabText(self.roomTypeTabWidget.indexOf(roomWidget), _translate("Form", roomName))
    
    def getServiceById(self, serviceId):
        return self.services[serviceId - 1]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Booking()
    widget.show()
    sys.exit(app.exec_())