# --------------- LABORATORIUM 2 ---------------
# Zad. 1. Sprawdź typ bazowy dla danych str, int, list, range, dict, bool, bytes, NoneType.
# Zad. 2. Zdefiniuj klasycznie za pomocą słowa kluczowego class jedną klasę i utwórz jej obiekty.
# Zad. 3. Zdefiniuj dynamicznie jedną klasę, w tym klasy z atrybutami i metodami. Stwórz jej obiekty.
# Zad. 4. Stwórz własną metaklasę. Utwórz własną metodę __new__ dla tej klasy, żeby nie dziedzi-
# czyła jej od metaklasy `type`.
# Zad. 5. Za pomocą swojej metaklasy utwórz kilka nowych klas potomnych.
# Zad. 6. Stwórz dynamicznie klasy jako zmienne globalne, na bazie danych zapisanych w strukturze:
# {‘Osoba’: [‘imię’, ‘nazwisko’, ‘wiek’], ‘Pojazd’: [‘marka’, ‘model’, ‘rocznik’]}.
# Zad. 7. Stwórz metaklasę , która przy próbie tworzenia klas na jej bazie o nazwach [Student, Wy-
# kladowca, Dziecko] stworzy klasy o nazwie Osoba.
# Zad. 8. Stwórz metaklasę, która będzie powodować, że klasa stworzona na jej bazie i podająca
# jako klasa bazowa klasę Osoba doda drugą klasę bazową Niewolnik.
# Zad. 9. Stwórz metaklasę Roślina do weryfikowania poprawności atrybutów/metod nowo tworzo-
# nych klas. Niech nowa klasa będzie miała możliwość posiadania naraz tylko jednego z listy
# atrybutów [energetyczna, pastewna , rekultywacyjna, ozdobna].
# Zad. 10. Stwórz metaklasę Podatnik, która do klas potomnych doda składnik numer_nip.
# Zad. 11. Stwórz metaklasę Roślina, która z klas potomnych będzie usuwać atrybuty [mięśnie, ner-
# wy, oczy, skóra].
# Zad. 12. Stwórz metaklasę Nazewnik do sprawdzania czy: nazwy klas zaczynają się od dużej litery;
# zmienne klas zaczynają się od małej litery; zaś metody klas od dużej litery. Gdy nie zastoso-
# wano się do tych reguł należy poprawić nazwy w nowo tworzonej klasie.
# Zad. 13. Stwórz metaklasę Plikownik, który dla nowo tworzonych klas na jej bazie będzie tworzył
# ich obiekty z atrybutami w formie plików tekstowych na dysku. W przypadku usuwania
# obiektów, niech również zostanie usunięty ten plik z dysku
# ----------------------------

from types import NoneType

# Zadanie 1
# els = (str, int, list, range, dict, bool, bytes, NoneType)
# for el in els:
#     print(type(el))

# Zadanie 2
class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Jan")
p2 = Person("Anna")
print(p1.name, p2.name)

# Zadanie 3
Cos = type(
    'Cos',
    (),
    {
        'attr': 100,
        'attr_val': lambda x: x.attr
    }
)
obj = Cos()
obj.attr_val()


# Zadanie 4
class MyMeta:
    def __new__(cls, name, bases, dct):
        obj = object.__new__(cls)
        obj.name = name
        return obj


# Zadanie 5
class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Tworzenie klasy: {name}")
        return super().__new__(cls, name, bases, dct)


class A(metaclass=CustomMeta):
    pass


class B(metaclass=CustomMeta):
    pass


# Zadanie 6
data = {
    'Osoba': ['imię', 'nazwisko', 'wiek'],
    'Pojazd': ['marka', 'model', 'rocznik']
}

for class_name, attrs in data.items():
    def __init__(self, **kwargs):
        for attr in attrs:
            setattr(self, attr, kwargs.get(attr))


    globals()[class_name] = type(class_name, (), {'__init__': __init__})

os = Osoba(imię='Jan', nazwisko='Kowalski', wiek=30)
pj = Pojazd(marka='Toyota', model='Corolla', rocznik=2020)


