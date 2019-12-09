package com.justintime.ooad.decorator.components;

public abstract class Rooms {
	protected double price;
	protected String description;
	
	public Rooms() {
		this.price = 0;
		this.description = "Unknown Room";
	}
	
	public String showRoom() {
		return description;
	}
	
	public abstract double getPrice();
	
}
