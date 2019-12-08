package com.justintime.ooad;

public abstract class Room {
	protected double price;
	protected String description;
	
	public Room() {
		this.price = 0;
		this.description = "Unknown Room";
	}
	
	public String showRoom() {
		return description;
	}
	
	public abstract double getPrice();
	
}
