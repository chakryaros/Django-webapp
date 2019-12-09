package com.justintime.ooad.decorator.decorators;
import com.justintime.ooad.decorator.components.Rooms;
public class RoomWifi extends RoomDecorator {
	Rooms room;
	
	public RoomWifi(Rooms room) {
		this.room = room;
	}
	
	public String showRoom() {
		return room.showRoom() + ", Wifi";
	}
	
	public double getPrice() {
		return room.getPrice() + 15.99;
	}
}
