
<!DOCTYPE html>
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags"%>
<html>
<head>
    <meta charset="utf-8">
    <title> JustInTime</title>
  
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/style.css"> 


    </head>

    
<body >  

    <header class="tm-header">
            <img class="tm-logo" src="images/logo.png" alt="JustInTime">
    
            <nav class="tm-nav" >
                <div class="container-fluid">
                <ul>
                    <li><a class="active" href="index.html">Home</a></li>
                    <li ><a href="/flight.html">Flight </a></li>
                    <li><a href="/hotel.html">Hotel</a></li>
                    <li><a href="/login.jsp">Login</a></li>
                    <li><a href="/contact.html">Contact</a></li>
                </ul>  
                </div>  
            </nav>


    </header>

    <h2><center> Where do you want to visit?</center></h2>
     
     <section class="slider room flex">

      
                    <div class="tm-place">
                        <img  src="images/rocky.jpeg">
                       <a href="flight.html"> <p class="s">Rocky Mountain</p> </a>

                    </div>
                        <div class="tm-place">
                        <img  src="images/zion.jpeg">
                            <a href="flight.html"> <p class="s">Zion National Park</p></a>

                    </div>
                        <div class="tm-place">
                        <img  src="images/gc.jpeg">
                            <a href="flight.html">  <p>Grand Canyon</p></a>

                    </div>
                    </div>
                        <div class="tm-place">
                        <img  src="images/bg.jpg">
                        <a href="flight.html">  <p>Yellowstone</p></a>

                    </div>
                
    </section>

    <center><h2> Where do you want to stay?</h2></center>
     
     <section class="slider room flex">

      
                    <div class="tm-place">
                        <img  src="images/classic.jpg">
                       <a href="hotel.html"> <p class="s">Classic Hotel</p> </a>

                    </div>
                        <div class="tm-place">
                        <img  src="images/davison.jpg">
                            <a href="hotel.html"> <p class="s">Davision Hotel</p></a>

                    </div>
                        <div class="tm-place">
                        <img  src="images/hardrock.jpg">
                            <a href="hotel.html">  <p>HardRock Hotel</p></a>

                    </div>
                    </div>
                        <div class="tm-place">
                        <img  src="images/hilton.jpg">
                        <a href="hotel.html">  <p>Hilton Hotel</p></a>

                    </div>
                
    </section>

    </footer>
</body>
</html>