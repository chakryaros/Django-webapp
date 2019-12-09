package com.justintime.ooad.decorator.decorators;
import com.justintime.ooad.decorator.components.Rooms;
public class DeluxRoom extends Rooms {

	public DeluxRoom(String descrip) {
		description = descrip;
	}
	
	public double getPrice() {
		if(description.contains("King")){
			return (double)120;
		}
		else if(description.contains("Sofa")){
			return (double)135;
		}
		else{
			return (double)130;
		}
		
	}
	
}
