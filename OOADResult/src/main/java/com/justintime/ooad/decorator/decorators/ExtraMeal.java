package com.justintime.ooad.decorator.decorators;

import com.justintime.ooad.decorator.components.Flight;

public class ExtraMeal extends FlightDecorator{

    Flight flight;

    public ExtraMeal(Flight flight){
        this.flight = flight;
    }

    @Override
    public String showFlight() {
        return flight.showFlight() + ", Extra Meal";
    }

    @Override
    public double getPrice() {
        return flight.getPrice() + 11.50;
    }
    
}