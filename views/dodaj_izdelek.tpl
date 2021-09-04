% rebase("osnova.tpl")


Vnesite informacije o izdelku

<form action="/dodaj_izdelek/" method="POST">


<input type="text" pattern="[0-9]*" name="st_izdelka" value="{{st_izdelka}}">>
    <br>
    ime : <input type="text" name="ime">
    <br>
    cena: <input type="text" pattern="[0-9]*" name="cena">
    <br>
    kategorija :<input type="text" name="kategorija">
    <br>
    ponudba: <input type="text" name="ponudba">
    <br>
    opis: <input type="text" name="opis">
    <br>
    <input type="submit" value="Dodaj!">

</form>