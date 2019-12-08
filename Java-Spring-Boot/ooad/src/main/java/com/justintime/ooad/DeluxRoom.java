package com.justintime.ooad;

public class DeluxRoom extends Room {

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
