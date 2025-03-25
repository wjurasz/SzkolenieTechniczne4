# Zad. 7. Stwórz metaklasę ,
# która przy próbie tworzenia klas na jej bazie o nazwach [Student, Wykladowca, Dziecko] stworzy klasy o nazwie Osoba.

class RenameToOsobaMeta(type):
    def __new__(cls, name, bases, dct):
        if name in ["Student", "Wykladowca", "Dziecko"]:
            print(f"Zmieniono nazwę klasy '{name}' na 'Osoba'")
            name = "Osoba"
        else:
            print(f"Tworzenie klasy o nazwie: {name}")
        return super().__new__(cls, name, bases, dct)

class Student(metaclass=RenameToOsobaMeta):
    rola = "Student"

class Wykladowca(metaclass=RenameToOsobaMeta):
    rola = "Wykladowca"

class Dziecko(metaclass=RenameToOsobaMeta):
    wiek = 10

class InnaKlasa(metaclass=RenameToOsobaMeta):
    test = True

print(Student.__name__)      
print(Wykladowca.__name__)   
print(Dziecko.__name__)     
print(InnaKlasa.__name__)    
