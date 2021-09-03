
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
        self.ocene = {}

    def dodaj_oceno(self, ocena):
        self.ocene[ocena.st]=ocena

class Ocena:
    def __init__(self,st_izdelka):
        self.ocene = {}
        self.izracunana = {}
        self.st_izdelka = st_izdelka

    def prost_id_ocene(self):
        if self.ocene:
            return max(self.ocene) + 1
        else:
             return 1


    def izracun_ocene(self):
        sum = 0
        for id_ocene in self.ocene:
            sum += self.ocene[id_ocene]["ocena"]
        self.izracunane_ocene[datetime.datetime] = sum
        return sum

    
    def nova_ocena(self, ocena, st_racuna):
        for key in self.ocene:
            if self.ocene["st_racuna"] == st_racuna:
                pass
            else:
                continue
        ocena = {"ocena": ocena, "datetime": datetime.datetime, "st_racuna": st_racuna}
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

