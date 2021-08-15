from model import Ocene
import model
ocene = Ocene()
def tekstovni_umesnik():
    
    while True:
        osnovni_zaslon()

def zahtevaj_st_izdelka():
    st = input("Vnesi številko izdelka:")
    while not model.preveri_ce_je_veljavna_st_izdelka(st):
        print("stevilka izdelka ni veljavna, vnseite novo številko izdelka")
        st = input("Vnesi številko izdelka:")
    return st

def zahtevaj_oceno():
    return int(input("vnesi številsko vrednost ocene:   "))



def osnovni_zaslon():
    print("POHOFERCENI")

    st_izdelka = zahtevaj_st_izdelka()
    
    if ocene.poisci(st_izdelka) == []:
        ocena = zahtevaj_oceno()
        ocene.nova_ocena(st_izdelka, ocena)
        return print(ocene.izracun_ocene(st_izdelka))
    else:
        return print(f"ocena tega izdelka je : {ocene.izracun_ocene(st_izdelka)}")

tekstovni_umesnik()