package com.justintime.ooad.decorator.decorators;
import com.justintime.ooad.decorator.components.Rooms;
public class DoubleRoom extends Rooms {

	public DoubleRoom(String descrip) {
		description = descrip;
	}
	
	// These may be superfluous.
	public double getPrice() {
		return (double)115;
	}

}
