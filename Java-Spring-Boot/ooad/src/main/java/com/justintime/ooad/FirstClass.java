package com.justintime.ooad;
import java.util.ArrayList; 
import java.util.Random;

public class FirstClass extends Flight{

    public FirstClass(String descrip) {
        description = descrip + ", First Class";
    }

    @Override
    public double getPrice() {
        ArrayList<Double> prices = new ArrayList<>();
        prices.add((double) 529.99);
        prices.add((double) 629.99);

        Random rand = new Random();
        return prices.get(rand.nextInt(prices.size()));
    }
    
}