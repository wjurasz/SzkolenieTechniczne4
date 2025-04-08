# Zad. 7. Stwórz klasę i wykorzystaj wbudowane dekoratory: staticmethod, classmethod, property.
# Przetestuj składniki na obiektach.

from decorators import trycatch, timer, singleton
from log_calls import log, log_calls

class Car:

    def __init__(self, brand, yearofProduction):
        self.brand = brand
        self.yearofProduction = yearofProduction
        Car.carCount += 1

    @staticmethod
    @log
    @trycatch
    @timer
    @singleton
    def service():
        print("Pamiętaj o przeglądzie samochodu")

    @classmethod
    @log
    @trycatch
    @timer
    @singleton
    def get_car_count(cls):
        return f'Aktualnie jest {cls.carCount} samochodów.'
    
    @property
    @log
    @trycatch
    @timer
    @singleton
    def age(self):
        return 2025 - self.yearofProduction
    
    carCount = 0  

car1 = Car("Toyota", 2010)
car2 = Car("BMW", 2015)

Car.service()
print(Car.get_car_count())
print(f"Wiek samochodu {car1.brand}: {car1.age} lat")
print(f"Wiek samochodu {car2.brand}: {car2.age} lat")
