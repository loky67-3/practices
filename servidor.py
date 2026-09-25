import socket

# Creamos el socket
servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# 0.0.0.0 significa:
# "escuchar conexiones en las interfaces de esta computadora"
servidor.bind(("0.0.0.0", 5000))

# Ponemos el socket en modo escucha.
servidor.listen(1)

print("Esperando conexión...")
print("Puerto: 5000")

# accept() espera hasta que un cliente se conecte.
conexion, direccion = servidor.accept()

print(f"Conectado: {direccion}")

# Recibimos datos.
datos = conexion.recv(1024)

print("Mensaje:", datos.decode())

# Respondemos al cliente.
conexion.sendall(
    b"Hola desde el servidor"
)

# Cerramos la conexión.
conexion.close()
servidor.close()