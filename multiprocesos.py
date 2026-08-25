from multiprocessing import Process

def preparar():
    print("Se esta preparando la comida")

def entregar():
    print("Se esta entregando el pedido")

def atender():
    print("Se esta atendiendo a los clientes")

def cobrar():
    print("Se esta cobrando")

if __name__=="__main__":
    cocina=Process(target=preparar)
    entrega=Process(target=(entregar))
    atiende=Process(target=(atender))
    cobra=Process(target=(cobrar))

    cocina.start()
    entrega.start()
    atiende.start()
    cobra.start()

    cocina.join()
    entrega.join()
    atiende.join()
    cobra.join()
    print("Todos los procesos completados")