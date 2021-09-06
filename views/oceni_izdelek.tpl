% rebase("osnova.tpl")


<form action="/oceni/{{ocena.st_izdelka}}" method="POST" required >
št računa : <input type="text" pattern="[0-9]*"  name="st_racuna">
<br>
<input type="radio" id="YGWYPF" name="ocena" value="YGWYPF" required >
  <label for="YGWYPF">YOU GET WHAT YOU PAY FOR</label><br>
  <input type="radio" id="POP" name="ocena" value="POP">
  <label for="POP">PRICE-OVER PERFORMANCE</label><br>
  <input type="radio" id="SCAM" name="ocena" value="SCAM">
  <label for="SCAM">SCAM</label>
<button type="submit">oceni</button>
</form>