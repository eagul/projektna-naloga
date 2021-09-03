% rebase("osnova.tpl")

številka : <h1>{{izdelek.st_izdelka}}</h1>
% slovar = izdelek.slovar
% for key in slovar:
%     if slovar[key]:

        <li>{{key}}:{{slovar[key]}}</li>
%end
%end



<form action="/uredi/{{izdelek.st_izdelka}}">
<button type="submit">Uredi informacije o izdelku</button>
</form>