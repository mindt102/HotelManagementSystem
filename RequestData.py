from const import *
import random
import json
import requests
import datetime


class RequestData:
    # Room Type
    def getRoomTypeById(typeId) -> str:
        try:
            r = requests.get(f"{URL}/roomTypes?typeId={typeId}")
            data = r.json()
            if data['isError'] is False:
                return data['data']
            return {"type": ""}
        except:
            return {"type": ""}

    def getRoomTypeByRoomNumber(roomNumber: int) -> str:
        roomRes = requests.get(f"{URL}/rooms/{str(roomNumber)}")
        roomData = roomRes.json()
        return RequestData.getRoomTypeById(roomData['roomType'])

    def getAllRoomType() -> list:
        try:
            r = requests.get(f"{URL}/roomTypes")
            data = r.json()
            if data['isError'] is False:
                return data['data']
            return []
        except:
            return []

    def getAvailableRoomByTypeId(roomTypeId: int) -> int:
        try:
            r = requests.get(
                f"{URL}/roomTypes/getAvailable?typeId={str(roomTypeId)}")
            data = r.json()
            if data['isError'] is False:
                return data['data']
            return 0
        except:
            return 0

    # Service
    def getServices():
        res = requests.get(f"{URL}/services")
        return res.json()

    def getServiceById(serviceId: int) -> dict:
        res = requests.get(f"{URL}/services/{serviceId}")
        return res.json()

    def getServiceOrdersByBookingId(bookingId: int) -> list:
        results = []
        with open(DATAPATH + "serviceOrders.json", "r", encoding="utf8") as f:
            orders = json.load(f)
            for order in orders:
                if order["bookingId"] == bookingId:
                    results.append(order)
        return results

    def getServiceOrdersByDate(date: str) -> list:
        r = requests.get(f"{URL}/services/getByDate?date={date}")
        return r.json()

    def createServiceOrder(orderData: dict):
        reqData = {
            "serviceId":orderData['serviceId'],
            'roomNumber': int(orderData['roomNumber']),
            "note":orderData['note'],
        }
        requests.post(f"{URL}/services/create", json=reqData)
        return

    def finishServiceOrder(orderId: int):
        requests.put(f"{URL}/services/finish/{str(orderId)}")
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
        newBooking = {
            "clientName": bookingData["clientName"],
            "clientNumber": bookingData["clientNumber"],
            "checkInDate": bookingData["checkinDate"],
            "checkOutDate": bookingData["checkoutDate"],
            "roomType": bookingData['roomType']
        }
        r = requests.post(f"{URL}/bookings/create", json=newBooking)
        if r.status_code == 200:
            bookingList = requests.get(f"{URL}/bookings").json()['data']
            bookingId = max(list(map(lambda x: x["id"], bookingList)))
            return bookingId

    def getBookingById(bookingId: int) -> dict:
        r = requests.get(f"{URL}/bookings/{str(bookingId)}")
        return r.json()['data']

    def getTotalCheckinByDate(date: str) -> int:
        r = requests.get(f"{URL}/bookings/checkin/byDate/count?date={date}")
        return int(r.text)
        # return random.randint(8, 15)

    def getTotalCheckoutByDate(date: str) -> int:
        r = requests.get(f"{URL}/bookings/checkout/byDate/count?date={date}")
        return int(r.text)
        # return random.randint(8, 15)

    def getTotalBookingByDate(date: str) -> int:
        r = requests.get(f"{URL}/bookings/byDate/count?date={date}")
        return int(r.text)
        # return random.randint(8, 15)

    def getTotalRevenueByDate(date: str) -> int:
        r = requests.get(f"{URL}/revenue/booking/total?date={date}")
        return int(r.text)
        # return random.randint(800, 1500)

    def getUpcomingArrivals() -> list:
        r = requests.get(f"{URL}/bookings/upcoming/arrivals")
        return r.json()
        
        # with open(DATAPATH + "upcoming.json", "r", encoding="utf8") as f:
        #     data = json.load(f)
        # return data

    def getUpcomingDeparture() -> list:
        r = requests.get(f"{URL}/bookings/upcoming/departure")
        return r.json()
        
        # with open(DATAPATH + "upcoming.json", "r", encoding="utf8") as f:
        #     data = json.load(f)
        # return data

    # Return a list of revenues from each booking that check out in a specific day
    def getRevenueByDate(date: str) -> list:
        r = requests.get(f"{URL}/revenue/booking?date={date}")
        return r.json()
        # bookingsByDate = []
        # with open(DATAPATH + "bookings.json", "r") as f:
        #     bookings = json.load(f)
        #     for booking in bookings:
        #         if booking["checkoutDate"] == date and booking["status"] == 3:
        #             bookingsByDate.append(booking)
        # revenuesByDate = []

        # for booking in bookingsByDate:
        #     revenue = {
        #         "bookingId": booking["id"],
        #         "clientName": booking["clientName"],
        #         "roomNumber": booking["roomNumber"],
        #         "roomFee": random.randint(300, 500),
        #         "serviceFee": random.randint(100, 300),
        #     }
        #     revenue["totalBill"] = revenue["roomFee"] + revenue["serviceFee"]
        #     revenuesByDate.append(revenue)
        # return revenuesByDate

    def getRevenueByBookingId(bookingId: int) -> int:
        r = requests.get(f"{URL}/revenue/booking/{bookingId}")
        return int(r.text)
        
        # return random.randint(400, 800)

    # Return a list of booking based on status and date, sort by checkinTime or checkoutTime
    def getBookings(clientName: str = None, checkoutDate: str = None, checkinDate: str = None, status: int = None) -> list:
        r = requests.get(f"{URL}/bookings")
        result = []
        try:
            if r.status_code == 200:
                for booking in r.json()['data']:
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
        except:
            pass

        return result

    def checkin(bookingId: int):
        requests.put(f"{URL}/bookings/{str(bookingId)}/checkin")
        return

    def checkout(bookingId: int):
        requests.put(f"{URL}/bookings/{str(bookingId)}/checkout")
        return

    def login(username: str, password: str) -> dict:
        user = {
            "username": "abc",
            "password": "123"

        }
        if username == user["username"] and password == user["password"]:
            return {
                "isError": False,
                "data": {
                    "firstName": "Minh",
                    "lastName": "Duong"
                }
            }
        return {
            "isError": True
        }


if __name__ == "__main__":
    print(RequestData.getUpcomingArrivals())
