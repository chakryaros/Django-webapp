package com.justintime.ooad;


public class SeatSelection extends FlightDecorator{

    Flight flight;

    public SeatSelection(Flight flight){
        this.flight = flight;
    }

    @Override
    public String showFlight() {
        return flight.showFlight() + ", Seat Selection";
    }

    @Override
    public double getPrice() {
        return flight.getPrice() + 12.99;
    }
    
}