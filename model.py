import json
UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}
baza_prodajnih_mest = (381029)


class Izdelki:

    def __init__(self, st_izdelka, cena=None, katergorija=None, ponudba=None):
        if preveri_ce_je_veljavna_st_izdelka(st_izdelka):
        
            self.st_izdelka = st_izdelka
        if cena is not None:
            self.cena = cena
        if katergorija is not None:
            self.katergorija = katergorija
        if ponudba is not None:
            self.ponudba = ponudba


    
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


    def poisci(self, st_izdelka=None):
        rezultat = []
        for id_ocene in self.ocene:
            ocena = self.ocene[id_ocene]
            if (st_izdelka == ocena["st_izdelka"] or st_izdelka is None): #and (st_racuna == ocena["st_racuna"] or st_racuna is None)
                rezultat.append(id_ocene)
        return rezultat
    
    def izracun_ocene(self, st_izdelka):
        ocene_za_izracun = self.poisci(st_izdelka)
        sum = 0
        for id_ocene in ocene_za_izracun:
            
            sum += self.ocene[id_ocene]["ocena"]
    
        return sum

    
    def nova_ocena(self, st_izdelka, ocena):
        ocena = {"st_izdelka": st_izdelka, "ocena":ocena}
        id_ocene = self.prost_id_ocene()
        self.ocene[id_ocene] = ocena

class Racuni:
        def __init__(self, st_racuna):
        
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
            self.st_racuna = st_racuna
        
        

