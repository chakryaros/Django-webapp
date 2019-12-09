package com.justintime.ooad.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController{
    @GetMapping("/")
    public String displayHome(){
        return "index";
    }
    @GetMapping("/flight")
    public String displayFlights(){
        return "flight";
    }
    @GetMapping("/hotel")
    public String displayRooms(){
        return "hotel";
    }

}