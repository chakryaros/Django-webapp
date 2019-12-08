package com.justintime.ooad;

import java.util.ArrayList;

public class customer {
    public String name;
    public String email;
    public String type;
    protected LocalSystem system;
    protected ArrayList<Room> hotelReservation = new ArrayList<>();
    protected ArrayList<Flight> flightReservation = new ArrayList<>();

    public customer(String name, String email){
        this.name = name;
        this.email = email;
    }

    public String getName(){
        return name;
    }

    public String getEmail(){
        return email;
    }

    public void addHotelReservation(Room h){
        hotelReservation.add(h);
        system.setReservationState(h.showRoom());
        system.removeRoom(h.showRoom());
    }

    public void addFlightReservation(Flight f){
        flightReservation.add(f);
        system.setReservationState(f.showFlight());
        system.removeFlight(f.showFlight());
    }

    protected void getHotelReservation(){
        for(int i = 0; i < hotelReservation.size(); i++)
        {
            System.out.println(hotelReservation.get(i).showRoom() + " $" + hotelReservation.get(i).getPrice());
        }
    }

    protected void getFlightReservation(){
        for(int i = 0; i < flightReservation.size(); i++)
        {
            System.out.println(flightReservation.get(i).showFlight() + " $" + flightReservation.get(i).getPrice());
        }
    }
}