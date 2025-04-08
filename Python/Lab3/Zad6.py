# Zad. 6. Stwórz dekorator klasy, który doda do niej metodę `info()` wypisującą składniki klasy.

def decorator(cls):
    def info(self):
        return f"Składniki klasy {cls.__name__}: {self.__dict__}"
    setattr(cls, 'info', info)
    return cls

@decorator
class myClass:
    def __init__(self, nazwa, wartość):
        self.nazwa = nazwa
        self.wartość = wartość

obiekt = myClass("Przykład", 42)
print(obiekt.info())  
