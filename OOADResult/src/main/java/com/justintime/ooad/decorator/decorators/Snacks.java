package com.justintime.ooad.decorator.decorators;
import com.justintime.ooad.decorator.components.Rooms;
public class Snacks extends RoomDecorator {
	Rooms room;
	
	public Snacks(Rooms room) {
		this.room = room;
	}
	
	public String showRoom() {
		return room.showRoom() + ", Stocked Mini-Fridge";
	}
	
	public double getPrice() {
		return room.getPrice() + 20;
	}

}
