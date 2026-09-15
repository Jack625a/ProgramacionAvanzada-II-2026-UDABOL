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
servidor.listen()

print("SERVIDOR ACTIVO")
print(f"{host}:{puerto}")

usuarios=[]

#Paso extra. funcion para envio simultaneo
def enviarTodos(mensaje,usuarioActual=None):
    for usuario in usuarios:
        if usuario != usuarioActual:
            try:
                usuario.send(mensaje.encode())
            except:
                usuarios.remove(usuario)

#Paso extra. Funcion para obtener las conexiones
def atender(conexion,direccion):
    print(f"USUARIO CONECTADO: {direccion}")
    usuarios.append(conexion) #agregamos al usuario a la lista de peticiones
    mensaje=f"Usuario {direccion} se conecto al chat..."
    enviarTodos(mensaje,conexion)
    while True:
        try:
            mensaje=conexion.recv(1024).decode()
            if not mensaje:
                break
            print(f"{direccion}: {mensaje}")
            if mensaje.lower()=="salir":
                break
            mensajeCompleto=f"Usuario {direccion}: {mensaje}"
            enviarTodos(mensajeCompleto,conexion)
        except:
            break
    if conexion in usuarios:
        usuarios.remove(conexion)
    conexion.close()
    print(f"Usuario desconectado {direccion}")
    

while True:
    conexion,direccion=servidor.accept()

    #crear el hilo para recibir los mensajes
    hilo=threading.Thread(target=atender,args=(conexion,direccion))
    hilo.start()
    print(f"Usuarios conectados: {len(usuarios)}")
    
