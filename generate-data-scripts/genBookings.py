from turtle import update
from tqdm import trange
from path import *
import random
import json

CURR_TIME = "11:10:59"

def getTypeIdFromRoomNumber(roomNumber: int) -> int:
    for room in rooms:
        if room["roomNumber"] == roomNumber:
            return room["typeId"]

def randomRoomType() -> int:
    i = random.randint(1,8)
    if i <= 2:
        return 1
    elif i <= 4:
        return 2
    elif i <= 5:
        return 3
    else:
        return random.randint(4, 9)

def isAvailableRoom (roomNumber: int, checkinDate, checkoutDate) -> bool: 
    for book in bookings:
        if book["roomNumber"] == roomNumber:
            if book["status"] == 2 or book["status"] == 1:
                return False
    return True

def getAvailableRoom(roomTypeId: int, checkinDate, checkoutDate) -> int:
    for room in rooms:
        if room["typeId"] == roomTypeId:
            avail = isAvailableRoom(room["roomNumber"], checkinDate, checkoutDate)
            # print(f"room: {room} - avail: {avail}")
            if avail:
                return room["roomNumber"]

def randomCheckinTime() -> str:
    hh = random.randint(10, 12)
    mm = random.randint(10, 59)
    ss = random.randint(10, 59)
    return f"{hh}:{mm}:{ss}"

def randomCheckoutTime() -> str:
    hh = random.randint(12, 14)
    mm = random.randint(10, 59)
    ss = random.randint(10, 59)
    return f"{hh}:{mm}:{ss}"

def bookRoom(checkinDate: str, checkoutDate: str, bookDateTime: str, status: int = 1):
    global bookingId
    roomType = randomRoomType()
    roomNumber = getAvailableRoom(roomType, checkinDate, checkoutDate)
    if not roomNumber:
        # print(f"No available room of type {roomType}")
        return
    booked[roomType - 1] += 1
    bookings.append({
        "id": bookingId,
        "clientName": genName(),
        "clientNumber": genPhoneNumber(),
        "checkinDate": checkinDate, 
        "checkoutDate": checkoutDate,
        "checkinTime": randomCheckinTime() if status >= 2 else "",
        "checkoutTime": randomCheckoutTime() if status >= 3 else "",
        "createdAt": bookDateTime,
        "status": status, # 1 Created, 2: Checkin, 3: Checkout,
        "roomNumber": roomNumber
    })
    bookingId += 1
    # print(f"Types: {booked}")

def genName() -> str:
    return random.choice(names)

def genPhoneNumber() -> str:
    return "09" + "".join([str(random.randint(0,9)) for _ in range (8)])
        
def genFirst50Bookings():
    for _ in range(50):
        bookDateTime = f"2022-03-0{random.randint(0, 9)}T{randomCheckinTime()}Z"
        checkinDate = "2022-04-" + str(random.randint(12, 15))
        checkoutDate = "2022-04-" + str(random.randint(16, 20))
        bookRoom(checkinDate, checkoutDate, bookDateTime, status=2)
    # with open("first50bookings.json", "w") as f:
    #     json.dump(bookings, f)

def orderService(bookingId: int, serviceId: int, date: str, lastDay = False):
    global orderId
    if not lastDay:
        orders.append({
            "orderId": orderId,
            "bookingId": bookingId,
            "serviceId": serviceId,
            "createdAt": f"{date}T{randomCheckinTime()}Z",
            "updatedAt": f"{date}T{randomCheckoutTime()}Z",
            "status": 2,
            "note": ""
        })
    else:
        timeA = randomCheckinTime()
        timeB = randomCheckinTime()

        createTime = min(timeA, timeB)
        updateTime = max(timeA, timeB)
        if updateTime < CURR_TIME:
            status = 2
        elif createTime < CURR_TIME:
            status = 1
        else:
            return
        print(date, createTime, updateTime)
        orders.append({
            "orderId": orderId,
            "bookingId": bookingId,
            "serviceId": serviceId,
            "createdAt": f"{date}T{createTime}Z",
            "updatedAt": f"{date}T{updateTime}Z" if status == 2 else "",
            "status": status,
            "note": ""
        })
    orderId += 1

