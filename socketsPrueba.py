#Importar sockets
import socket
import threading

#Paso 1. crear el servidor
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Paso 2. Definir el host y el puerto
host="127.0.0.1"
puerto=5000

servidor.bind((host,puerto))
#paso 3. Activar el host
servidor.listen(1)

#Paso 4. Aceptar las conexiones de los usuarios
conexion,direccion=servidor.accept()
print(f"Cliente conectado: {direccion}")

#Funcion para recibir los mensajes

def recibirMensajes():
    while True:
        try:
            mensaje=conexion.recv(1024).decode()

            if not mensaje:
                break
            print(f"MENSAJE RECIBIDO: {mensaje}")
            
        except:
            break

#crear el hilo para recibir los mensajes
hilo=threading.Thread(target=recibirMensajes)
hilo.start()

#Accion para enviar los mensaje 
while True:
    mensaje=input("SERVIDOR: ")
    conexion.send(mensaje.encode())
    if mensaje.lower()=="":
        break
    

conexion.close()
servidor.close()
print("Servidor cerrado...")