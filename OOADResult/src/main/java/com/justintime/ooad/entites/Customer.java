package com.justintime.ooad.entites;

// import java.util.ArrayList;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

// import com.justintime.ooad.Flight;
// import com.justintime.ooad.LocalSystem;
// import com.justintime.ooad.Rooms;

@Entity
public class Customer {
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    private Long CustomerId;
    public String name;
    public String email;
    public String type;

    // protected LocalSystem system;
    // protected ArrayList<Rooms> hotelReservation = new ArrayList<>();
    // protected ArrayList<Flight> flightReservation = new ArrayList<>();

    public Customer(String name, String email){
        this.name = name;
        this.email = email;
    }

    public Customer() {
	}

	public void setCustomerId(Long CustomerId){
        this.CustomerId = CustomerId;
    }

    public Long getCustomerId(){
        return CustomerId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    // public ArrayList<Rooms> getHotelReservation() {
    //     return hotelReservation;
    // }

    // public void setHotelReservation(ArrayList<Rooms> hotelReservation) {
    //     this.hotelReservation = hotelReservation;
    // }

    // public ArrayList<Flight> getFlightReservation() {
    //     return flightReservation;
    // }

    // public void setFlightReservation(ArrayList<Flight> flightReservation) {
    //     this.flightReservation = flightReservation;
    // }

    
}