# threading module 

from threading import Thread

# from multiprocessing import Process 
# import os 
# import time


def square_numbers():
    for i in range(100):
        i * i 

    print("Processo concluído!")


if __name__ == '__main__':
    threads = []
    num_threads = 10  # Fallback caso cpu_count retorne None


    # Criamos os processos e adicionamos à lista
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)


    # Inicia todos os processos em paralelo
    for thread in threads:
        thread.start()


    # Trava a thread principal até que todos concluam
    for thread in threads:
        thread.join()


    print("Processo concluído!")
