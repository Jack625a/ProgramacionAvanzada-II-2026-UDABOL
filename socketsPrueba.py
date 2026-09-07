#Importar sockets
import socket

#Paso 1. crear el servidor
servidor=socket(socket.AF_INET,socket.SOCK_STREAM)

#Paso 2. Definir el host y el puerto
servidor.bind("127.0.0.1",5000)
#paso 3. Activar el host
servidor.listen(1)

#Paso 4. Aceptar las conexiones de los usuarios
conexion,direccion=servidor.accept()
print(f"Cliente conectado: {direccion}")

mensaje=conexion.recv(1024)

print(f"MENSAJE RECIBIDO: {mensaje.decode()}")
mensaje=input("Ingrese su mensaje")
conexion.send(mensaje.encode())

conexion.close()
servidor.close()
