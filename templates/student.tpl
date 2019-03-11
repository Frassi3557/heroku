<html>
   <body>
      <form action = "https://vef-2019-v.herokuapp.com/result" method = "POST">

         <p>Nafn: <input type = "text" name = "Nafn" /></p>
         <p>Heimilisfang: <input type = "text" name = "Heimilisfang" /></p>
         <p>Netfang: <input type = "email" name = "Netfang" /></p>
         <p>Símanúmer: <input type ="phone" name = "Sími" /></p>
         <h3>Fyrir hádegi:</h3>

         <input type="checkbox" name="Fyrir hádegi" value="Python"> Python<br>
         <input type="checkbox" name="Fyrir hádegi" value="Javascript"> Javascript<br>
         <input type="checkbox" name="Fyrir hádegi" value="Gagnagrunnur"> Gagnagrunnur<br>
         
         <h3>Hádegisverður</h3>
         <input type="radio" name="Matur" value="Já" checked> Já takk<br>
         <input type="radio" name="Matur" value="Nei"> Nei takk<br>
         
         <h3>Eftir hádegi:</h3>
         <input type="checkbox" name="Eftir hádegi" value="Python 2"> Python 2<br>
         <input type="checkbox" name="Eftir hádegi" value="Javascript 2"> Javascript 2<br>
         <input type="checkbox" name="Eftir hádegi" value="Gagnagrunnur 2"> Gagnagrunnur 2<br>
         
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>