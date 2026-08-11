import time

def tarea(n):
    print(f"Iniciando tarea {n}")
    time.sleep(5)
    print(f"Tarea {n} finalizada")

for tareas in range(100):
    tarea(tareas)