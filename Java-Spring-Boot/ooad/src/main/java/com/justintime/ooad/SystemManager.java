package com.justintime.ooad;

import java.util.Observer;
import java.util.Observable;

public class SystemManager implements Observer{

    private LocalSystem ov = null;
    
    public SystemManager(LocalSystem ov){
        this.ov = ov;
    }

    @Override
    public void update(Observable o, Object arg) {
        if(o == ov){
            System.out.println(ov.getReservationState());
        }
    }
}
