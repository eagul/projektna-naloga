
import json
import datetime
UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}
KATEGORIJE = {"A":22.5 , "B" : 9.5 , "C" : 100}
PONUDBA = ("Stalna", "Občasna")
baza_prodajnih_mest = ("381029")


def preveri_ce_je_veljavna_st_izdelka(st):
        return st.isnumeric() and len(st) >= 5 and len(st) <= 8
        


class Izdelki:

    def __init__(self):
        self.baza_izdelkov = {}


    def dodaj_izdelek(self, izdelek):
        self.baza_izdelkov[izdelek.st_izdelka] = izdelek

    def uredi_lastnosti_izdelka(self, izdelek):
        self.baza_izdelkov[izdelek.st_izdelka] = izdelek


class Izdelek:

    def __init__(self, st_izdelka):
        self.st_izdelka = st_izdelka

    def lastnosti(self, ime=None, cena=None, kategorija=None, ponudba=None, opis=None):
        self.ime = ime
        self.cena = cena
        self.kategorija = kategorija
        self.ponudba = ponudba
        self.opis = opis
        self.slovar = {"ime": ime, "cena": cena, "kategorija": kategorija, "ponudba" : ponudba, "opis": opis}

    def posodobi_lastnosti(self, ime=None, cena=None, kategorija=None, ponudba=None, opis=None):
        if not self.ime and ime:
            self.ime = ime
            self.slovar["ime"] = ime
        if not self.cena and cena:
            self.cena = cena
            self.slovar["cena"] = cena
        if not self.kategorija and kategorija:
            self.kategorija = kategorija
            self.slovar["kategorija"] = kategorija
        if not self.ponudba and ponudba:
            self.ponudba = ponudba
            self.slovar["ponudba"] = ponudba
        if not self.opis and opis:
            self.opis = opis
            self.slovar["opis"] = opis
        
       

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
        self.baza_ocen = {}

    def dodaj_oceno(self, ocena):
        self.baza_ocen[ocena.st_izdelka]=ocena

class Ocena:
    def __init__(self,st_izdelka):
        self.ocene_izdelka = {}
        self.izracunana = 0
        self.st_izdelka = st_izdelka
        self.baza_racunov = set()

    def prost_id_ocene(self):
        if self.ocene_izdelka:
            return max(self.ocene_izdelka) + 1
        else:
             return 1


    def nov_racun_check(self, st_racuna):
            #check_veljavnost dolzine
            if len(st_racuna) <  14 or len(st_racuna) > 34:
                return False
            # check veljavnosti prodajnega mesta
            if st_racuna[:6] not in baza_prodajnih_mest:
                return False
            if not st_racuna in self.baza_racunov:
                self.baza_racunov.add(st_racuna)
                return True

    def izracun_ocene(self):
        sum = 0
        count = 0
        for id_ocene in self.ocene_izdelka:
            count += 1
            sum += self.ocene_izdelka[id_ocene]["ocena"]
        self.izracunana = sum // count
        return sum // count

    
    def nova_ocena(self, ocena, st_racuna):
        ocena = {"ocena": ocena, "datetime": datetime.datetime, "st_racuna": st_racuna}
        id_ocene = self.prost_id_ocene()
        self.ocene_izdelka[id_ocene] = ocena
       

    def zapisi_ocene_v_datoteko(self, ime_dat): #ime datoteke naj bo string in naj se začne z "projektna naloga\\"
        with open(ime_dat, "w", encoding="utf-8") as dat:
            slovar = self.ocene_izdelka
            json.dump(slovar, dat)

