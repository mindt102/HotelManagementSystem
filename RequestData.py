from const import *
import json

class RequestData:
    def getAllRoomType() -> list:
        with open("roomType.json", "r", encoding="utf8") as f:
            return json.load(f)

    def getServiceById(serviceId):
        with open("./sample-data/services.json", "r", encoding="utf8") as f:
            services = json.load(f)
            for service in services:
                if service["id"] == serviceId:
                    return service
            else:
                return None