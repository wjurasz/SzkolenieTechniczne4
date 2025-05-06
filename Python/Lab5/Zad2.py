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
