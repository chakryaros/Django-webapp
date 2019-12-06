class Customer():

    def __init__(self,n,e):
        self.name = n
        self.email = e
        self.system = None
        self.roomReservation = []
        self.flightReservation = []
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def addRoomReservation(self,r):
        self.roomReservation.append(r)
        self.system.subject_state(r.showRoom())
        self.system.removeRoom(r)

    def addFlightReservation(self,f):
        self.flightReservation.append(f)
        self.system.subject_state(f.showFlight())
        self.system.removeFlight(f)
    
    def getReservations(self):
        print("Room Reservations: ")
        for r in self.roomReservation:
            print(r.showRoom() + " $" + str(r.getPrice()))
        
        print("Flight Reservations: ")
        for f in self.flightReservation:
            print(f.showFlight() + " $" + str(f.getPrice()))