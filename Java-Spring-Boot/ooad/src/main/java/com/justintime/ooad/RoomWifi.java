package com.justintime.ooad;

public class RoomWifi extends RoomDecorator {
	Room room;
	
	public RoomWifi(Room room) {
		this.room = room;
	}
	
	public String showRoom() {
		return room.showRoom() + ", Wifi";
	}
	
	public double getPrice() {
		return room.getPrice() + 15.99;
	}
}
