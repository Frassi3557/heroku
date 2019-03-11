<html>
   <body>
      <form action = "https://vef-2019-v.herokuapp.com/result" method = "POST">

         <p>Nafn: <input type = "text" name = "Name" /></p>
         <p>Heimilisfang: <input type = "text" name = "Address" /></p>
         <p>Netfang: <input type = "email" name = "Email" /></p>
         <p>Símanúmer: <input type ="phone" name = "Phone" /></p>
         <h3>Fyrir hádegi:</h3>

         <input type="checkbox" name="fHadegi" value="Python"> Python<br>
         <input type="checkbox" name="fHadegi" value="Javascript"> Javascript<br>
         <input type="checkbox" name="fHadegi" value="Gagnagrunnur"> Gagnagrunnur<br>
         
         <h3>Hádegisverður</h3>
         <input type="radio" name="Matur" value="yes" checked> Já takk<br>
         <input type="radio" name="Matur" value="no"> Nei takk<br>
         
         <h3>Eftir hádegi:</h3>
         <input type="checkbox" name="eHadegi" value="Python2"> Python 2<br>
         <input type="checkbox" name="eHadegi" value="Javascript2"> Javascript 2<br>
         <input type="checkbox" name="eHadegi" value="Gagnagrunnur2"> Gagnagrunnur 2<br>
         
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>