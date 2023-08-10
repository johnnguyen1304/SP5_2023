class Vehicle:
    def __init__(self, wheelCount, doorCount, VIN):
        self.wheelCount = wheelCount
        self._doorCount = doorCount
        self.__VIN = VIN

    def getVIN(self):
        return self.__VIN

    def setVIN(self, new_vin):
        self.__VIN = new_vin

    vin = property(getVIN, setVIN)


class Bus(Vehicle):
    def __init__(self, wheelCount, doorCount, VIN, seatCount):
        super().__init__(wheelCount, doorCount, VIN)
        self.__seatCount = self.__validate_seat_count(seatCount)

    def getSeatCount(self):
        return self.__seatCount

    def setSeatCount(self, new_seat_count):
        self.__seatCount = self.__validate_seat_count(new_seat_count)

    seatCount = property(getSeatCount, setSeatCount)

    def __validate_seat_count(self, seatCount):
        if 0 <= seatCount <= 200:
            return seatCount
        return 0

class Engine:
    def __init__(self, engine_type):
        self.__type = engine_type
    
    def setType(self, new_engine_type):
        self.__type = new_engine_type
    
    def showDetails(self):
        return "The engine is type:" +self.__type


# Test the classes
vehicle = Vehicle(4, 4, "ZE1D4")
bus = Bus(8, 2, "B0TW", 40)

print("VIN number of Vehicle:", vehicle.vin)
print("VIN number of Bus:", bus.vin)
print("Seat Count of Bus:", bus.seatCount)



engine = Engine("Diesel")
print("-Engine Details-\n" + engine.showDetails())