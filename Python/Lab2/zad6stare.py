class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Tworzenie nowej klasy {name}')

        requrired_atrributes = ["brand", "model"]
        for attr in requrired_atrributes:
            if attr not in dct:
                raise TypeError(f'Klasa {name}, musi zawietac atrybut: {attr}')

        requrired_methods = ['show_info']
        for method in requrired_methods:
            if method not in dct or not callable(dct[method]):
                raise TypeError(f'Klasa {name}, musi zawierać metodę: {method}')    
        
        return super().__new__(cls, name, bases, dct)
    

class validCar(metaclass = ValidateMeta):
    brand = "defalutBrand"
    model = "defalutModel"
    
    def show_info(self):
        return f'Samochód: {self.brand}, {self.model}'

car = validCar()
print(car.show_info())


class notvalidCar(metaclass = ValidateMeta):
    brand = "defaultBrand"  

    def show_info(self):
        return f'Samochód: {self.brand}, {self.model}'
    
car2 = notvalidCar()
print(car2.show_info())