
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<html xmlns:th="http://www.thymeleaf.org">
<head>

	<meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title> JustInTime</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	<link rel="stylesheet" type="text/css" href="css/login.css"> 
	<link rel="stylesheet" type="text/css" href="css/style.css"> 


</head>
<body>
	<header class="tm-header">
            <img class="tm-logo1" src="images/logo.png" alt="JustInTime">
    
            <nav class="tm-nav" >
                <div class="container-fluid">
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li ><a href="flight.html">Flight </a></li>
                    <li><a href="hotel.html">Hotel</a></li>
                    <li><a class="active" href="login.html">Login</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>  
                </div>  
            </nav>
    </header>
	<div class="container">
		<!-- <img id="logoimage" src="images/logo.png" alt="JustInTime"> -->

		<center><h3> <font color="darkred">Login Account</font></h3></center>

		
		<div class="form_container">
			<form method="post">
					<!-- Name : <input type="text" name="name" />
					Password : <input type="password" name="password" />  -->
					<!-- <input type="submit" /> -->
				<div class="form-group">
						Name : <center><input type="text" placeholder="Enter Email" name="name" required></center>
				</div>

				<div class="form-group">
						Password : <center><input type="password" placeholder="Enter Password" name="password" required></center>
				</div>

				<div class="submit">
					<center><input id="submit_button" type="submit"  value="Login"></center>
				</div>
			</form>
		</div>

		<div class="createaccount">
			<center><p style="font-size: 12px"> Don't have an Account? </p></center>
			<center><a id="createaccount" href="register.html">Create an Account Now</a></center>
			
		</div>

		
	<div class="imagelogin"></div>

	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>