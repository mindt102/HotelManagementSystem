from tqdm import trange
import random
import json


orders = []
orderId = 1
booked = [0]*9

with open("rooms.json", "r") as f:
    rooms = json.load(f)

with open("first50bookings.json", "r") as f:
    bookings = json.load(f)
    bookingId = len(bookings) + 1

with open("names.txt", "r") as f:
    names = list(map(str.strip,f.readlines()))

def getTypeIdFromRoomNumber(roomNumber: int):
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

def randomCheckinTime():
    hh = random.randint(10, 12)
    mm = random.randint(10, 59)
    ss = random.randint(10, 59)
    return f"{hh}:{mm}:{ss}"

def randomCheckoutTime():
    hh = random.randint(12, 14)
    mm = random.randint(10, 59)
    ss = random.randint(10, 59)
    return f"{hh}:{mm}:{ss}"

def bookRoom(checkinDate: str, checkoutDate: str, bookDateTime: str, status: int = 1):
    global bookingId
    roomType = randomRoomType()
    roomNumber = getAvailableRoom(roomType, checkinDate, checkoutDate)
    if not roomNumber:
        print(f"No available room of type {roomType}")
        return
    booked[roomType - 1] += 1
    bookings.append({
        "id": bookingId,
        "clientName": genName(),
        "clientNumber": genPhoneNumber(),
        "checkinDate": checkinDate, 
        "checkoutDate": checkoutDate,
        "checkinTime": randomCheckinTime(),
        "checkoutTime": randomCheckoutTime(),
        "createdAt": bookDateTime,
        "status": status, # 1 Created, 2: Checkin, 3: Checkout,
        "roomNumber": roomNumber
    })
    bookingId += 1
    print(f"Types: {booked}")

def genName() -> str:
    return random.choice(names)

def genPhoneNumber() -> str:
    return "09" + "".join([str(random.randint(0,9)) for _ in range (8)])
        
def genFirst50Bookings():
    global bookings
    global bookingId
    bookingId = 1
    bookings = []
    for _ in range(50):
        bookDate = f"2022-03-0{random.randint(0, 9)}T{randomCheckinTime()}Z"
        checkinDate = "2022-04-" + str(random.randint(12, 15))
        checkoutDate = "2022-04-" + str(random.randint(16, 20))
        bookRoom(checkinDate, checkoutDate, bookDate, status=2)
    with open("first50bookings.json", "w") as f:
        json.dump(bookings, f)

def orderService(bookingId: int, serviceId: int, date: str):
    global orderId
    orders.append({
        "orderId": orderId,
        "bookingId": bookingId,
        "serviceId": serviceId,
        "createdAt": f"{date}T{randomCheckinTime()}Z",
        "updatedAt": f"{date}T{randomCheckoutTime()}Z"
    })
    orderId += 1

def checkDate(date: str):
    departure = 0
    arrival = 0
    occupied = 0
    serv = 0
    for book in bookings:
        if book["checkoutDate"] == date:
            book["status"] = 3
            departure += 1
            booked[getTypeIdFromRoomNumber(book["roomNumber"]) - 1] -= 1
        elif book["checkinDate"] == date:
            book["status"] = 2
            arrival += 1

        if book["status"] == 2:
            occupied += 1
            if random.randint(1, 10) <= 2:
                orderService(book["id"], random.randint(1, 5), date)
                serv += 1
        
    print(f"""
========================
Date: {date}
Occupied: {occupied}
Arrival: {arrival}
Departure: {departure}
Orders: {serv}
Types: {booked}""")

def simulateOneDay(day: int, month: int):
    date = toDateString(day, month)
    checkDate(date)
    for _ in range(random.randint(10, 15)):
        checkinDay, checkinMonth = fixDate(day+1, month)
        checkinDate = toDateString(checkinDay, checkinMonth)

        bookDay, bookMonth = fixDate(day - random.randint(-5, 5), month - 1)
        bookDate = toDateString(bookDay, bookMonth)

        checkoutDay, checkoutMonth = fixDate(day + random.randint(2, 7), month)
        checkoutDate = toDateString(checkoutDay, checkoutMonth)
        
        bookRoom(checkinDate, checkoutDate, bookDate)

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
    for _ in range(duration):
        day += 1
        day, month = fixDate(day, month)

        simulateOneDay(day, month)

genFirst50Bookings()
simulate(15, 4, 18)

with open("bookings.json", "w") as f:
    json.dump(bookings, f)

with open("serviceOrders.json", "w") as f:
    json.dump(orders, f)
