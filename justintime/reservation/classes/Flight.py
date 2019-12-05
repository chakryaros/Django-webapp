import abc

class Flight():

    def __init__(self):
        self.price = 0
        self.description = "Unknown Flight"

    def showFlight(self):
        return self.description

    @abc.abstractmethod
    def getPrice(self):
        pass

class EconomicClass(Flight):

    def __init__(self,d):
        self.description = d + ", Economic Class"
    
    def getPrice(self):
        return 139.99

class FirstClass(Flight):

    def __init__(self,d):
        self.description = d + ", First Class"

    def getPrice(self):
        return 329.99

class FlightDecorator(Flight):
    
    def showFlight(self):
        pass

class ExtraMeal(FlightDecorator):

    def __init__(self,f):
        self.flight = f
    
    def showFlight(self):
        return self.flight.showFlight() + ", Extra Meal"
    
    def getPrice(self):
        return self.flight.getPrice() + 20.5

class ExtraSpace(FlightDecorator):

    def __init__(self,f):
        self.flight = f

    def showFlight(self):
        return self.flight.showFlight() + ", Extra Space"
    
    def getPrice(self):
        return self.flight.getPrice() + 49.99

class SeatSelection(FlightDecorator):

    def __init__(self,f):
        self.flight = f

    def showFlight(self):
        return self.flight.showFlight() + ", Seat Selection"

    def getPrice(self):
        return self.flight.getPrice() + 12.99

class FlightWifi(FlightDecorator):

    def __init__(self,f):
        self.flight = f

    def showFlight(self):
        return self.flight.showFlight() + ", Wifi"

    def getPrice(self):
        return self.flight.getPrice() + 15.99