#PASO 1. IMPORTAR LAS LIBRERIAS
import socket
import threading

#PASO 2. CREAR EL SOCKET USUARIO
usuario=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#PASO 3 DEFINIR EL HOST Y PUERTO DEL SERVIDOR
host="127.0.0.1"
puerto=5000

#PASO 4. CONECTARNOS AL SERVIDOR
usuario.connect((host,puerto))

print("USUARIO CONECTADO")
print("Escriba 'salir' para terminar la comunicacion")

#PASO 5. FUNCION PARA RECIBIR LOS MENSAJES
def recibirMensajes():
    while True:
        try:
            mensaje=usuario.recv(1024).decode()
            if not mensaje:
                break
            print(f"SERVIDOR: {mensaje}")
            if mensaje.lower=="salir":
                print("SE CERRO LA CONEXION")
                break
        except:
            break

#PASO 6. CREAR EL HILO PARA RECIBIR MENSAJES
hilo=threading.Thread(target=recibirMensajes)
hilo.start()

#PASO 7. ENVIAR MENSAJES
while True:
    mensaje=input("USUARIO: ")
    usuario.send(mensaje.encode())

    if mensaje.lower()=="salir":
        break

usuario.close()