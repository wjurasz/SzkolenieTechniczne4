# Zad. 8. Stwórz metaklasę, która będzie powodować, że klasa stworzona na jej bazie i podająca
# jako klasa bazowa klasę Osoba doda drugą klasę bazową Niewolnik.

class Osoba:
    def kto(self):
        return "Jestem Osoba"

class Niewolnik:
    def status(self):
        return "Jestem Niewolnikiem"
    

class AutoSlaveMeta(type):
    def __new__(cls, name, bases, dct):
        if Osoba in bases and Niewolnik not in bases:
            print(f"Do klasy '{name}' dodano automatycznie Niewolnik jako bazę.")
            bases = (Osoba, Niewolnik) + tuple(b for b in bases if b is not Osoba)
        return super().__new__(cls, name, bases, dct)

class Pracownik(Osoba, metaclass=AutoSlaveMeta):
    def zawod(self):
        return "Pracuję"

class Zwierze(metaclass=AutoSlaveMeta):
    def gatunek(self):
        return "Ssaki"
    
    
pracownik = Pracownik()
zwierze = Zwierze()

print("== Pracownik ==")
print("Bazy:", [base.__name__ for base in Pracownik.__bases__])
print("Metoda kto():", pracownik.kto())
print("Metoda status():", pracownik.status())
print("Metoda zawod():", pracownik.zawod())

print("\n== Zwierze ==")
print("Bazy:", [base.__name__ for base in Zwierze.__bases__])
print("Metoda gatunek():", zwierze.gatunek())
