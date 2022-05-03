from path import DATAPATH
import json
rooms = []
for f in range(2,7):
    for r in range(10):
        roomNo = f*100 + r
        if r <= 3:
            typeId = 1
        elif r <= 7:
            typeId = 2
        else:
            typeId = 3
        rooms.append({
            "roomNumber": roomNo,
            "typeId": typeId
        })
        
typeId = 4
for f in range(7, 10):
    for r in range(10):
        roomNo = f*100 + r
        rooms.append({
            "roomNumber": roomNo,
            "typeId": typeId
        })
        if roomNo % 5 == 4:
            typeId += 1

with open(DATAPATH + "rooms.json", "w") as f:
    json.dump(rooms, f)