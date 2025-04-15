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
