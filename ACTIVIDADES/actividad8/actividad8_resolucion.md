## Ejercicios
## 1 . Coherencia de caché: Explica cómo se mantiene la coherencia de caché en un sistema de memoria compartida utilizando el protocolo MESI. Incluya ejemplos de transiciones de estados de caché cuando dos procesadores acceden y modifican la misma línea de caché.

Respuesta Esperada:

Debea describir los cuatro estados del protocolo MESI (Modificado, Exclusivo, Compartido, Inválido) y explicar las transiciones de estados cuando:
- Un procesador lee una línea de caché por primera vez.
- Un segundo procesador lee la misma línea de caché.
- El primer procesador modifica la línea de caché.
- El segundo procesador intenta leer la línea de caché modificada.

## MI RESPUESTA:

- Modificado (M): La línea de caché ha sido modificada por el procesador y es la única copia válida en el sistema. El procesador tiene permiso para escribir en la línea.

- Exclusivo (E): La línea de caché es la única copia válida en el sistema, pero no ha sido modificada.

- Compartido (S): La línea de caché está presente en la caché de más de un procesador y no ha sido modificada.

- Inválido (I): La línea de caché no contiene datos válidos.

ESTE ES UN EJEMPLO DE TRANSICIONES DE ESTADOS DE CACHE:

- Un procesador lee una línea de caché por primera vez:

    La línea de caché inicialmente se encontraba en estado Inválido (I).
    Cuando el procesador realiza la lectura, la línea pasa al estado Exclusivo (E), ya que es la única copia válida en el sistema.

- Un segundo procesador lee la misma línea de caché:

    Cuando el segundo procesador intenta leer la línea, el protocolo MESI detecta que ya existe una copia válida.
    La línea de caché pasa al estado Compartido (S), ya que ahora hay dos copias válidas en el sistema.

- El primer procesador modifica la línea de caché:

    Cuando el primer procesador modifica la línea, el protocolo MESI detecta el cambio y actualiza el estado de la línea a Modificado (M).
    Ahora, el primer procesador tiene permiso para escribir en esa línea de caché, y es la única copia válida en el sistema.

- El segundo procesador intenta leer la línea de caché modificada:

    Cuando el segundo procesador intenta leer la línea de caché, el protocolo MESI detecta que la copia en la caché del primer procesador está modificada.
    El protocolo MESI invalida la copia del segundo procesador, llevándola al estado Inválido (I).
    Luego, el protocolo MESI transfiere la copia modificada del primer procesador al segundo procesador, actualizando el estado de la línea en el segundo procesador a Compartido (S).

De esta manera, el protocolo MESI mantiene la coherencia de caché, asegurando que todas las copias de una línea de caché sean coherentes y que las actualizaciones se propaguen correctamente entre los diferentes procesadores.

## 2 . Implementa un programa en C utilizando POSIX threads (pthread) que demuestre el uso de mutexes para proteger una variable compartida. El programa debe crear varios hilos que incrementen una variable global compartida de manera segura.
------------------------
import threading

NUM_THREADS = 5
NUM_INCREMENTS = 1000000

shared_variable = 0
lock = threading.Lock()

def increment():
    global shared_variable
    for _ in range(NUM_INCREMENTS):
        with lock:
            shared_variable += 1

threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final value of shared_variable: {shared_variable}")
-------------------------------------
## 3 . Describe los diferentes modelos de consistencia de memoria (consistencia estricta, consistencia secuencial, consistencia causal) y cómo afectan el comportamiento observable de los programas en un sistema de memoria compartida.

Respuesta Esperada:

Debes explicar:

- Consistencia estricta: Todas las operaciones de memoria son vistas por todos los procesadores en el orden exacto en que ocurren.
- Consistencia secuencial: Las operaciones de memoria de todos los procesadores se intercalan en un orden secuencial que es consistente con el orden de programa de cada procesador.
- Consistencia causal: Solo las operaciones de memoria que son causalmente relacionadas deben ser vistas en el mismo orden por todos los procesadores.
## MI RESPUESTA:
## cómo afectan el comportamiento observable de los programas:

- Consistencia estricta (Strict Consistency):

    Todas las operaciones de memoria se ven en el orden exacto en que ocurren.
    Comportamiento más predecible, pero difícil de implementar eficientemente.

- Consistencia secuencial (Sequential Consistency):

    Las operaciones se intercalan en un orden secuencial consistente con cada procesador.
    Más relajado que la consistencia estricta, permite optimizaciones.
    Comportamiento ligeramente menos predecible.

- Consistencia causal (Causal Consistency):

    Solo las operaciones causalmente relacionadas deben verse en el mismo orden.
    Más relajado que la consistencia secuencial, permite mayor paralelismo.
    Comportamiento más impredecible, con reordenes de operaciones no relacionadas.

