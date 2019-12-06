from classes.Flight import EconomicClass,FirstClass,FlightWifi,ExtraSpace,ExtraMeal,SeatSelection
from classes.Room import SingleRoom,DoubleRoom,DeluxRoom,RoomWifi,Snacks,BreakFast
from classes.Customer import Customer
from classes.Systems import LocalSystem,SystemManager
import random

def main():

    flights = []
    file = open("data.txt","r")

    for line in file.readlines():
        loc,dep,des,date = line.rstrip('\n').split(',')
        index = random.randint(0,1)
        if index == 0:
            f = EconomicClass(loc,dep,des,date)
        else:
            f = FirstClass(loc,dep,des,date)
        
        flights.append(f)
    file.close()


    rooms = []
    rooms.append(SingleRoom("Boulder","Liberty International Airport Hotel", "One Double Bed"))
    rooms.append(DoubleRoom("New York", "Liberty International Airport Hotel", "Two Double Beds"))
    rooms.append(DeluxRoom("Chicago", "Hilton Hotel", "One King Bed"))
    rooms.append(DoubleRoom("Denver", "Holiday Inn", "One Queen Bed"))
    rooms.append(DeluxRoom("Seattle", "Hilton Hotel", "One Queen Bed One Sofa Bed"))

    customers = []
    customers.append(Customer("Cassie Linamine","cassielin1998@gmail.com"))
    customers.append(Customer("Michael Sadrine","masa8888@yahoo.com"))
    customers.append(Customer("Kyle Burz","kybu@yahoo.com"))
    customers.append(Customer("Christian Lamort","chla8888@yahoo.com"))
    customers.append(Customer("Tom Luen","tomluen@yahoo.com"))
    customers.append(Customer("Matthrew Dulmer","lovematt@gmail.com"))

    JustInTime = LocalSystem(flights,rooms,customers)

    # Add subject and Observer
    subject = JustInTime
    concrete_observer = SystemManager(subject)
    subject.attach(concrete_observer)

    # TESTS
    # JustInTime.addCustomer(Customer("Tiffany Pandline","tipa6666@colorado.edu"))
    # f = EconomicClass("UA 2211 DEN-LAX 01/23/2019")
    # f = FlightWifi(f)
    # f = ExtraSpace(f)
    # JustInTime.current_customer.addFlightReservation(f)
    # print("Reservations: ")
    # JustInTime.current_customer.getReservations()
    # print("Remained Flights: ")
    # JustInTime.getFlights()

    for days in range(1,10):
        print("Day: " + str(days))
        flights = JustInTime.getFlights()
        print("")
        for i in range(0,random.randint(0,6)):
            c = random.choice(customers)

            if flights != []:
                f = random.choice(flights)

                for j in range(0,random.randint(0,3)):
                    add_on = random.choice(["Extra Meal","Extra Space","Seat Selection","Flight Wifi"])
                    if add_on == "Extra Meal":
                        f = ExtraMeal(f)
                    elif add_on == "Extra Space":
                        f = ExtraSpace(f)
                    elif add_on == "Seat Selection":
                        f = SeatSelection(f)
                    else:
                        f = FlightWifi(f)

                c.addFlightReservation(f)
            else:
                print("Sorry, " + c.getName() + ". No flights are available at this moment.")
            
        print("--------------------------------------")

if __name__ == "__main__":
    main()
    db_table = 'Admin'
