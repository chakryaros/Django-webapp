from classes.Flight import EconomicClass,FirstClass,FlightWifi,ExtraSpace,ExtraMeal,SeatSelection
from classes.Room import SingleRoom,DoubleRoom,DeluxRoom,RoomWifi,Snacks,BreakFast
from classes.Customer import Customer
from classes.Systems import LocalSystem,SystemManager

def main():
    flights = []
    flights.append(EconomicClass("UA 2211 DEN-LAX 01/23/2019"))
    flights.append(FirstClass("UA 2211 DEN-LAX 03/13/2019"))
    flights.append(EconomicClass("DL 520 SEA-EWR 03/34/2019"))
    flights.append(FirstClass("DL 520 SEA-EWR 05/03/2019"))

    rooms = []
    rooms.append(SingleRoom("Boulder - Liberty International Airport Hotel - One Double Bed"))
    rooms.append(DoubleRoom("New York - Liberty International Airport Hotel - Two Double Beds"))
    rooms.append(DeluxRoom("Chicago - Hilton Hotel - One King Bed"))
    rooms.append(DoubleRoom("Denver - Holiday Inn - One Queen Bed"))
    rooms.append(DeluxRoom("Seattle - Hilton Hotel - One Queen Bed One Sofa Bed"))

    customers = []
    customers.append(Customer("Cassie Linamine","cassielin1998@gmail.com"))
    customers.append(Customer("Michael Sadrine","masa8888@yahoo.com"))

    JustInTime = LocalSystem(flights,rooms,customers)

    # Add subject and Observer
    subject = JustInTime
    concrete_observer = SystemManager(subject)
    subject.attach(concrete_observer)

    # TESTS
    
    # JustInTime.getCustomers()
    # JustInTime.getFlights()
    # JustInTime.getRooms()

    # JustInTime.addCustomer(Customer("Tiffany Pandline","tipa6666@colorado.edu"))
    # print(JustInTime.current_customer.getName())
    # JustInTime.current_customer.addRoomReservation(DeluxRoom("Seattle - Hilton Hotel - One Queen Bed One Sofa Bed"))
    # JustInTime.getRooms()

    # JustInTime.addCustomer(Customer("Tiffany Pandline","tipa6666@colorado.edu"))
    # f = EconomicClass("UA 2211 DEN-LAX 01/23/2019")
    # f = FlightWifi(f)
    # f = ExtraSpace(f)
    # JustInTime.current_customer.addFlightReservation(f)
    # print("Reservations: ")
    # JustInTime.current_customer.getReservations()
    # print("Remained Flights: ")
    # JustInTime.getFlights()

    # JustInTime.addCustomer(Customer("Tiffany Pandline","tipa6666@colorado.edu"))
    # r = DoubleRoom("New York - Liberty International Airport Hotel - Two Double Beds")
    # r = Snacks(r)
    # r = RoomWifi(r)
    # r = BreakFast(r)
    # JustInTime.current_customer.addRoomReservation(r)
    # print("Reservations: ")
    # JustInTime.current_customer.getReservations()
    # print("Remained Rooms ")
    # JustInTime.getRooms()

if __name__ == "__main__":
    main()