A medida que se relaja el modelo de consistencia, se permite una mayor optimización y paralelismo, pero el comportamiento observable de los programas se vuelve menos predecible. Los programadores deben considerar estos trade-offs al diseñar sistemas de memoria compartida.

## 4 . Explica cómo el paso de mensajes en un sistema de memoria distribuida permite la comunicación entre nodos. Describa las ventajas y desventajas del paso de mensajes comparado con la memoria compartida.

Respuesta Esperada:

Debes explicar:

- Cómo los nodos envían y reciben mensajes para compartir datos.
- Ventajas: No requiere coherencia de caché, escalabilidad mejorada, adecuado para sistemas distribuidos.
- Desventajas: Latencia en la comunicación, mayor complejidad en la programación, sobrecarga de comunicación.

## MI RESPUESTA
## En un sistema de memoria distribuida, los nodos se comunican entre sí mediante el paso de mensajes:

- Los nodos envían y reciben mensajes para compartir datos y coordinar tareas.
- Librerías como MPI (Message Passing Interface) facilitan la comunicación entre nodos.

## Ventajas del paso de mensajes:

No requiere mantener coherencia de caché, ya que cada nodo tiene su propia memoria.
Mejor escalabilidad que la memoria compartida, ya que la comunicación se realiza de manera explícita entre nodos.
Adecuado para sistemas distribuidos, donde la memoria compartida sería impráctica.

## Desventajas del paso de mensajes:

- Mayor latencia en la comunicación entre nodos, en comparación con la memoria compartida.
- Programación más compleja, ya que los desarrolladores deben gestionar explícitamente la comunicación.
- Sobrecarga de comunicación, ya que los mensajes deben enviarse y recibirse entre nodos.
- En resumen, el paso de mensajes permite la comunicación entre nodos en un sistema de memoria distribuida, ofreciendo mejor escalabilidad, pero con mayor latencia y complejidad de programación en comparación con la memoria compartida.

## 5 . Compare los modelos de consistencia eventual y consistencia fuerte en sistemas de memoria distribuida. Proporcione ejemplos de aplicaciones donde cada modelo sería más adecuado.

Respuesta Esperada:

Debes describir:

- Consistencia fuerte: Las actualizaciones son visibles instantáneamente a todos los nodos, proporcionando una vista consistente de los datos en todo momento.
- Consistencia eventual: Las actualizaciones se propagan gradualmente y todos los nodos eventualmente alcanzan una consistencia, pero puede haber inconsistencias temporales.
- Ejemplos: Consistencia fuerte es crucial para aplicaciones financieras, mientras que la consistencia eventual es adecuada para redes sociales y sistemas de caching distribuido.
## MI RESPUESTA:
## Consistencia fuerte y consistencia eventual en sistemas de memoria distribuida:

## Consistencia fuerte:

Las actualizaciones son visibles instantáneamente a todos los nodos.
Proporciona una vista consistente de los datos en todo momento.
Garantiza que todas las operaciones se ven en el mismo orden por todos los nodos.
Requiere más sincronización y comunicación entre nodos, lo que impacta el rendimiento.

## Consistencia eventual:

Las actualizaciones se propagan gradualmente entre los nodos.
Los nodos eventualmente alcanzan un estado consistente, pero puede haber inconsistencias temporales.
Menos sincronización y comunicación entre nodos, lo que mejora el rendimiento.
Permite mayor disponibilidad y tolerancia a particiones.

## Ejemplos de aplicaciones:

- Consistencia fuerte:
    Aplicaciones financieras: Transacciones bancarias, donde la consistencia de los datos es crítica.
    Sistemas de reservas: Evitar overbooking en sistemas de reserva de vuelos o hoteles.
- Consistencia eventual:
    Redes sociales: Actualización de estados y publicaciones, donde la consistencia eventual es aceptable.
    Sistemas de caché distribuida: Mantener copias de datos en múltiples nodos, donde la consistencia eventual es suficiente.

En resumen, la consistencia fuerte garantiza la consistencia en todo momento, pero tiene un mayor impacto en el rendimiento. La consistencia eventual es más relajada, lo que permite mejorar el rendimiento, pero puede tener inconsistencias temporales. La elección del modelo de consistencia depende de los requisitos de la aplicación y del equilibrio entre consistencia y rendimiento.

## 6 . Implementa un programa en Python que utilice el módulo multiprocessing para demostrar la memoria compartida. Crea varios procesos que incrementen una variable compartida de manera segura utilizando un Value y un Lock.

import multiprocessing

def increment(shared_value, lock):
    for _ in range(10000):
        with lock:
            shared_value.value += 1

