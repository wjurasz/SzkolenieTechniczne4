from time import sleep
from multiprocessing import Process
from multiprocessing import Value


class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
# zainicjuj atrybut całkowity
        self.data = Value('i', 0)
# nadpisz funkcję run
    def run(self):
        sleep(1)
        self.data.value = 99
        print(f'Child stored: {self.data.value}')
if __name__ == '__main__':
# utwórz proces
    process = CustomProcess()
# uruchom proces
    process.start()
# poczekaj na zakończenie procesu
    print('Czekam na zakończenie procesu potomnego')
# czekaj, dopóki proces potomny nie zostanie zakończony
    process.join()
# zgłoś atrybut procesu
print(f'Parent got: {process.data.value}')