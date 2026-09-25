import socket

# Creamos el socket TCP.
cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# AQUÍ PONES LA IP LOCAL DE TU SERVIDOR.
cliente.connect(("192.168.1.100", 5000))

# Enviamos un mensaje.
cliente.sendall(
    b"Hola desde el cliente"
)

# Recibimos la respuesta.
respuesta = cliente.recv(1024)

print("Servidor:", respuesta.decode())

cliente.close()