package com.justintime.ooad.dao;

import java.util.List;

import com.justintime.ooad.entites.Customer;

import org.springframework.data.repository.CrudRepository;

public interface CustomerRepository extends CrudRepository<Customer, Long>{
    @Override
    public List<Customer> findAll();
}