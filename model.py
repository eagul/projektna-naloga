
import json
import datetime
UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}
KATEGORIJE = {"A":22.5 , "B" : 9.5 , "C" : 100}
PONUDBA = ("Stalna", "Občasna")
baza_prodajnih_mest = (381029)


def preveri_ce_je_veljavna_st_izdelka(st):
        return st.isnumeric() and len(st) >= 5 and len(st) <= 8
        


class Izdelki:

    def __init__(self):
        self.baza_izdelkov = ()


class Izdelek:

    def __init__(self, st_izdelka, ime=None, cena=None, kategorija=None, ponudba=None, opis=None):
        self.st_izdelka = st_izdelka
        self.ime = ime
        self.cena = cena
        self.kategorija = kategorija
        self.ponudba = ponudba
        self.opis = opis

    def uredi_izdelek(self, st_izdelka, cena=None, kategorija=None, ponudba=None):
        #preverjanje če je izdelek že v bazi izdelkov
        if f"{st_izdelka}" in self.baza_izdelkov:
            if self.baza_izdelkov[f"{st_izdelka}"]["cena"] == None and not cena == None:
                 self.baza_izdelkov[f"{st_izdelka}"]["cena"] = cena
            if self.baza_izdelkov[f"{st_izdelka}"]["kategorija"] == None and not kategorija == None:
                self.baza_izdelkov[f"{st_izdelka}"]["kategorija"] = kategorija
            if self.baza_izdelkov[f"{st_izdelka}"]["ponudba"] == None and not ponudba == None:
                self.baza_izdelkov[f"{st_izdelka}"]["ponudba"] = ponudba
            else:
                pass
        
       

    def zapisi_izdelke_v_datoteko(self, ime_dat): #ime datoteke naj bo string in naj se začne z "projektna naloga\\"
        with open(ime_dat, "w", encoding="utf-8") as dat:
            slovar = self.baza_izdelkov
            json.dump(slovar, dat)

    def iz_slovarja(slovar):
        u = Izdelki()
        for key in slovar:
            u.nov_izdelek(key, key["cena"], key["kategorija"], key["ponudba"])


    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Izdelki.iz_slovarja(slovar)




class Ocene:
    def __init__(self):
        self.ocene = {}
        self.izracunane_ocene = {}

    def prost_id_ocene(self):
        if self.ocene:
            return max(self.ocene) + 1
        else:
             return 1

    def poisci_id(self, st_izdelka=None):
        rezultat = []
        for id_ocene in self.ocene:
            ocena = self.ocene[id_ocene]
            if (st_izdelka == ocena["st_izdelka"] or st_izdelka is None):
                rezultat.append(id_ocene)
        return rezultat
    
    def izracun_ocene(self, st_izdelka):
        ocene_za_izracun = self.poisci_id(st_izdelka)
        sum = 0
        for id_ocene in ocene_za_izracun:
            sum += self.ocene[id_ocene]["ocena"]
        self.izracunane_ocene[st_izdelka] = sum
        return sum

    
    def nova_ocena(self, st_izdelka, ocena):
        ocena = {"st_izdelka": st_izdelka, "ocena":ocena}
        id_ocene = self.prost_id_ocene()
        self.ocene[id_ocene] = ocena

    def zapisi_ocene_v_datoteko(self, ime_dat): #ime datoteke naj bo string in naj se začne z "projektna naloga\\"
        with open(ime_dat, "w", encoding="utf-8") as dat:
            slovar = self.ocene
            json.dump(slovar, dat)

class Racuni:
        def __init__(self):
            self.baza_racunov = {}


        def nov_racun(self, st_racuna):
            #check_veljavnost dolzine
            if len(st_racuna) <  14 or len(st_racuna) > 34:
                return False

            razrez = st_racuna.split("-").split()
            nov_niz = ""
            for elemnt in razrez:
                nov_niz += elemnt
            st_racuna = nov_niz
            # check veljavnosti prodajnega mesta
            if st_racuna[:6] not in baza_prodajnih_mest:
                return False
            self.baza_racunov[st_racuna] = f"{datetime.time() ,datetime.date()}"
        
        def zapisi_racune_v_datoteko(self, ime_dat): #ime datoteke naj bo string in naj se začne z "projektna naloga\\"
            with open(ime_dat, "w", encoding="utf-8") as dat:
                slovar = self.baza_racunov
                json.dump(slovar, dat)

