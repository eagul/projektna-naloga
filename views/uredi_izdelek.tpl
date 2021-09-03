% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/uredi_izdelek/" method="POST">


<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{izdelek.st_izdelka}}">>
    
    ime : <input type="text" name="ime" value="{{izdelek.ime}}">
    
    cena: <input type="text" pattern="[0-9]*" name="cena" value="{{izdelek.cena}}">
    
    kategorija :<input type="text" name="kategorija" value="{{izdelek.kategorija}}">
    
    ponudba: <input type="text" name="ponudba" value="{{izdelek.ponudba}}">
    
    opis: <input type="text" name="opis" value="{{izdelek.opis}}">
    
    <input type="submit" value="Dodaj!">

</form>