# Zad. 9. Stwórz metaklasę Roślina do weryfikowania poprawności atrybutów/metod nowo tworzonych klas.
# Niech nowa klasa będzie miała możliwość posiadania naraz tylko jednego z listy
# atrybutów [energetyczna, pastewna , rekultywacyjna, ozdobna].

dozwolone_atrybuty = ["energetyczna", "pastewna", "rekultywacyjna", "ozdobna"]

class Roslina(type):
    def __new__(cls, name, bases, dct):
        znalezione = [attr for attr in dozwolone_atrybuty if attr in dct]
        if len(znalezione) > 1:
            raise TypeError(
                f"Klasa '{name}' może mieć tylko jeden z atrybutów: {dozwolone_atrybuty}. "
                f"Znaleziono: {znalezione}"
            )
        print(f"Klasa '{name}' utworzona poprawnie z atrybutami: {znalezione}")
        return super().__new__(cls, name, bases, dct)

class Slonecznik(metaclass=Roslina):
    energetyczna = True

try:
    class Mieszanka(metaclass=Roslina):
        pastewna = True
        ozdobna = True
except TypeError as e:
    print("Błąd:", e)

class Trawa(metaclass=Roslina):
    zielona = True

s = Slonecznik()
print("Czy Słonecznik jest energetyczny?", s.energetyczna)

t = Trawa()
print("Trawa ma atrybut zielona?", t.zielona)
