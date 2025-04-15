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
