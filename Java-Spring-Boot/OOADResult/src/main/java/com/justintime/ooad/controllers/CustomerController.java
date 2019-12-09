package com.justintime.ooad.controllers;

import com.justintime.ooad.entites.Customer;

import com.justintime.ooad.dao.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/customer")
public class CustomerController {

    Customer aCustomer = new Customer();

    @Autowired
    CustomerRepository cusRepo;

    @GetMapping("/login")
    public String login(Model model){
        model.addAttribute("customer", aCustomer);
        return "login";
    }

    @GetMapping("/register")
    public String registerCustomer(Model model){
        model.addAttribute("aCustomer", aCustomer);
        return "register";
    }

    @PostMapping("/save")
    public String CreateCustomer(Customer customer, Model model){
        cusRepo.save(customer);
        return "redirect:/";
    }

}