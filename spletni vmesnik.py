import re
import bottle

import model
izdelki = model.Izdelki()
ocene = model.Ocene()

UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}
KATEGORIJE = {"A":22.5 , "B" : 9.5 , "C" : 100}
PONUDBA = ("Stalna", "Občasna")
baza_prodajnih_mest = ("381029")

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
    i = model.Ocena(st_izdelka)
    ocene.dodaj_oceno(i)
    
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
    return bottle.redirect(f'/izdelek/{st_izdelka}')


@bottle.get("/izdelek/<st_izdelka>")
def prikazi(st_izdelka):
        izdelek = izdelki.baza_izdelkov[st_izdelka]
        ocena = ocene.baza_ocen[st_izdelka]

        return bottle.template("prikazi_izdelek.tpl", izdelek=izdelek, ocena=ocena)

@bottle.get("/oceni/<st_izdelka>")
def oceni(st_izdelka):
    ocena = ocene.baza_ocen[st_izdelka]

    return bottle.template("oceni_izdelek.tpl", ocena=ocena)

@bottle.post("/oceni/<st_izdelka>")
def ocena(st_izdelka):
    st_racuna = bottle.request.forms["st_racuna"]
    rez = bottle.request.forms["ocena"]
    ocena = ocene.baza_ocen[st_izdelka]
    if ocena.nov_racun_check(st_racuna):
        rez_ocena = UTEZI[rez]
        ocena.nova_ocena(rez_ocena, st_racuna)
        ocena.izracun_ocene

        return bottle.redirect(f'/izdelek/{st_izdelka}')
    else:
        return bottle.template("st_racuna_narobe.tpl")
    
bottle.run(debug=True, reloader=True)
 