# Zadanie 7
class RenameMeta(type):
    def __new__(cls, name, bases, dct):
        if name in ['Student', 'Wykladowca', 'Dziecko']:
            name = 'Osoba'
        return super().__new__(cls, name, bases, dct)


class Student(metaclass=RenameMeta):
    pass


# Zadanie 8
class Niewolnik:
    pass


class AddSlaveMeta(type):
    def __new__(cls, name, bases, dct):
        if Osoba in bases:
            bases = bases + (Niewolnik,)
        return super().__new__(cls, name, bases, dct)


class Czlowiek(Osoba, metaclass=AddSlaveMeta):
    pass


# Zadanie 9
class RoslinaMeta(type):
    def __new__(cls, name, bases, dct):
        allowed = ['energetyczna', 'pastewna', 'rekultywacyjna', 'ozdobna']
        count = sum(1 for k in dct if k in allowed)
        if count > 1:
            raise TypeError("Tylko jeden atrybut rośliny może być użyty.")
        return super().__new__(cls, name, bases, dct)


class Trawa(metaclass=RoslinaMeta):
    energetyczna = True


# Zadanie 10
class PodatnikMeta(type):
    def __new__(cls, name, bases, dct):
        dct['numer_nip'] = '000-000-00-00'
        return super().__new__(cls, name, bases, dct)


class Firma(metaclass=PodatnikMeta):
    pass


# Zadanie 11
class CleanRoslinaMeta(type):
    def __new__(cls, name, bases, dct):
        for attr in ['mięśnie', 'nerwy', 'oczy', 'skóra']:
            dct.pop(attr, None)
        return super().__new__(cls, name, bases, dct)


class Kapusta(metaclass=CleanRoslinaMeta):
    skóra = 'zielona'
    liście = 'duże'


# Zadanie 12
import re


class NazewnikMeta(type):
    def __new__(cls, name, bases, dct):
        if not name[0].isupper():
            name = name.capitalize()
        new_dct = {}
        for k, v in dct.items():
            if callable(v) and not k[0].isupper():
                k = k.capitalize()
            elif not callable(v) and not k[0].islower():
                k = k[0].lower() + k[1:]
            new_dct[k] = v
        return super().__new__(cls, name, bases, new_dct)


class osoba(metaclass=NazewnikMeta):
    Imie = "Jan"

    def przywitanie(self):
        print("Cześć")


# Zadanie 13
import os


