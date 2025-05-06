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
