% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/uredi_izdelek/" method="POST">


<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{izdelek.st_izdelka}}">>
    <br>
    ime : <input type="text" name="ime" value="{{izdelek.ime}}">
    <br>
    cena: <input type="text" pattern="[0-9]*" name="cena" value="{{izdelek.cena}}">
    <br>
    kategorija :<input type="text" name="kategorija" value="{{izdelek.kategorija}}">
    <br>
    ponudba: <input type="text" name="ponudba" value="{{izdelek.ponudba}}">
    <br>
    opis: <input type="text" name="opis" value="{{izdelek.opis}}">
    <br>
    <input type="submit" value="Dodaj!">

</form>