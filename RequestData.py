from const import *
import random
import json

class RequestData:
    # Room Type
    def getAllRoomType() -> list:
        with open(DATAPATH + "roomType.json", "r", encoding="utf8") as f:
            return json.load(f)

    def getAvailableRoomByTypeId(roomTypeId: int) -> int:
        return random.randint(0, 5)

    # Service
    def getServiceById(serviceId: int) -> dict:
        with open(DATAPATH + "services.json", "r", encoding="utf8") as f:
            services = json.load(f)
            for service in services:
                if service["id"] == serviceId:
                    return service
            else:
                return None

    # Booking
    def createBooking(bookingData: dict) -> int:
        print(bookingData)
        bookingId = random.randint(1, 200)
        return bookingId

    def getBookingById(bookingId: int) -> dict:
        data = {
            "id": bookingId,
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
        return data
    def getBookingServiceByOrderID(orderId: int) -> dict:
        order = {
            "orderId": 1,
            "bookingId": 7,
            "serviceId": 4,
            "createdAt": "2022-04-16T10:47:14Z",
            "updatedAt": "2022-04-16T12:27:11Z"
        }
        return order
    
    def getTotalCheckinByDate(date: str) -> int:
        return random.randint(8, 15)

    def getTotalCheckoutByDate(date: str) -> int:
        return random.randint(8, 15)

    def getTotalBookingByDate(date: str) -> int:
        return random.randint(8, 15)

    def getTotalRevenueByDate(date: str) -> int:
        return random.randint(800, 1500)

    def getUpcomingArrivals() -> list:
        with open(DATAPATH + "upcoming.json", "r", encoding="utf8") as f:
            data = json.load(f) 
        return data

    def getUpcomingDeparture() -> list:
        with open(DATAPATH + "upcoming.json", "r", encoding="utf8") as f:
            data = json.load(f) 
        return data
    