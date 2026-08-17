import threading #Para el uso de hilos
import time

def procesarArchivos(nombre):
    print(f"Inciando procesamiento {nombre}")
    time.sleep(2)
    print(f"Finalizado: Archivo procesado {nombre}")

archivos=[
    "archivo1.txt",
    "archivo2.txt",
    "archivo3.txt",
    "archivo4.txt",
    "archivo5.txt"
] 

inicio=time.time()

hilos=[]

for archivo in archivos:
    hilo=threading.Thread(target=procesarArchivos,args=(archivo,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

final=time.time()

print(f"Tiempo total de Procesamiento {final - inicio} segundo")