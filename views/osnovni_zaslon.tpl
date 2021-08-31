% rebase("osnova.tpl")

<h2>Vnesite številko izdelka</h2>


<form action="/isci/">
  iskalni niz:
  <input type="text" pattern="[0-9]*" name="iskalni_niz">
  <input type="submit" value="Išči!">
</form>