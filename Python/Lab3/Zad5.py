# Zad. 5. Stwórz dekorator klasy, który doda do niej zmienną `licznik_obiektów`

def decorator(cls):
    cls.licznik_obiektów = 0
    
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        cls.licznik_obiektów += 1
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    
    return cls


@decorator
class myclass:
    def __init__(self, name):
        self.name = name

a = myclass("Obiekt 1")
b = myclass("Obiekt 2")
c = myclass("Obiekt 3")

print(myclass.licznik_obiektów)