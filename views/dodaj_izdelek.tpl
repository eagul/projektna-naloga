% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/dodaj_izdelek/" method="POST">


<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{st_izdelka}}">>
    
    ime : <input type="text" name="ime">
    
    cena: <input type="text" pattern="[0-9]*" name="cena">
    
    kategorija :<input type="text" name="kategorija">
    
    ponudba: <input type="text" name="ponudba">
    
    opis: <input type="text" name="opis">
    
    <input type="submit" value="Dodaj!">

</form>