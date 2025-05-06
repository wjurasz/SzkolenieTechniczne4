from time import sleep
from multiprocessing import Process,active_children, cpu_count, Lock, RLock, Barrier
from random import random

# if __name__ == '__main__':
# # utwórz proces
#     process = Process()
# # zgłoś identyfikator procesu
#     print(process.pid)
# # uruchom proces
#     process.start()
# # zgłoś identyfikator procesu
#     print(process.pid)

def task(barrier, number):
 # generate a unique value
    value = random() * 10
 # block for a moment
    sleep(value)
 # report result
    print(f'Process {number} done, got: {value}', flush=True)
 # wait on all other processes to complete
    barrier.wait()


# reporting function
def report(lock, identifier):
 # acquire the lock
 with lock:
    print(f'>process {identifier} done')
# work function
def task(lock, identifier, value):
 # acquire the lock
 with lock:
    print(f'>process {identifier} sleeping for {value}')
 sleep(value)
 # report
 report(lock, identifier)


# function to execute in a new process
def task():
 sleep(1)
if __name__ == '__main__':
 # create the process
    process = Process(target=task)
 # report the exit status
    print(process.exitcode)
 # start the process
    process.start()
 # report the exit status
    print(process.exitcode)
 # wait for the process to finish
    process.join()
 # report the exit status

 # get the number of cpu cores
    num_cores = cpu_count()
# report details
    print(num_cores)
# work function
def task(lock, identifier, value):
 # acquire the lock
 with lock:
    print(f'>process {identifier} got the lock, sleeping for {value}')
    sleep(value)
# entry point
if __name__ == '__main__':
 # create the shared lock
    lock = Lock()
 # create a number of processes with different sleep times
    processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
 # start the processes
    for process in processes:
        process.start()
 # wait for all processes to finish
    for process in processes:
        process.join()
        

        # create a shared reentrant lock
    lock = RLock()
 # create processes
    processes = [Process(target=task, args=(lock, i, random())) for i in
range(10)]
 # start child processes
    for process in processes:
        process.start()
 # wait for child processes to finish
    for process in processes:
        process.join()

        # create a barrier
    barrier = Barrier(5 + 1)
 # create the worker processes
    for i in range(5):
 # start a new process to perform some work
        worker = Process(target=task, args=(barrier, i))
        worker.start()
 # wait for all processes to finish
    print('Main process waiting on all results...')
    barrier.wait()
 # report once all processes are done
    print('All processes have their result')