package com.justintime.ooad;

public class SingleRoom extends Room {

	public SingleRoom(String descrip) {
		description = descrip;
	}
	
	public double getPrice() {
        return (double)100;
	}
}
