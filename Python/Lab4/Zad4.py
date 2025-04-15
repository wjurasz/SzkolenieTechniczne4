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
