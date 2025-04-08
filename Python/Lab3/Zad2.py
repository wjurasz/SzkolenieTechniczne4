# Zad. 2. Stwórz funkcję do obliczania np. średniej dwóch liczb. Utwórz i dodaj do niej dekorator,
# który wypisze jakie argumenty zostały dostarczone do funkcji, celem weryfikacji wyniku
from time import time
from multiprocessing import Process  # lub inna konkretna klasa/funkcja


num1 = 4
num2 = 5
num3 = 2

def dekorator(func):
    def wrapper(*args, **kwargs):
        print(f'Liczby to = {args}')
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        time_elapsed = t2 - t1
        print(f'Czas wykonania funkcji to {time_elapsed} sekund')
        return result
    return wrapper
        

# Zad. 3. Stwórz kolejny dekorator, który zmierzy czas wykonania funkcji (można użyć moduł `time`)

@timer
@dekorator
def calc(num1, num2, num3):
    import time
    result = num1 * num2 / num3
    time.sleep(1)
    print(f'Wynik: {result}')
    return result

calc(num1,num2,num3)
  