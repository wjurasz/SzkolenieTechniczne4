# Zad. 1. Stwórz dekorator do dowolnej funkcji, który będzie wypisywał informację przed i po wywołaniu funkcji.
def dekorator_zad1(func):
    def wrapper():
        print("Informacja przed wywołaniem")
        func()
        print("Informacja po wywołaniu")
    return wrapper

@dekorator_zad1
def hellowrdl():
    print("Hello")


hellowrdl()