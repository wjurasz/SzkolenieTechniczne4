# Zad. 10. Stwórz metaklasę Podatnik, która do klas potomnych doda składnik numer_nip.

class Podatnik(type):
    def __new__(cls, name, bases, dct):
        dct.setdefault("numer_nip", "000-000-00-00")  
        return super().__new__(cls, name, bases, dct)

class Firma(metaclass=Podatnik):
    nazwa = "XXXXX"

class OsobaFizyczna(metaclass=Podatnik):
    imie = "XX"

f = Firma()
o = OsobaFizyczna()

print("Firma NIP:", f.numer_nip)
print("Osoba NIP:", o.numer_nip)
