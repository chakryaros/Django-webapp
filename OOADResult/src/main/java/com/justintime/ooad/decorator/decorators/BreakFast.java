package com.justintime.ooad.decorator.decorators;

import com.justintime.ooad.decorator.components.Rooms;

public class BreakFast extends RoomDecorator {
	Rooms room;
	
	public BreakFast(Rooms room) {
		this.room = room;
	}
	
	public String showRoom() {
		return room.showRoom() + ", Breakfast";
	}
	
	public double getPrice() {
		return room.getPrice() + 7.99;
	}

}
