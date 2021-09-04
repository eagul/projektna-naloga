% rebase("osnova.tpl")

številka : <h1>{{izdelek.st_izdelka}}</h1>
% slovar = izdelek.slovar
% for key in slovar:
%     if slovar[key]:

        <li>{{key}}:{{slovar[key]}}</li>
%end
%end


% n = 0
% slovar = izdelek.slovar
% for key in slovar:
% 
% if not slovar[key]:
    <form action="/uredi/{{izdelek.st_izdelka}}">
    <button type="submit">Dodaj {{key}} izdelka</button>
    </form>
%end
%end
%end
%end
%end

Ta izdelek je ocenejen kot: {{ocena.izracunana}}


<form action="/oceni/{{izdelek.st_izdelka}}">
<button type="submit">Oceni ta izdelek</button>
</form>