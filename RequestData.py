from const import *
import random
import json
import requests
import datetime

class RequestData:
    # Room Type
    def getRoomTypeById(typeId) -> str:
        with open(DATAPATH + "roomType.json", "r", encoding="utf8") as f:
            roomTypes = json.load(f)
        for roomType in roomTypes:
            if roomType["id"] == typeId:
                return roomType
    
    def getRoomTypeByRoomNumber(roomNumber: int) -> str:
        with open(DATAPATH + "rooms.json", "r") as f:
            rooms = json.load(f)
        for room in rooms:
            if room["roomNumber"] == roomNumber:
                return RequestData.getRoomTypeById(room["typeId"])["type"]

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
        # res = requests.get(f"{URL}/services/{serviceId}")
        # return res.json()

    def getServiceOrdersByBookingId(bookingId: int) -> list:
        results = []
        with open(DATAPATH + "serviceOrders.json", "r", encoding="utf8") as f:
            orders = json.load(f)
            for order in orders:
                if order["bookingId"] == bookingId:
                    results.append(order)
        return results

    def getServiceOrdersByDate(date: str) -> list:
        results = []
        with open(DATAPATH + "serviceOrders.json", "r", encoding="utf8") as f:
            orders = json.load(f)
            for order in orders:
                if date in order["createdAt"]:
                    results.append(order)
        return results       

    def createServiceOrder(orderData: dict):
        print(orderData)
        return

    def finishServiceOrder(orderId: int):
        return

    def getTodayOrdersByStatus(status: int) -> list:
        todayDateString = datetime.datetime.today().strftime("%Y-%m-%d")
        with open(DATAPATH + "serviceOrders.json", "r", encoding="utf8") as f:
            orders = json.load(f)
        result = []
        for order in orders:
            if todayDateString in order["createdAt"] and order["status"] == status:
                result.append(order)
        return result
        
    # Booking
    def createBooking(bookingData: dict) -> int:
        # with open(DATAPATH + "bookings.json", "r+") as f:
        #     bookings = json.load(f)
        # bookingId = len(bookings) + 1
        # newBooking = {
        #     "id": bookingId,
        #     "clientName": bookingData["clientName"],
        #     "clientNumber": bookingData["clientNumber"],
        #     "checkinDate": bookingData["checkinDate"],
        #     "checkoutDate": bô
        # }
        # print(bookingData)
        bookingId = random.randint(1, 200)
        return bookingId

    def getBookingById(bookingId: int) -> dict:
        data = None
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
            for booking in bookings:
                if booking["id"] == bookingId:
                    data = booking
                    break
        return data
    
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

    # Return a list of revenues from each booking that check out in a specific day
    def getRevenueByDate(date: str) -> list:
        bookingsByDate = []
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
            for booking in bookings:
                if booking["checkoutDate"] == date and booking["status"] == 3:
                    bookingsByDate.append(booking)
        revenuesByDate = []

        for booking in bookingsByDate:
            revenue = {
                "bookingId": booking["id"],
                "clientName": booking["clientName"],
                "roomNumber": booking["roomNumber"],
                "roomFee": random.randint(300, 500),
                "serviceFee": random.randint(100, 300),
            }
            revenue["totalBill"] = revenue["roomFee"] + revenue["serviceFee"]
            revenuesByDate.append(revenue)
        return revenuesByDate

    def getRevenueByBookingId(bookingId: int) -> int:
        return random.randint(400, 800)

    # Return a list of booking based on status and date, sort by checkinTime or checkoutTime
    def getBookings(clientName: str = None, checkoutDate: str = None, checkinDate: str = None, status: int = None) -> list:
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
        result = []
        for booking in bookings:
            if clientName:
                if clientName not in booking["clientName"]:
                    continue
            if checkinDate:
                if booking["checkinDate"] != checkinDate:
                    continue
            if checkoutDate:
                if booking["checkoutDate"] != checkoutDate:
                    continue
            if status:
                if booking["status"] != status:
                    continue
            result.append(booking)
        
        # Sort results by checkinTime or checkoutTime

        return result

    def checkin(bookingId: int):
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
        for booking in bookings:
            if booking["id"] == bookingId:
                booking["status"] = 2
                print(booking)
                return
    
    def checkout(bookingId: int):
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
        for booking in bookings:
            if booking["id"] == bookingId:
                booking["status"] = 3
                print(booking)
                return
if __name__ == "__main__":
    print(RequestData.getServiceById(1))
