package com.justintime.ooad;

import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{
        ArrayList<Flight> flights = new ArrayList<>();
        ArrayList<Room> rooms = new ArrayList<>();
        ArrayList<customer> customers = new ArrayList<>();

        flights.add(new EconomicClass("UA 2211 DEN-LAX 01/23/2019"));
        flights.add(new FirstClass("UA 2211 DEN-LAX 03/13/2019"));
        flights.add(new EconomicClass("DL 520 SEA-EWR 03/34/2019"));
        flights.add(new FirstClass("DL 520 SEA-EWR 05/03/2019"));
   
        rooms.add(new SingleRoom("Boulder - Liberty International Airport Hotel - One Double Bed"));
        rooms.add(new DoubleRoom("New York - Liberty International Airport Hotel - Two Double Beds"));
        rooms.add(new DeluxRoom("Chicago - Hilton Hotel - One King Bed"));
        rooms.add(new DoubleRoom("Denver - Holiday Inn - One Queen Bed"));
        rooms.add(new DeluxRoom("Seattle - Hilton Hotel - One Queen Bed One Sofa Bed"));

        customers.add(new customer("Cassie Linamine","cassielin1998@gmail.com"));
        customers.add(new customer("Michael Sadrine","masa8888@yahoo.com"));

        LocalSystem JustInTime = new LocalSystem(flights, rooms, customers);
        JustInTime.setSystem(JustInTime);

        // JustInTime.addRoom(new SingleRoom("Seattle - Marriot Hotel - One Double Bed"));
        
        // JustInTime.searchFlight("DEN","LAX","01/23/2019","03/13/2019");
        // JustInTime.searchRoom("Boulder", "One");
        // JustInTime.addCustomer(new customer("Tiffany Pandline","tipa6666@colorado.edu"),JustInTime);
        // JustInTime.getCustomers();

        // HotelOrder order = new HotelOrder("Chicago - Hilton Hotel - One King Bed", 200);
        // c1.addHotelReservation(order);
        // System.out.println(JustInTime.getReservationState());

        // customer test = new customer("Liy Danny", "lilydanny@outlook.com");
        // Flight f = new FirstClass("AA 6666 LAX-SEA 12/24/2019 01/13/2020");
        // f = new Wifi(f);
        // f = new ExtraSpace(f);
        // JustInTime.addCustomer(test, JustInTime);
        // JustInTime.setCustomer(test);
        // JustInTime.current_customer.addFlightReservation(f);
        // JustInTime.current_customer.getFlightReservation();

        // customer test = new customer("Liy Danny", "lilydanny@outlook.com");
        // Room r = new DeluxRoom("Cinccinati - Courtyard - One King Bed");
        // r = new RoomWifi(r);
        // r = new BreakFast(r);
        // JustInTime.addCustomer(test, JustInTime);
        // JustInTime.setCustomer(test);
        // JustInTime.current_customer.addHotelReservation(r);
        // JustInTime.current_customer.getHotelReservation();

    }
}