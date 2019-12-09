package com.justintime.ooad.decorator.decorators;

import java.util.ArrayList;
import java.util.Random;

import com.justintime.ooad.decorator.components.Flight;


public class EconomicClass extends Flight{

    public EconomicClass(String descrip) {
        description = descrip + ", Economy Class";
    }

    @Override
    public double getPrice() {
        ArrayList<Double> prices = new ArrayList<>();
        prices.add((double)239.99);
        prices.add((double)339.99);

        Random rand = new Random();
        return prices.get(rand.nextInt(prices.size()));
    }
    
}

