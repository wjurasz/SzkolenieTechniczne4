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
