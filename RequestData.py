from const import *
import random
import json

class RequestData:
    def getAllRoomType() -> list:
        with open(DATAPATH + "roomType.json", "r", encoding="utf8") as f:
            return json.load(f)

    def getServiceById(serviceId: int) -> dict:
        with open(DATAPATH + "services.json", "r", encoding="utf8") as f:
            services = json.load(f)
            for service in services:
                if service["id"] == serviceId:
                    return service
            else:
                return None

    def getAvailableRoomByTypeId(roomTypeId: int) -> int:
        return random.randint(0, 5)

    def createBooking(bookingData: dict) -> int:
        print(bookingData)
        bookingId = random.randint(1, 200)
        return bookingId
    
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
    