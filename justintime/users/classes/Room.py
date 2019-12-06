import abc

class Room():

    def __init__(self):
        self.price = 0
        self.location= ""
        self.h_name = ""
        self.des = ""

    def showRoom(self):
        return self.location + "-" + self.h_name + "-" + self.des

    @abc.abstractmethod
    def getPrice(self):
        pass

class DeluxRoom(Room):
    
    def __init__(self,l,n,d):
        self.location = l
        self.h_name = n
        self.des = d

    def getPrice(self):
        if "King" in self.description:
            return 129.99
        elif "Sofa" in self.description:
            return 149.99
        else:
            return 139.99

class DoubleRoom(Room):

    def __init__(self,l,n,d):
        self.location = l
        self.h_name = n
        self.des = d
    
    def getPrice(self):
        return 109.99

class SingleRoom(Room):

    def __init__(self,l,n,d):
        self.location = l
        self.h_name = n
        self.des = d

    def getPrice(self):
        return 89.99

class RoomDecorator(Room):

    @abc.abstractmethod
    def showRoom(self):
        pass

class BreakFast(RoomDecorator):

    def __init__(self,r):
       self.room = r

    def showRoom(self):
        return self.room.showRoom() + ", BreakFast"

    def getPrice(self):
        return self.room.getPrice() + 7.99

class RoomWifi(RoomDecorator):

    def __init__(self,r):
        self.room = r

    def showRoom(self):
        return self.room.showRoom() + ", Wifi"

    def getPrice(self):
        return self.room.getPrice() + 15.99

class Snacks(RoomDecorator):

    def __init__(self,r):
        self.room = r

    def showRoom(self):
        return self.room.showRoom() + ", Snacks"

    def getPrice(self):
        return self.room.getPrice() + 19.99