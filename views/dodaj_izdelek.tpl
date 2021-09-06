% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/dodaj_izdelek/" method="POST">


<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{st_izdelka}}">
    <br>
    ime : <input type="text" name="ime">
    <br>
    cena: <input type="text" pattern="[0-9]*" name="cena">
    <br><br>
    Kategorija:
       <input type="radio" id="A" name="kategorija" value="A" required >
  <label for="A">A</label><br>
  <input type="radio" id="B" name="kategorija" value="B">
  <label for="B">B</label><br>
  <input type="radio" id="C" name="kategorija" value="C">
  <label for="C">C</label>
    <br><br>
    Ponudba:
    <input type="radio" id="Stalna" name="ponudba" value="Stalna" required >
  <label for="Stalna">Stalna ponudba</label><br>
  <input type="radio" id="Začasna" name="ponudba" value="Začasna">
  <label for="Začasna">Začasna ponudba</label><br>
 
    <br>
    opis: <input type="text" name="opis">
    <br>
    <input type="submit" value="Dodaj!">

</form>