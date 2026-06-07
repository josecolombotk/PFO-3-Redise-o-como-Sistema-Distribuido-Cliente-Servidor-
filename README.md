# PFO 3: Rediseño como Sistema Distribuido (Cliente-Servidor)

## Descripción

Este proyecto corresponde al Trabajo Práctico Numero 3 (PFO 3) de Programación sobre Redes. El objetivo es rediseñar un sistema originalmente centralizado para funcionar bajo una arquitectura distribuida cliente-servidor utilizando sockets en Python.

La solución implementada permite que múltiples clientes se conecten a un servidor mediante sockets TCP para enviar tareas. El servidor recibe las solicitudes y las distribuye entre un conjunto de workers que procesan las tareas de forma concurrente utilizando hilos.

## Objetivos

* Implementar comunicación cliente-servidor mediante sockets.
* Utilizar procesamiento concurrente mediante un pool de workers.
* Distribuir tareas recibidas por el servidor entre varios workers.
* Simular una arquitectura distribuida escalable.
* Comprender los conceptos de balanceo de carga, colas de mensajes y almacenamiento distribuido.

## Arquitectura del Sistema

La arquitectura propuesta está compuesta por los siguientes elementos:

### Clientes

Representan las aplicaciones que envían solicitudes al sistema. En este proyecto se implementa un cliente de consola capaz de conectarse al servidor y enviar tareas para su procesamiento.

### Balanceador de Carga

Nginx fue seleccionado como balanceador de carga en el diseño arquitectónico del sistema. Su función sería distribuir las solicitudes entrantes entre múltiples servidores workers para mejorar la escalabilidad y disponibilidad del servicio. En la implementación desarrollada para este trabajo no se configuró un balanceador real, manteniéndose como parte del diseño conceptual.

### Servidores Workers

Los servidores workers reciben las tareas distribuidas por el sistema y las procesan utilizando un pool de hilos. Cada worker puede atender solicitudes de forma independiente y concurrente.

### Cola de Mensajes

RabbitMQ se incluye en el diseño arquitectónico como mecanismo de comunicación entre servicios y distribución de tareas en entornos distribuidos.

### Almacenamiento Distribuido

* PostgreSQL: almacenamiento persistente de usuarios, tareas y resultados.
* Amazon S3: almacenamiento de archivos y recursos compartidos.

## Implementación

La implementación desarrollada para este trabajo incluye:

### servidor.py

El servidor:

* Escucha conexiones entrantes mediante sockets TCP.
* Recibe tareas enviadas por los clientes.
* Almacena las tareas en una cola compartida.
* Distribuye las tareas entre varios workers.
* Envía el resultado procesado al cliente correspondiente.

### cliente.py

El cliente:

* Se conecta al servidor mediante sockets TCP.
* Envía una tarea ingresada por el usuario.
* Recibe la respuesta generada por el worker.
* Muestra el resultado en pantalla.

## Tecnologías Utilizadas

* Python 3
* Socket Programming
* Threading
* Queue

## Ejecución

### Iniciar el servidor

```bash
python servidor.py
```

### Ejecutar un cliente

```bash
python cliente.py
```

Es posible ejecutar múltiples clientes simultáneamente para comprobar el funcionamiento concurrente del pool de workers.

## Escalabilidad

La arquitectura propuesta permite escalar horizontalmente agregando nuevos servidores workers sin modificar el funcionamiento de los clientes. Esto mejora la capacidad de procesamiento y la tolerancia a fallos del sistema.

