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


