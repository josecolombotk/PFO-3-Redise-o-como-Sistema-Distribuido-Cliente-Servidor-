import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

tarea = input("Ingrese una tarea: ")

cliente.send(tarea.encode())

respuesta = cliente.recv(1024).decode()

print("\nResultado recibido:")
print(respuesta)

cliente.close()