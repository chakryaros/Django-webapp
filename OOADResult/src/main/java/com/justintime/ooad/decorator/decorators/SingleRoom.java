package com.justintime.ooad.decorator.decorators;
import com.justintime.ooad.decorator.components.Rooms;
public class SingleRoom extends Rooms {

	public SingleRoom(String descrip) {
		description = descrip;
	}
	
	public double getPrice() {
        return (double)100;
	}
}
