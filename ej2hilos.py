#Simular compartir datos entre hilos
import threading

contador=0
pausa=threading.Lock() #PAUSA

def incrementar():
    global contador
    for _ in range(1000000):
        with pausa:
            contador=contador+1

hilo1=threading.Thread(target=incrementar)
hilo2=threading.Thread(target=incrementar)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(contador)