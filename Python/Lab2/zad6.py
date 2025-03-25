# Zad. 6. Stwórz dynamicznie klasy jako zmienne globalne, na bazie danych zapisanych w strukturze:
# {‘Osoba’: [‘imię’, ‘nazwisko’, ‘wiek’], ‘Pojazd’: [‘marka’, ‘model’, ‘rocznik’]}.

structure = {
    'Osoba': ['imię', 'nazwisko', 'wiek'],
    'Pojazd': ['marka', 'model', 'rocznik']
}

class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Tworzenie nowej klasy {name}')

        required_attributes = ['marka', 'model']
        for attr in required_attributes:
            if attr not in dct:
                raise TypeError(f'Klasa {name} musi zawierać atrybut: {attr}')

        required_methods = ['show_info']
        for method in required_methods:
            if method not in dct or not callable(dct[method]):
                raise TypeError(f'Klasa {name} musi zawierać metodę: {method}')

        return super().__new__(cls, name, bases, dct)

globals_result = {}

for class_name, attributes in structure.items():
    class_dict = {}

    for attr in attributes:
        class_dict[attr] = f'domyślne_{attr}'

    def __init__(self, **kwargs):
        for attr in attributes:
            setattr(self, attr, kwargs.get(attr, f'domyślne_{attr}'))
    class_dict['__init__'] = __init__

    if class_name == 'Pojazd':
        def show_info(self):
            return f'Samochód: {self.marka}, {self.model}, {self.rocznik}'
        class_dict['show_info'] = show_info
        new_class = ValidateMeta(class_name, (object,), class_dict)
    else:
        new_class = type(class_name, (object,), class_dict)

    globals_result[class_name] = new_class

Osoba = globals_result['Osoba']
Pojazd = globals_result['Pojazd']

osoba = Osoba(imię="Jan", nazwisko="Kowalski", wiek=30)
pojazd = Pojazd(marka="Toyota", model="Corolla", rocznik=2020)

(osoba.__dict__, pojazd.show_info())
