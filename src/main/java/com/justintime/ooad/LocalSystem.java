package com.justintime.ooad;

import java.util.ArrayList;
import java.util.Observable;

import com.justintime.ooad.decorator.components.Flight;
import com.justintime.ooad.decorator.components.Rooms;
import com.justintime.ooad.entites.Customer;

public class LocalSystem extends Observable {
    
    private ArrayList<Flight> flights = new ArrayList<Flight>();
    private ArrayList<Rooms> rooms = new ArrayList<Rooms>();
    private ArrayList<Customer> customers = new ArrayList<Customer>();
    public Customer current_customer;
    private String reservationState;

    public LocalSystem(ArrayList<Flight> flights, ArrayList<Rooms> rooms, ArrayList<Customer> customers) {
        this.flights = flights;
        this.rooms = rooms;
        this.customers = customers;
        this.reservationState = "Unknown Reservation";
    }

    public void addFlight(Flight f) {
        flights.add(f);
        System.out.println("A Flight is Added To The System.");
    }

    public void addRoom(Rooms r) {
        rooms.add(r);
        System.out.println("A Room is Added To The System.");
    }

    public void searchFlight(String dep, String des, String dep_time, String return_time) {
        String for_trip = dep + "-" + des + " " + dep_time;
        String back_trip = des + "-" + dep + " " + return_time;
        for (int i = 0; i < flights.size(); i++) {
            if (flights.get(i).showFlight().contains(for_trip) || flights.get(i).showFlight().contains(back_trip)) {
                System.out.println(flights.get(i).showFlight());
            }
        }
    }

    public void searchRoom(String Location, String Type) {
        for (int i = 0; i < rooms.size(); i++) {
            if (rooms.get(i).showRoom().contains(Location) && rooms.get(i).showRoom().contains(Type)) {
                System.out.println(rooms.get(i).showRoom());
            }
        }
    }

    public void removeRoom(String descrip) {
        for (int i = 0; i < rooms.size(); i++) {
            if (rooms.get(i).showRoom() == descrip) {
                rooms.remove(i);
                break;
            }
        }
    }

    public void removeFlight(String descrip) {
        for (int i = 0; i < flights.size(); i++) {
            if (flights.get(i).showFlight() == descrip) {
                flights.remove(i);
                break;
            }
        }
    }

    public void setReservationState(String state) {
        this.reservationState = state;
        setChanged();
        notifyObservers();
    }

    public String getReservationState() {
        return reservationState;
    }

    public void getCustomers() {
        for (int i = 0; i < customers.size(); i++) {
            System.out.println(customers.get(i).getName() + " " + customers.get(i).getEmail());
        }
    }

    public Customer getCustomer(String name, String email) {
        for (int i = 0; i < customers.size(); i++) {
           if(customers.get(i).getName() == name && customers.get(i).getEmail() == email){
               return customers.get(i);
           }
        }
        return null;
    }

    // public void addCustomer(Customer c, LocalSystem s) {
    //     customers.add(c);
    //     this.current_customer = c;
    //     setSystem(s);
    // }

    public void setCustomer(Customer c) {
        this.current_customer = c;
    }

    // public void setSystem(LocalSystem s){
    //     for(int i = 0; i < customers.size(); i++) {
    //         customers.get(i).system = s;
    //     }
    // }

}