def checkDate(date: str, lastDay: bool = False):
    departure = 0
    arrival = 0
    occupied = 0
    serv = 0
    for book in bookings:
        if book["checkoutDate"] == date:
            if not lastDay:
                book["status"] = 3
                book["checkoutTime"] = randomCheckoutTime()
                departure += 1
                booked[getTypeIdFromRoomNumber(book["roomNumber"]) - 1] -= 1
            else:
                checkoutTime = randomCheckinTime()
                if checkoutTime < CURR_TIME:
                    book["status"] = 3
                    book["checkoutTime"] = randomCheckinTime()
                    arrival += 1
        elif book["checkinDate"] == date:
            if not lastDay:
                book["status"] = 2
                book["checkinTime"] = randomCheckinTime()
                arrival += 1
            else:
                checkinTime = randomCheckinTime()
                if checkinTime < CURR_TIME:
                    book["status"] = 2
                    book["checkinTime"] = randomCheckinTime()
                    arrival += 1
        if book["status"] == 2:
            occupied += 1
            if not lastDay:
                if random.randint(1, 10) <= 2:
                    orderService(book["id"], random.randint(1, 5), date, lastDay=lastDay)
                    serv += 1
            else:
                if random.randint(1, 10) <= 4:
                    orderService(book["id"], random.randint(1, 5), date, lastDay=lastDay)
                    serv += 1

#     print(f"""
# ========================
# Date: {date}
# Occupied: {occupied}
# Arrival: {arrival}
# Departure: {departure}
# Orders: {serv}
# Types: {booked}""")

def simulateOneDay(day: int, month: int, lastDay= False):
    date = toDateString(day, month)
    checkDate(date, lastDay=lastDay)
    for _ in range(random.randint(10, 15)):
        checkinDay, checkinMonth = fixDate(day+1, month)
        checkinDate = toDateString(checkinDay, checkinMonth)

        bookDay, bookMonth = fixDate(day - random.randint(-5, 5), month - 1)
        bookDate = toDateString(bookDay, bookMonth)
        bookDateTime = f"{bookDate}T{randomCheckinTime()}Z"

        checkoutDay, checkoutMonth = fixDate(day + random.randint(2, 7), month)
        checkoutDate = toDateString(checkoutDay, checkoutMonth)
        
        bookRoom(checkinDate, checkoutDate, bookDateTime)

def toDateString(day: int, month: int) -> str:
    dayStr = str(day)
    monthStr = str(month)
    if day < 10:
        dayStr = "0" + dayStr
    if month < 10:
        monthStr = "0" + monthStr
    return f"2022-{monthStr}-{dayStr}"

def fixDate(day:int, month:int):
    if day > 30:
        day -= 30
        month += 1
    if day < 0:
        day += 30
        month -= 1
    return (day, month)

def simulate(firstDay: int, firstMonth: int, duration: int):
    day = firstDay
    month = firstMonth
    for _ in range(duration-1):
        simulateOneDay(day, month)
        day += 1
        day, month = fixDate(day, month)    
        print(day, month)
    simulateOneDay(day, month, lastDay=True)
if __name__ == "__main__":
    
    orders = []
    orderId = 1

    bookings = []
    bookingId = 1

    booked = [0]*9


    with open(DATAPATH + "rooms.json", "r") as f:
        rooms = json.load(f)

    with open("names.txt", "r") as f:
        names = list(map(str.strip,f.readlines()))
    
    genFirst50Bookings()
    simulate(15, 4, 19) # 19 days from 15.04 to 03.05

    with open(DATAPATH + "03-05-test-bookings.json", "w") as f:
        json.dump(bookings, f)

    with open(DATAPATH + "03-05-test-serviceOrders.json", "w") as f:
        json.dump(orders, f)
