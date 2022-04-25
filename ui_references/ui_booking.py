# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'booking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1480, 930)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1480, 930))
        Form.setMaximumSize(QtCore.QSize(1480, 930))
        Form.setStyleSheet("background-color: #f0f0f0;")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #3f4773;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("background-color: white; border-radius: 10;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.inDateLine = QtWidgets.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inDateLine.setFont(font)
        self.inDateLine.setStyleSheet("background-color: #dddddd; padding: 3px;")
        self.inDateLine.setCalendarPopup(True)
        self.inDateLine.setTimeSpec(QtCore.Qt.UTC)
        self.inDateLine.setObjectName("inDateLine")
        self.gridLayout.addWidget(self.inDateLine, 4, 1, 1, 1)
        self.nameLine = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLine.setFont(font)
        self.nameLine.setStyleSheet("background-color: #dddddd; padding: 3px;")
        self.nameLine.setObjectName("nameLine")
        self.gridLayout.addWidget(self.nameLine, 2, 1, 1, 1)
        self.phoneLine = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneLine.setFont(font)
        self.phoneLine.setStyleSheet("background-color: #dddddd; padding: 3px;")
        self.phoneLine.setObjectName("phoneLine")
        self.gridLayout.addWidget(self.phoneLine, 3, 1, 1, 1)
        self.outDateLine = QtWidgets.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outDateLine.setFont(font)
        self.outDateLine.setStyleSheet("background-color: #dddddd; padding: 3px;")
        self.outDateLine.setCalendarPopup(True)
        self.outDateLine.setTimeSpec(QtCore.Qt.UTC)
        self.outDateLine.setObjectName("outDateLine")
        self.gridLayout.addWidget(self.outDateLine, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.line = QtWidgets.QFrame(self.frame_5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #3f4773;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.roomTypeTabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.roomTypeTabWidget.setStyleSheet("background-color: #f0f0f0;")
        self.roomTypeTabWidget.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.roomTypeTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.roomTypeTabWidget.setTabBarAutoHide(True)
        self.roomTypeTabWidget.setObjectName("roomTypeTabWidget")
        self.singleRoom = QtWidgets.QWidget()
        self.singleRoom.setObjectName("singleRoom")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.singleRoom)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.roomTypeFrame = QtWidgets.QFrame(self.singleRoom)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.roomTypeFrame.setFont(font)
        self.roomTypeFrame.setStyleSheet("background-color: white; border-radius: 10;")
        self.roomTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomTypeFrame.setObjectName("roomTypeFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.roomTypeFrame)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.price = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.gridLayout_2.addWidget(self.price, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.bookAmount = QtWidgets.QSpinBox(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bookAmount.setFont(font)
        self.bookAmount.setStyleSheet("background-color: #dddddd; padding: 5px;")
        self.bookAmount.setObjectName("bookAmount")
        self.gridLayout_2.addWidget(self.bookAmount, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.area = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.area.setFont(font)
        self.area.setObjectName("area")
        self.gridLayout_2.addWidget(self.area, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.description = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.description.setFont(font)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.gridLayout_2.addWidget(self.description, 4, 1, 1, 1)
        self.services = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.services.setFont(font)
        self.services.setObjectName("services")
        self.gridLayout_2.addWidget(self.services, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)
        self.availroom = QtWidgets.QLabel(self.roomTypeFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.availroom.setFont(font)
        self.availroom.setObjectName("availroom")
        self.gridLayout_2.addWidget(self.availroom, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.roomTypeFrame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.roomTypeTabWidget.addTab(self.singleRoom, "")
        self.doubleRoom = QtWidgets.QWidget()
        self.doubleRoom.setObjectName("doubleRoom")
        self.roomTypeTabWidget.addTab(self.doubleRoom, "")
        self.verticalLayout_2.addWidget(self.roomTypeTabWidget)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(1100, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cancelBtn = QtWidgets.QPushButton(self.frame_2)
        self.cancelBtn.setStyleSheet("QPushButton\n"
"{\n"
"      border-style: none;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    background-color: #3f4773;\n"
"    border-radius: 10;\n"
"    padding: 7;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"      background-color:#485187;\n"
"}")
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout_3.addWidget(self.cancelBtn, 0, 0, 1, 1)
        self.bookBtn = QtWidgets.QPushButton(self.frame_2)
        self.bookBtn.setStyleSheet("QPushButton\n"
"{\n"
"      border-style: none;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    background-color: #3f4773;\n"
"    border-radius: 10;\n"
"    padding: 7;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"      background-color:#485187;\n"
"}")
        self.bookBtn.setFlat(False)
        self.bookBtn.setObjectName("bookBtn")
        self.gridLayout_3.addWidget(self.bookBtn, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.roomTypeTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_18.setText(_translate("Form", "Booking"))
        self.label_16.setText(_translate("Form", "Information"))
        self.label.setText(_translate("Form", "Name"))
        self.inDateLine.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.outDateLine.setDisplayFormat(_translate("Form", "yyyy/MM/dd"))
        self.label_3.setText(_translate("Form", "Phone Number"))
        self.label_4.setText(_translate("Form", "Checkin Date"))
        self.label_5.setText(_translate("Form", "Checkout Date"))
        self.label_17.setText(_translate("Form", "Select Room"))
        self.price.setText(_translate("Form", "$50 per night"))
        self.label_14.setText(_translate("Form", "Description:"))
        self.label_9.setText(_translate("Form", "Free Services:"))
        self.label_11.setText(_translate("Form", "Available room:"))
        self.label_2.setText(_translate("Form", "Area:"))
        self.area.setText(_translate("Form", "37 square meters"))
        self.label_7.setText(_translate("Form", "Price:"))
        self.description.setText(_translate("Form", "A room assigned to one person. May have one or more beds."))
        self.services.setText(_translate("Form", "None"))
        self.label_13.setText(_translate("Form", "Number of room:"))
        self.availroom.setText(_translate("Form", "10 rooms"))
        self.roomTypeTabWidget.setTabText(self.roomTypeTabWidget.indexOf(self.singleRoom), _translate("Form", "Single Room"))
        self.roomTypeTabWidget.setTabText(self.roomTypeTabWidget.indexOf(self.doubleRoom), _translate("Form", "Tab 2"))
        self.cancelBtn.setText(_translate("Form", "Cancel"))
        self.bookBtn.setText(_translate("Form", "Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())