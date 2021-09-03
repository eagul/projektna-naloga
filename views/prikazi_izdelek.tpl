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
% n += 1
% if not n == len(slovar):
    <form action="/uredi/{{izdelek.st_izdelka}}">
    <button type="submit">Uredi informacije o izdelku</button>
    </form>
%
%
%
%
%

<form action="/oceni/{{izdelek.st_izdelka}}">
<button type="submit">Oceni ta izdelek</button>
</form>