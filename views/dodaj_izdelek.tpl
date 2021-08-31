% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/dodaj_izdelek/" method="POST">
  iskalni niz:

<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{st_izdelka}}">>

 ime : <input type="text" name="ime">
  
 opis: <input type="text" pattern="[0-9]*" name="cena">

  kategorija :<input type="text" name="kategorija">

 ponudba: <input type="text" name="ponudba">

  opis: <input type="text" name="opis">

  <input type="submit" value="Dodaj!">
</form>