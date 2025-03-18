class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Samochód: {self.brand} {self.model}, Rok: {self.year}"

car1 = Car("Opel","Astra",2010)
print(car1.info())


def info(self):
    return f"Samochód: {self.marka} {self.model}, Rok: {self.year}"

def dynamic_init(self, brand, model, year):
    setattr(self, "marka", brand)
    setattr(self, "model", model)
    setattr(self, "year", year)

DynamicCar = type(
    "DynamicCar",
    (object,),
    {
        "__init__": dynamic_init,  
        "info": info,
    }
)

car = DynamicCar("Renault", "Laguna", 1450)
print(car.info())  
