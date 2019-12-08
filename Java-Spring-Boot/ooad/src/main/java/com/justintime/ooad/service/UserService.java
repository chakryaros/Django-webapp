package com.justintime.ooad.service;

// import com.justintime.ooad.model.Login;
// import com.justintime.ooad.model.User;

// public interface UserService {

//   void register(User user);

//   User validateUser(Login login);
// }

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
@Service
public class UserService {
    public boolean validateUser(String userid, String password) {
        // in28minutes, dummy
        return userid.equalsIgnoreCase("chakryaros")
                && password.equalsIgnoreCase("123456");
    }
}