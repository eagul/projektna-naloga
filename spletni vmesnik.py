import bottle

import model
izdelki = model.Izdelki()


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
        try :
            izdelki.baza_izdelkov[iskalni_niz]
            return bottle.redirect(f'/izdelek/{iskalni_niz}')
        except KeyError:
            return bottle.template("dodaj_izdelek.tpl", st_izdelka=iskalni_niz)

        
#bottle.post("/st_racuna/")

@bottle.post('/dodaj_izdelek/')
def dodaj_izdelek():
    st_izdelka = bottle.request.forms["st_izdelka"]
    ime = bottle.request.forms['ime']
    cena = bottle.request.forms['cena']
    opis = bottle.request.forms['opis']
    kategorija = bottle.request.forms['kategorija']
    ponudba = bottle.request.forms['ponudba']
    u = model.Izdelek(st_izdelka)
    u.lastnosti(ime, cena, kategorija, ponudba, opis)
    izdelki.dodaj_izdelek(u)
    return bottle.redirect(f'/izdelek/{st_izdelka}')


@bottle.get('/uredi/<st_izdelka>')
def uredi(st_izdelka):
    izdelek = izdelki.baza_izdelkov[st_izdelka]
    return bottle.template("uredi_izdelek.tpl", izdelek=izdelek)


@bottle.post("/uredi_izdelek/")
def uredi_izdelek():
        
    st_izdelka = bottle.request.forms["st_izdelka"]
    ime = bottle.request.forms['ime']
    cena = bottle.request.forms['cena']
    opis = bottle.request.forms['opis']
    kategorija = bottle.request.forms['kategorija']
    ponudba = bottle.request.forms['ponudba']
    izdelek = izdelki.baza_izdelkov[st_izdelka]
    izdelek.posodobi_lastnosti(ime, cena, kategorija, ponudba, opis)
    #print(izdelek.slovar["cena"])
    #izdelki.baza_izdelkov[st_izdelka] = izdelek
    return bottle.redirect(f'/izdelek/{st_izdelka}')


@bottle.get("/izdelek/<st_izdelka>")
def prikazi(st_izdelka):
        izdelek = izdelki.baza_izdelkov[st_izdelka]
        return bottle.template("prikazi_izdelek.tpl", izdelek=izdelek)



bottle.run(debug=True, reloader=True)
 