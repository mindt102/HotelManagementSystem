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
    
    def getTotalCheckinByDate(date: str) -> int:
        pass

    def getTotalCheckoutByDate(date: str) -> int:
        pass

    def getTotalBookingByDate(date: str) -> int:
        pass

    def getTotalRevenueByDate(date: str) -> int:
        pass

    def getUpcomingArrivals() -> list:
        pass

    def getUpcomingDeparture() -> list:
        pass
    