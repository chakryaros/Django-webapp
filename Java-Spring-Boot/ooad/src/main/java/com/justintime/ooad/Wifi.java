package com.justintime.ooad;

public class Wifi extends FlightDecorator{

    Flight flight;

    public Wifi(Flight flight){
        this.flight = flight;
    }

    @Override
    public String showFlight() {
        return flight.showFlight() + ", Wifi";
    }

    @Override
    public double getPrice() {
        return flight.getPrice() + 15.99;
    }
    
}