from const import *
import random
import json
import requests

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
        # res = requests.get(f"{URL}/services/{serviceId}")
        # return res.json()

    def getServicesByBookingId(bookingId: int) -> list:
        results = []
        with open(DATAPATH + "serviceOrders.json", "r", encoding="utf8") as f:
            services = json.load(f)
            for service in services:
                if service["bookingId"] == bookingId:
                    results.append(service)
        return results

    # Booking
    def createBooking(bookingData: dict) -> int:
        print(bookingData)
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

    # Return a list of booking based on status and date, sort by checkinTime or checkoutTime
    def getBookings(clientName: str = None, checkoutDate: str = None, checkinDate: str = None, status: int = None, sortBy: str = None) -> list:
        with open(DATAPATH + "bookings.json", "r") as f:
            bookings = json.load(f)
        result = []
        for booking in bookings:
            if clientName:
                if booking["clientName"] != clientName:
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

if __name__ == "__main__":
    print(RequestData.getServiceById(1))