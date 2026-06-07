import socket
import threading
from queue import Queue

HOST = "127.0.0.1"
PORT = 5000

# Cola  tareas
cola_tareas = Queue()

# Cantidad de workers
NUM_WORKERS = 3


def worker(worker_id):
    while True:
        conexion, direccion, tarea = cola_tareas.get()

        print(f"[Worker {worker_id}] Procesando tarea: {tarea}")

        # Simula procesamiento
        resultado = f"Worker {worker_id} procesó: {tarea.upper()}"

        conexion.send(resultado.encode())

        conexion.close()

        cola_tareas.task_done()


# Crear el pool de workers
for i in range(NUM_WORKERS):
    hilo = threading.Thread(
        target=worker,
        args=(i + 1,),
        daemon=True
    )
    hilo.start()

print(f"Pool de {NUM_WORKERS} workers iniciado.")

# Socket servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(5)

print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    conexion, direccion = servidor.accept()

    tarea = conexion.recv(1024).decode()

    print(f"Tarea recibida desde {direccion}: {tarea}")

    cola_tareas.put(
        (conexion, direccion, tarea)
    )