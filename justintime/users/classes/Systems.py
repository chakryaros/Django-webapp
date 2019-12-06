import abc

class LocalSystem():

    def __init__(self,f,r,c):
        self._observers = set()
        self._state = None

        self.flights = f
        self.rooms = r
        self.customers = c
        self.current_customer = None

        for cs in self.customers:
            cs.system = self

    def addFlight(self,f):
        self.flights.append(f)
        print(f.showFlight() + " Is Now Available For Booking!")

    def addRoom(self,r):
        self.rooms.append(r)
        print(r.showRoom() + " Is Now Available For Booking!")

    def addCustomer(self,c):
        self.customers.append(c)
        self.current_customer = c
        self.current_customer.system = self

    def removeFlight(self,f):
        for flight in self.flights:
            if flight.showFlight() in f.showFlight():
                self.flights.remove(flight)
                break

    def removeRoom(self,r):
        for room in self.rooms:
            if room.showRoom() in r.showRoom():
                self.rooms.remove(room)
                break

    def getCustomers(self):
        for c in self.customers:
            print(c.getName() + " " + c.getEmail())

    def getFlights(self):
        print("Flights Available: ")
        for f in self.flights:
            print(f.showFlight())
        
        return self.flights
            

    def getRooms(self):
        print("Rooms Available: ")
        for r in self.rooms:
            print(r.showRoom())

    def searchRoom(self,loc,n):
        for r in self.rooms:
            if loc in r.showRoom() and n in r.showRoom():
                return r

    def searchRoom(self,dep,des,date):
        for f in self.flights:
            if dep + "-" + des in f.showFlight() and date in f.showFlight():
                return f

    # Observer Pattern
    def attach(self,observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self,observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def get_state(self):
        return self._state

    def subject_state(self,arg):
        self._state = arg
        self._notify()
        
    
class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class SystemManager(Observer):

    def __init__(self,s):
        self._subject = s

    def update(self, arg):
        self._observer_state = arg
        print(self._subject.get_state())