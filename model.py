
import json
import datetime
UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}
KATEGORIJE = {"A":22.5 , "B" : 9.5 , "C" : 100}
PONUDBA = ("Stalna", "Občasna")
baza_prodajnih_mest = (381029)


class Izdelki:

    def __init__(self):
        self.baza_izdelkov = {}

    def nov_izdelek(self, st_izdelka, cena=None, katergorija=None, ponudba=None):
        #preverjanje če je izdelek že v bazi izdelkov
        if f"{st_izdelka}" in self.baza_izdelkov:
            if self.baza_izdelkov[f"{st_izdelka}"]["cena"] == None and not cena == None:
                 self.baza_izdelkov[f"{st_izdelka}"]["cena"] = cena
            if self.baza_izdelkov[f"{st_izdelka}"]["kategorija"] == None and not katergorija == None:
                self.baza_izdelkov[f"{st_izdelka}"]["kategorija"] = katergorija
            if self.baza_izdelkov[f"{st_izdelka}"]["ponudba"] == None and not ponudba == None:
                self.baza_izdelkov[f"{st_izdelka}"]["ponudba"] = ponudba
            else:
                pass
        
        nov_slovar = {}
        if preveri_ce_je_veljavna_st_izdelka(str(st_izdelka)):
            if cena is not None:
                nov_slovar["cena"] = cena
            elif katergorija is not None:
                nov_slovar["katergorija"] = katergorija
            elif ponudba is not None:
                nov_slovar["ponudba"] = ponudba
            self.baza_izdelkov[f"{st_izdelka}"] = nov_slovar

    def zapisi_izdelke_v_datoteko(self, ime_dat): #ime datoteke naj bo string in naj se začne z "projektna naloga\\"
        with open(ime_dat, "w", encoding="utf-8") as dat:
            slovar = self.baza_izdelkov
            json.dump(slovar, dat)

    
def preveri_ce_je_veljavna_st_izdelka(st):
        return st.isnumeric() and len(st) >= 5 and len(st) <= 8
        

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
        
        