def main():
    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    processes = []

    for _ in range(4):
        p = multiprocessing.Process(target=increment, args=(shared_value, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value: {shared_value.value}")

if __name__ == "__main__":
    main()
## MI RESPUESTA:

import multiprocessing

NUM_PROCESSES = 4
NUM_INCREMENTS = 10000

def increment(shared_value, lock):
    for _ in range(NUM_INCREMENTS):
        with lock:
            shared_value.value += 1

def main():
    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    processes = []

    for _ in range(NUM_PROCESSES):
        p = multiprocessing.Process(target=increment, args=(shared_value, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value of shared_value: {shared_value.value}")

if __name__ == "__main__":
    main()
- Explicación:

- Importamos el módulo multiprocessing que nos permite crear y gestionar procesos en Python.
- Definimos las constantes NUM_PROCESSES y NUM_INCREMENTS que establecen el número de procesos y el número de incrementos que cada proceso realizará.
- Definimos la función increment() que incrementa la variable compartida shared_value dentro de un bloque with lock: para garantizar la exclusión mutua.
- En el main(), creamos un objeto Value compartido shared_value y un Lock lock que se utilizarán para proteger el acceso a la variable compartida.
- Creamos una lista de procesos processes y lanzamos cada uno de ellos utilizando multiprocessing.Process(target=increment, args=(shared_value, lock)).
- Esperamos a que todos los procesos terminen utilizando p.join() para cada proceso.
- Finalmente, imprimimos el valor final de shared_value.

Al ejecutar este programa, verás que el valor final de shared_value será igual a NUM_PROCESSES * NUM_INCREMENTS, lo que demuestra que los procesos han incrementado la variable compartida de manera segura utilizando el mecanismo de bloqueo.

Algunas cosas a tener en cuenta:

- Utilizamos multiprocessing.Value para crear una variable compartida entre procesos, en lugar de una variable global.
- Utilizamos multiprocessing.Lock para crear un bloqueo que se usa para proteger el acceso a la variable compartida.
- Dentro de la función increment(), usamos un bloque with lock: para adquirir el bloqueo antes de incrementar la variable compartida.

Este enfoque garantiza que solo un proceso pueda acceder a la variable compartida a la vez, evitando así condiciones de carrera y manteniendo la integridad de los datos.

## 7 . Explica la diferencia entre coherencia de caché y consistencia de caché. Proporciona ejemplos de cómo estos conceptos afectan el rendimiento de un sistema multiprocesador.

Respuesta esperada:

Debes explicar:

- Coherencia de Caché: Garantiza que todas las copias de un dato en diferentes cachés sean iguales.
- Consistencia de Caché: Garantiza el orden en que las operaciones de memoria son vistas por diferentes procesadores.
- Ejemplos: Condiciones de carrera debido a la falta de coherencia, problemas de sincronización debido a la falta de consistencia.
## MI RESPUESTA:
La coherencia de caché y la consistencia de caché son conceptos relacionados pero distintos en un sistema multiprocesador:

- Coherencia de Caché:

    . La coherencia de caché garantiza que todas las copias de un mismo dato en las diferentes cachés de los procesadores sean iguales.
    . Esto significa que cuando un procesador modifica un dato, esa modificación se propaga a todas las demás copias del dato en las cachés de otros procesadores.
    . La falta de coherencia de caché puede causar condiciones de carrera, donde los procesadores ven diferentes valores para el mismo dato.
- Consistencia de Caché:

    . La consistencia de caché garantiza el orden en que las operaciones de memoria son vistas por los diferentes procesadores.
    . Esto significa que si un procesador realiza una secuencia de operaciones de memoria, los demás procesadores verán esas operaciones en el mismo orden.
    . La falta de consistencia de caché puede causar problemas de sincronización, donde los procesadores no ven las operaciones en el orden esperado.

Ejemplos:

- Condiciones de carrera:

    En un sistema multiprocesador sin coherencia de caché, si dos procesadores intentan incrementar la misma variable compartida al mismo tiempo, pueden ver diferentes valores finales debido a la falta de sincronización.
    Esto puede llevar a resultados incorrectos y errores en la aplicación.

- Problemas de sincronización:

    En un sistema multiprocesador sin consistencia de caché, si un procesador realiza una secuencia de operaciones de memoria para adquirir un bloqueo y luego liberar el bloqueo, otros procesadores podrían ver esas operaciones en un orden diferente.
    Esto puede causar que los procesadores adquieran el bloqueo en un orden incorrecto, lo que puede provocar bloqueos y errores de sincronización.

En resumen, la coherencia de caché garantiza que todos los procesadores vean los mismos datos, mientras que la consistencia de caché garantiza que los procesadores vean las operaciones de memoria en el mismo orden. Ambos conceptos son cruciales para el correcto funcionamiento de un sistema multiprocesador, ya que afectan directamente al rendimiento y la integridad de los datos.

## 8 . Implementa un programa en Python que simule la coherencia de caché utilizando threading. Crea un sistema donde múltiples hilos modifiquen una variable compartida y utilice bloqueos para garantizar la coherencia.

import threading

shared_value = 0
lock = threading.Lock()

def modify_shared_value():
    global shared_value
    for _ in range(10000):
        with lock:
            temp = shared_value
            temp += 1
            shared_value = temp

def main():
    threads = []

    for _ in range(4):
        t = threading.Thread(target=modify_shared_value)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final value: {shared_value}")

if __name__ == "__main__":
    main()

## MI RESPUESTA
import threading

NUM_THREADS = 4
NUM_ITERATIONS = 10000

shared_value = 0
lock = threading.Lock()

def modify_shared_value():
    global shared_value
    for _ in range(NUM_ITERATIONS):
        with lock:
            temp = shared_value
            temp += 1
            shared_value = temp

def main():
    threads = []

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=modify_shared_value)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final value: {shared_value}")

if __name__ == "__main__":
    main()

Explicación:

    - Importamos el módulo threading que nos permite crear y gestionar hilos en Python.
    - Definimos las constantes NUM_THREADS y NUM_ITERATIONS que establecen el número de hilos y el número de iteraciones que cada hilo realizará.
    - Declaramos la variable compartida shared_value y un lock que se utilizará para proteger el acceso a la variable compartida.
    - Definimos la función modify_shared_value() que incrementa la variable compartida shared_value dentro de un bloque with lock: para garantizar la exclusión mutua.
    - En el main(), creamos una lista de hilos threads y lanzamos cada uno de ellos utilizando threading.Thread(target=modify_shared_value).
    - Esperamos a que todos los hilos terminen utilizando t.join() para cada hilo.
    - Finalmente, imprimimos el valor final de shared_value.
## 9 .Describe cómo funciona un sistema de snoop bus para mantener la coherencia de caché en un sistema multiprocesador. ¿Cuáles son los desafíos asociados con el snoop bus?

Respuesta Esperada:

Debes explicar:

- Funcionamiento del snoop bus: Todas las cachés observan (snooping) el bus de datos para detectar operaciones relevantes y mantener la coherencia.
- Desafíos: Escalabilidad limitada debido al tráfico en el bus, latencia, complejidad de implementación.
## MI RESPUESTA
El sistema de snoop bus es una técnica utilizada en sistemas multiprocesador para mantener la coherencia de caché. Funciona de la siguiente manera:

- Funcionamiento del Snoop Bus:

.Todas las cachés de los procesadores están conectadas a un bus compartido, llamado "snoop bus".
.Cuando un procesador realiza una operación de lectura o escritura en su propia caché, esa operación se transmite a través del snoop bus.
.Todas las demás cachés "observan" (snoop) el bus, detectando las operaciones realizadas por otros procesadores.
.Cada caché mantiene información sobre el estado de sus propias líneas de caché (por ejemplo, si están modificadas, compartidas, etc.) usando protocolos como MESI.
.Cuando una caché detecta una operación relevante en el bus (como una escritura a una línea de caché que posee), actualiza su propia información de coherencia para mantener la consistencia de los datos.

- Desafíos del Snoop Bus:

.Escalabilidad limitada: A medida que se agregan más procesadores, el tráfico en el snoop bus aumenta, lo que puede limitar la escalabilidad del sistema.
.Latencia: El hecho de que todas las operaciones de memoria deban pasar por el snoop bus introduce latencia adicional, lo que puede afectar el rendimiento.
.Complejidad de implementación: Gestionar la coherencia de caché utilizando un snoop bus es técnicamente complejo, especialmente cuando se trabaja con protocolos de coherencia más avanzados.
.Consumo de energía: El tráfico constante en el snoop bus consume una cantidad significativa de energía, lo que puede ser un problema en sistemas con restricciones de alimentación.

Para mitigar estos desafíos, se han desarrollado otras técnicas de coherencia de caché, como los directorios de coherencia, que pueden escalar mejor y reducir la complejidad del diseño. Sin embargo, el snoop bus sigue siendo una solución ampliamente utilizada, especialmente en sistemas multiprocesador más pequeños y de bajo costo.

En resumen, el snoop bus es un enfoque efectivo para mantener la coherencia de caché en sistemas multiprocesador, pero enfrenta desafíos de escalabilidad, latencia y complejidad de implementación a medida que los sistemas se vuelven más grandes y complejos.
