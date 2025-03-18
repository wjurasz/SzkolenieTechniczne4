
class MetaCar(type):
    def __new__(cls, name, bases, dct):
        print(f'Tworzenie nowej klasy: {name}')

        new_class = super().__new__(cls, name, bases, dct)

        new_class.custom_attribute = "Dodany atrybut przez metaklase"

        return new_class
    
class CustomClass(metaclass = MetaCar):
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"wartość: {self.value}"
     
newobj1 = CustomClass("1")
newobj2 = CustomClass("2")

print(newobj1.show())
print(newobj2.show())

class CarA(metaclass=MetaCar):
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"CarA - Wartość: {self.value}"

class CarB(metaclass=MetaCar):
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"CarB - Wartość: {self.value}"

class CarC(metaclass=MetaCar):
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"CarC - Wartość: {self.value}"

car1 = CarA("Opel")
car2 = CarB("Dodge")
car3 = CarC("Ford")

print(car1.show()) 
print(car2.show())  
print(car3.show())  