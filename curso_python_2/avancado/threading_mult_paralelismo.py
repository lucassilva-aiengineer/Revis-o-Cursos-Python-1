from multiprocessing import Process 
import os 
import time


def square_numbers():
    for i in range(100):
        _ = i * i 
        time.sleep(0.1)


if __name__ == '__main__':
    processes = []
    num_process = os.cpu_count() or 2  # Fallback caso cpu_count retorne None


    # Criamos os processos e adicionamos à lista
    for i in range(num_process):
        p = Process(target=square_numbers)
        processes.append(p)


    # Inicia todos os processos em paralelo
    for p in processes:
        p.start()


    # Trava a thread principal até que todos concluam
    for p in processes:
        p.join()


    print("Processo concluído!")