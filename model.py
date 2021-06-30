import json
UTEZI = {"YGWYPF":1.0, "POP":1.0,"SCAM":1.0}



class Ocene:
    def __init__(self):
        self.ocene = {}
    
    def prost_id_ocene(self):
        if self.ocene:
            return max(self.ocene) + 1
        else:
             return 1





    def poisci(self, st_izdelka=None, uporabnik=None, st_racuna=None):
        rezultat = []
        for id_ocene in self.ocene:
            ocena = self.ocene[id_ocene]
            if (st_izdelka == ocena["st_izdelka"] or st_izdelka is None) and \
            (uporabnik == ocena["uporabnik"] or uporabnik is None) and \
            st_racuna == ocena["st_racuna"] or st_racuna is None):
                rezultat.append(id_ocene)
        return rezultat
    


    def nova_ocena(self, st_izdelka, ocena, uporabnik, st_racuna):
        if uporabnik == False:
            if self.poisci(st_izdelka,)
         
        ocena = {"st_izdelka":st_izdelka, "ocena":ocena, "uporabnik":uporabnik, "st_racuna":st_racuna}
        id_ocene = self.prost_id_ocene()
        self.ocene[id_ocene] = ocena


        
        

