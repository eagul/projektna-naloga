% rebase("osnova.tpl")

Vnesite številko računa
<form action="/st_racuna/">
  Številka računa:
  <input type="text" pattern="[0-9]*" name="st_racuna">
  <input type="submit" value="Vnesi!">
</form>