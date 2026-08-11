import time
from threading import Thread

def tarea(n):
    print(f"Iniciando tarea {n}")
    time.sleep(5)
    print(f"Tarea {n} finalizada")

hilos=[]

for a in range(1,1000):
    hilo=Thread(target=tarea,args=(a,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()



    