class PlikownikMeta(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        filename = f"{cls.__name__}_{id(obj)}.txt"
        obj._filename = filename
        with open(filename, "w") as f:
            for k, v in obj.__dict__.items():
                f.write(f"{k}: {v}\n")
        return obj

    def __del__(cls):
        if hasattr(cls, '_filename') and os.path.exists(cls._filename):
            os.remove(cls._filename)


class Dane(metaclass=PlikownikMeta):
    def __init__(self, x):
        self.x = x


# --------------- LABORATORIUM 3 ---------------


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

## Zad. 2. Stwórz funkcję do obliczania np. średniej dwóch liczb. Utwórz i dodaj do niej dekorator,
# który wypisze jakie argumenty zostały dostarczone do funkcji, celem weryfikacji wyniku
from time import *


# from multiprocessing import Process

def dekorator(func):
    def wrapper(*args, **kwargs):
        print(f'Liczby to = {args}')
        result = func(*args, **kwargs)
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        t3 = t2 - t1
        print(f'Czas wykonania funkcji to {t3} sekund')
        return result

    return wrapper


# Zad. 3. Stwórz kolejny dekorator, który zmierzy czas wykonania funkcji (można użyć moduł `time`)

@timer
@dekorator
def calc(a, b):
    result = a + b / 2
    sleep(1)  # zeby był czas poakzany
    return print(f'Wynik to {result}')


calc(2, 5)


# Zad. 4. Dla dowolnej klasy z metoda dodaj dekorator metody, który wypisze informacje o danej
# klasie
def info_klasy_dekorator(metoda):
    def wrapper(self, *args, **kwargs):
        print(f"Wywołanie metody: {metoda.__name__}")
        print(f"Nazwa klasy: {self.__class__.__name__}")
        print(f"Moduł: {self.__class__.__module__}")
        return metoda(self, *args, **kwargs)

    return wrapper


class Samochod:
    def __init__(self, marka):
        self.marka = marka

    @info_klasy_dekorator
    def jedz(self):
        print(f"{self.marka} jedzie!")


# Testowanie
auto = Samochod("Toyota")
auto.jedz()


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

# --------------- LABORATORIUM 4 ---------------

# Zad. 1. Uruchom dowolną funkcję w procesie
from multiprocessing import Process
from time import sleep


def calculate_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
        sleep(0.2)
    print(f"Silnia z {n} to: {result}")


if __name__ == '__main__':
    number = 5
    p = Process(target=calculate_factorial, args=(number,))
    p.start()
    p.join()
    print("Obliczenia zakończone.")

# 2. Konstruktor inicjuje zmienną wystąpienia, aby była wystąpieniem multiprocessing.Value z wartością początkową równą zero
from multiprocessing import Process, Value
from time import sleep


class CustomProcess(Process):
    def __init__(self, counter):
        super().__init__()
        self.counter = counter

    def run(self):
        for _ in range(5):
            with self.counter.get_lock():
                self.counter.value += 1
            sleep(0.5)


if __name__ == '__main__':
    shared_counter = Value('i', 0)
    process = CustomProcess(shared_counter)
    process.start()
    process.join()

    print(f"Zmienna po zakończeniu procesu: {shared_counter.value}")

# 3. Proces nadrzędny blokuje się, dopóki proces potomny nie zakończy działania.
from multiprocessing import Process
from time import sleep


class CustomProcess(Process):
    def run(self):
        print("Proces potomny: startuję")
        sleep(3)
        print("Proces potomny: zakończony.")


if __name__ == '__main__':
    print("Proces nadrzędny: uruchamiam proces potomny.")
    p = CustomProcess()
    p.start()

    print("Proces nadrzędny: czekam na zakończenie procesu potomnego")
    p.join()

    print("Proces nadrzędny: proces potomny się zakończył, kontynuuję dalej.")

# 4. Proces potomny blokuje się, a następnie zmienia wartość zmiennej wystąpienia
# i raportuje zmianę. Zmiana zmiennej wystąpienia jest propagowana z powrotem do procesu nadrzędnego.
from multiprocessing import Process, Value
from time import sleep


class CustomProcess(Process):
    def __init__(self, shared_value):
        super().__init__()
        self.shared_value = shared_value

    def run(self):
        print("Proces potomny: startuję, sleep na 3 sekundy")
        sleep(3)
        with self.shared_value.get_lock():
            self.shared_value.value = 42
            print("Proces potomny: zmieniłem wartość na 42.")


if __name__ == '__main__':
    shared_value = Value('i', 0)

    print(f"Proces nadrzędny: początkowa wartość = {shared_value.value}")
    p = CustomProcess(shared_value)
    p.start()
    p.join()

    print(f"Proces nadrzędny: po zakończeniu procesu wartość = {shared_value.value}")

# --------------- LABORATORIUM 5 ---------------

# Zad. 1. Utwórz proces i przetestuj atrybuty: nazwę, demona, pid, aktywność, kod wyjścia, procesy podrzędne.
# Laboratorium Szkolenie techniczne 4 16
# Problem: Współbieżne przetwarzanie pliku. Niech poszczególne wątki przetwarzają pojedyncze wiersze w pliku. Przetwarzanie niech polega np. na zmianie
# wielkość liter. Proces główny niech: tworzy procesy robocze; dzieli fragmenty
# pliku na części do przetworzenia przez wątki; uruchamia procesy; informuje
# użytkownika, że przetwarzanie wielowątkowe się zakończyło.
# Do rozwiązania tego problemu użyj kolejno poniższe techniki

import multiprocessing
import time
import os


def worker():
    print(f"[WORKER] Proces roboczy działa. PID: {os.getpid()}")
    time.sleep(2)
    print(f"[WORKER] Proces roboczy kończy pracę. PID: {os.getpid()}")


if __name__ == "__main__":
    print("[MAIN] Tworzenie procesu...")
    p = multiprocessing.Process(target=worker, name="MojProces")
    p.daemon = False
    p.start()

    print(f"[MAIN] Nazwa procesu: {p.name}")
    print(f"[MAIN] Czy proces jest demonem: {p.daemon}")
    print(f"[MAIN] PID procesu: {p.pid}")
    print(f"[MAIN] Czy proces żyje: {p.is_alive()}")

    p.join()

    print(f"[MAIN] Czy proces żyje po zakończeniu: {p.is_alive()}")
    print(f"[MAIN] Kod wyjścia: {p.exitcode}")

    children = multiprocessing.active_children()
    print(f"[MAIN] Procesy podrzędne (pozostałe aktywne): {[child.name for child in children]}")

    # Zad. 2. Utwórz przykład wieloprocesowy wykorzystujący blokadę Lock.
import multiprocessing
import time


def worker(lock, num):
    with lock:
        print(f"Proces {num} zablokowany")
        time.sleep(1)
        print(f"Proces {num} odblkowany ")


if __name__ == "__main__":
    lock = multiprocessing.Lock()

    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(lock, i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    print("Wszystkie procesy zakończone.")

#  Zad. 3. Utwórz przykład wieloprocesowy wykorzystujący blokadę RLock.

# Zad. 3. Przykład wieloprocesowy wykorzystujący RLock
import multiprocessing
import time


def worker(lock, counter, num):
    with lock:
        print(f"Proces {num} zablokowany")
        val = counter.value
        time.sleep(0.5)  # Symulacja pracy
        counter.value = val + 1
        print(f"Proces {num} odblokowany (licznik = {counter.value})")


if __name__ == "__main__":
    lock = multiprocessing.RLock()
    counter = multiprocessing.Value('i', 0)

    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(lock, counter, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Wszystkie procesy zakończone.")
    print(f"Wartość końcowa licznika: {counter.value}")

# Zad. 4. Utwórz przykład wieloprocesowy wykorzystujący zmienną Condition.
import multiprocessing
import time


def consumer(condition, data):
    print("Konsument: czekam na dane...")
    with condition:
        condition.wait()  # Czeka na sygnał od producenta
        print(f"Konsument: otrzymałem dane: {data.value}")


def producer(condition, data):
    print("Producent: przygotowuję dane...")
    time.sleep(2)  # Symulacja pracy
    with condition:
        data.value = 42
        print("Producent: dane gotowe, wysyłam sygnał.")
        condition.notify()  # Powiadamia konsumenta


if __name__ == "__main__":
    condition = multiprocessing.Condition()
    data = multiprocessing.Value('i', 0)

    p1 = multiprocessing.Process(target=consumer, args=(condition, data))
    p2 = multiprocessing.Process(target=producer, args=(condition, data))

    p1.start()
    time.sleep(0.1)  # Upewnia się, że konsument czeka zanim producent wyśle
    p2.start()

    p1.join()
    p2.join()

    print("Zakończono przetwarzanie.")

# Zad. 5. Utwórz przykład wieloprocesowy wykorzystujący blokadę Semafor.
# Zad. 5. Przykład z multiprocessing.Semaphore
import multiprocessing
import time
import random


def print_job(sem, process_id):
    print(f"Proces {process_id} czeka na dostęp do drukarki...")
    with sem:
        print(f"Proces {process_id} drukuje...")
        time.sleep(random.uniform(0.5, 1.5))  # Symulacja drukowania
        print(f"Proces {process_id} zakończył drukowanie.")


if __name__ == "__main__":
    semaphore = multiprocessing.Semaphore(2)  # Tylko 2 procesy mogą jednocześnie drukować
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=print_job, args=(semaphore, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Wszystkie zadania drukowania zakończone.")

# Zad. 6. Utwórz przykład wieloprocesowy wykorzystujący blokadę Event.
# Zad. 6. Przykład z multiprocessing.Event – Start wyścigu
import multiprocessing
import time
import random


def runner(event, runner_id):
    print(f"Biegacz {runner_id} gotowy na starcie.")
    event.wait()  # Czeka na sygnał startu
    print(f"Biegacz {runner_id} wystartował!")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Biegacz {runner_id} zakończył bieg.")


def starter(event):
    print("Sędzia: przygotować się...")
    time.sleep(2)
    print("Sędzia: start!")
    event.set()  # Wysyła sygnał startu


if __name__ == "__main__":
    start_event = multiprocessing.Event()

    runners = [multiprocessing.Process(target=runner, args=(start_event, i)) for i in range(4)]
    judge = multiprocessing.Process(target=starter, args=(start_event,))

    for r in runners:
        r.start()
    judge.start()

    for r in runners:
        r.join()
    judge.join()

    print("Wyścig zakończony.")

# Zad. 7. Utwórz przykład wieloprocesowy wykorzystujący blokadę Barrier.
# Zad. 7. Przykład z multiprocessing.Barrier – Zgrana drużyna
import multiprocessing
import time
import random


def team_member(barrier, member_id):
    print(f"Członek {member_id} przygotowuje się...")
    time.sleep(random.uniform(0.5, 1.5))  # Każdy przygotowuje się różnie
    print(f"Członek {member_id} gotowy, czeka na resztę...")
    barrier.wait()  # Czekanie na wszystkich członków
    print(f"Członek {member_id} zaczyna zadanie!")


if __name__ == "__main__":
    num_members = 4
    barrier = multiprocessing.Barrier(num_members)

    processes = [multiprocessing.Process(target=team_member, args=(barrier, i)) for i in range(num_members)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Wszyscy członkowie rozpoczęli zadanie.")

# --------------- LABORATORIUM 6 ---------------

# Zad. 1. Rozwiąż poniższy problem z poprzednich zajęć przy użyciu multiproces-
# sing.Pool.
# Problem: Współbieżne przetwarzanie pliku. Niech poszczególne wątki przetwa-
# rzają pojedyncze wiersze w pliku. Przetwarzanie niech polega np. na zmianie
# wielkość liter. Proces główny niech: tworzy procesy robocze; dzieli fragmenty
# pliku na części do przetworzenia przez wątki; uruchamia procesy; informuje
# użytkownika, że przetwarzanie wielowątkowe się zakończyło.

import multiprocessing


def process_line(line):
    return line.upper()


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with multiprocessing.Pool() as pool:
        processed_lines = pool.map(process_line, lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(processed_lines)

    print("Przetwarzanie wieloprocesowe zakończone.")


if __name__ == "__main__":
    main()

# Zad. 2. Zmień jasność obrazku wczytanego z pliku za pomocą puli procesów. Należy
# obraz podzielić na części i przetworzyć każdą część równolegle, ostatecznie po-
# łączyć wyniki i zapisać rezultat do pliku.

from multiprocessing import Pool
from PIL import Image
import numpy as np


def adjust_brightness(segment_data, factor):
    segment_array = np.array(segment_data, dtype=np.uint8)
    adjusted = np.clip(segment_array * factor, 0, 255).astype(np.uint8)
    return adjusted.tolist()


def split_image(image_array, num_chunks):
    height = image_array.shape[0]
    chunk_height = height // num_chunks
    chunks = []
    for i in range(num_chunks):
        start = i * chunk_height
        end = (i + 1) * chunk_height if i != num_chunks - 1 else height
        chunks.append(image_array[start:end])
    return chunks


def main():
    brightness_factor = 1.5
    num_processes = 4
    input_path = "sample_image.png"
    output_path = "brightened_image.png"

    image = Image.open(input_path).convert("RGB")
    image_array = np.array(image)

    segments = split_image(image_array, num_processes)
    args = [(segment, brightness_factor) for segment in segments]

    with Pool(processes=num_processes) as pool:
        processed_segments = pool.starmap(adjust_brightness, args)

    result_array = np.vstack(processed_segments)
    result_image = Image.fromarray(np.array(result_array, dtype=np.uint8))

    result_image.save(output_path)
    print(f"Zapisano wynikowy obraz: {output_path}")


if __name__ == "__main__":
    main()

# Zad. 3. Stwórz program, który łączy się z 10 różnymi stronami HTTP, np.
# http://interia.pl itp; pobiera treść stron i wypisuje wielkość strony. Należy użyć
# pulę procesów do równoległego wykonania połączeń. Do połączeń można użyć
# modułu requests i funkcji requests.get(url).

import requests
from multiprocessing import Pool

urls = [
    "http://interia.pl",
    "http://wp.pl",
    "http://onet.pl",
    "http://gazeta.pl",
    "http://o2.pl",
    "http://tvn24.pl",
    "http://polsatnews.pl",
    "http://money.pl",
    "http://rmf24.pl",
    "http://radiozet.pl"
]


def fetch_size(url):
    try:
        response = requests.get(url, timeout=5)
        return (url, len(response.text))
    except Exception as e:
        return (url, f"Error: {e}")


if __name__ == "__main__":
    with Pool(processes=5) as pool:
        results = pool.map(fetch_size, urls)

    for url, size in results:
        print(f"{url} => {size} bajtów")

# Zad. 4. Stwórz program, który znajdzie wśród plików w podanym katalogu zadaną
# frazę przy użyciu puli procesów.

import os
from multiprocessing import Pool


def search_in_file(args):
    filepath, phrase = args
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                if phrase in line:
                    return f"{filepath} (linia {i}): {line.strip()}"
    except Exception as e:
        return f"{filepath}: Błąd - {e}"
    return None


def find_phrase_in_dir(directory, phrase):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    with Pool() as pool:
        results = pool.map(search_in_file, [(path, phrase) for path in file_paths])

    matches = [res for res in results if res]

    if matches:
        for match in matches:
            print(match)
    else:
        print("Nie znaleziono")


if __name__ == "__main__":
    dir_path = input("Podaj ścieżkę do katalogu: ")
    phrase = input("Podaj słowo do wyszukania: ")

    find_phrase_in_dir(dir_path, phrase)

# Zad. 5. Stwórz program, który w liście danych znajdzie zadaną wartość. Należy użyć
# procesów do przyśpieszenia wyszukania. Niech w przypadku znalezienia warto-
# ści przeszukanie zostanie zakończone (przez wszystkie procesy), a wynik zosta-
# nie wyświetlony.

import multiprocessing
import numpy as np


def search_chunk(chunk, target, queue):
    for index, value in enumerate(chunk):
        if value == target:
            queue.put((multiprocessing.current_process().name, index, value))
            break  # zakończ lokalnie
    return


def parallel_search(data, target, num_chunks=4):
    chunk_size = len(data) // num_chunks
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

    manager = multiprocessing.Manager()
    result_queue = manager.Queue()
    processes = []

    for chunk in chunks:
        p = multiprocessing.Process(target=search_chunk, args=(chunk, target, result_queue))
        p.start()
        processes.append(p)

    found = result_queue.get()  # blokujące czekanie na pierwszy wynik

    for p in processes:
        p.terminate()

    print(f"Znaleziono: proces {found[0]}, indeks w swoim kawałku: {found[1]}, wartość: {found[2]}")


if __name__ == "__main__":
    data = np.random.randint(0, 1000000, size=1_000_000)
    target_value = int(input("Podaj wartość do wyszukania: "))
    parallel_search(data.tolist(), target_value)

# Zad. 6. Stwórz duży zestaw danych np. poprzez numpy.random.rand(). Podziel ten
# zbiór na mniejsze części, np. przy użyciu np.split(). Zsumuj wszystkie elementy
# tablicy przy użyciu puli procesów, wypisz wynik.

from multiprocessing import Pool
import numpy as np


def sum_chunk(chunk):
    return np.sum(chunk)


def parallel_sum(array, num_chunks=4):
    chunks = np.array_split(array, num_chunks)

    with Pool(processes=num_chunks) as pool:
        partial_sums = pool.map(sum_chunk, chunks)

    total = sum(partial_sums)
    print(f"Suma wszystkich elementów: {total}")


if __name__ == "__main__":
    data = np.random.rand(10_000_000)  # 10 milionów liczb
    parallel_sum(data)

# --------------- LABORATORIUM 7 - --------------

import ray
# import time
# import numpy as np
# import os

ray.init(ignore_reinit_error=True)


# Zadanie 1: Przetestuj podane przykłady (dokumentacja zawiera wiele)
# Uwaga: Pominięto, ponieważ przykłady są opisowe i częściowo pokrywają się z pozostałymi zadaniami.

# Zadanie 2: Suma dużej tablicy
@ray.remote
def sum_chunk(chunk):
    return np.sum(chunk)


def sum_large_array():
    data = np.random.rand(10_000_000)
    chunks = np.array_split(data, 10)
    futures = [sum_chunk.remote(chunk) for chunk in chunks]
    return sum(ray.get(futures))


# Zadanie 3: Wyszukiwanie wartości w danych
@ray.remote
def search_chunk(data_chunk, value):
    return value in data_chunk


def search_value_parallel(data, value):
    chunks = np.array_split(data, 10)
    futures = [search_chunk.remote(chunk, value) for chunk in chunks]
    results = ray.get(futures)
    return any(results)


# Zadanie 4: Wyszukiwanie frazy w plikach
@ray.remote
def search_phrase_in_file(path, phrase):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return path if phrase in content else None
    except Exception:
        return None


def find_phrase_in_directory(directory, phrase):
    files = [os.path.join(directory, f) for f in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, f))]
    futures = [search_phrase_in_file.remote(path, phrase) for path in files]
    results = ray.get(futures)
    return [r for r in results if r is not None]


# Przykładowe użycie:
# print(sum_large_array())
# print(search_value_parallel(np.random.randint(0, 100, 10000), 42))
# print(find_phrase_in_directory(".", "import"))


# --------------- LABORATORIUM 8 ---------------

# Zadanie 1: Przetestuj podane przykłady (fragmenty wymagają uruchomienia ręcznego lub kopiowania z dokumentu)

# Zadanie 2: Zmiana jasności obrazka z przetwarzaniem rozproszonym
import ray
import numpy as np
from PIL import Image

ray.init(ignore_reinit_error=True)


@ray.remote
def adjust_brightness(chunk, factor):
    return np.clip(chunk * factor, 0, 255).astype(np.uint8)


def split_image(img_array, parts):
    return np.array_split(img_array, parts, axis=0)


def merge_image(chunks):
    return np.vstack(chunks)


def process_image(input_path, output_path, brightness_factor=1.2, parts=4):
    img = Image.open(input_path).convert("RGB")
    img_array = np.array(img)
    chunks = split_image(img_array, parts)
    futures = [adjust_brightness.remote(chunk, brightness_factor) for chunk in chunks]
    result = ray.get(futures)
    final_img = Image.fromarray(merge_image(result))
    final_img.save(output_path)


# Przykład użycia:
# process_image("input.jpg", "output.jpg")

# Zadanie 3: Równoległe pobieranie stron i wyświetlanie ich rozmiarów
import requests

urls = [
    "http://interia.pl", "http://wp.pl", "http://onet.pl", "http://gazeta.pl", "http://o2.pl",
    "http://tvn24.pl", "http://rmf24.pl", "http://money.pl", "http://polsatnews.pl", "http://se.pl"
]


@ray.remote
def fetch_url_size(url):
    try:
        response = requests.get(url, timeout=5)
        return (url, len(response.content))
    except Exception as e:
        return (url, f"Błąd: {e}")


def check_websites(url_list):
    results = ray.get([fetch_url_size.remote(url) for url in url_list])
    for url, size in results:
        print(f"{url}: {size} bajtów")

# Przykład użycia:
# check_websites(urls)