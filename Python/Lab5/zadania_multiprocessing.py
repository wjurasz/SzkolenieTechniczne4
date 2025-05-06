import multiprocessing
import time
from multiprocessing import Lock, RLock, Condition, Semaphore, Event, Barrier

with open("dane.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

def process_line(line):
    return line.swapcase()

def lock_worker(lock, line, result_list):
    with lock:
        result_list.append(process_line(line))

def zad2_lock_example():
    manager = multiprocessing.Manager()
    results = manager.list()
    lock = Lock()
    processes = []
    for line in lines:
        p = multiprocessing.Process(target=lock_worker, args=(lock, line, results))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return list(results)

def rlock_worker(rlock, line, result_list):
    with rlock:
        result_list.append(process_line(line))

def zad3_rlock_example():
    manager = multiprocessing.Manager()
    results = manager.list()
    rlock = RLock()
    processes = []
    for line in lines:
        p = multiprocessing.Process(target=rlock_worker, args=(rlock, line, results))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    return list(results)

def condition_worker(cond, line, result_list):
    with cond:
        cond.wait()
        result_list.append(process_line(line))

def zad4_condition_example():
    manager = multiprocessing.Manager()
    results = manager.list()
    cond = Condition()
    processes = []
    for line in lines:
        p = multiprocessing.Process(target=condition_worker, args=(cond, line, results))
        processes.append(p)
        p.start()
    time.sleep(1)
    with cond:
        cond.notify_all()
    for p in processes:
        p.join()
    return list(results)




if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()

    results = {
        "Zad2_Lock": zad2_lock_example(),
        "Zad3_RLock": zad3_rlock_example(),
        "Zad4_Condition": zad4_condition_example(),
        
    }

    for key, val in results.items():
        print(f"{key}: {val}")
