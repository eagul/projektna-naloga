import bottle

import model


bottle.TEMPLATE_PATH.insert(0, 'C:\\Users\\Jamnik\\Documents\\FMF\\UVP drugič\\projektna naloga\\views')

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template("osnovni_zaslon.tpl")

@bottle.get('/isci/')
def posreduj():
    iskalni_niz = bottle.request.query['iskalni_niz']
    if not model.preveri_ce_je_veljavna_st_izdelka(iskalni_niz):
        return "Številka izdelka ni veljavna"

    else:
        return bottle.template("dodaj_izdelek.tpl", st_izdelka=iskalni_niz)

        
bottle.post("/st_racuna/")
        


bottle.post('/dodaj_izdelek/')
def dodaj_izdelek():
    ime = bottle.request.forms['ime']
    st_izdelka = bottle.request.forms["st_izdelka"]
    cena = bottle.request.forms['cena']
    opis = bottle.request.forms['opis']
    kategorija = bottle.request.forms['kategorija']
    ponudba = ime = bottle.request.forms['ponudba']
    model.Izdelek(st_izdelka, ime, cena, kategorija, ponudba, opis)
    
    bottle.redirect(f'/izdelek/{st_izdelka}')
    




bottle.run(debug=True, reloader=True)
 