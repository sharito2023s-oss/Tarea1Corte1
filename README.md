✅ Ítems desarrollados
1. Modificación de la función mover_robot

Se implementó la lógica para que:

Cada movimiento consuma 1 unidad de batería.

El robot solo pueda moverse si tiene batería > 0.

La acción recargar restablece la batería a 5.

2. Restricción por batería

Si la batería llega a 0, el robot no puede moverse hasta recargar.

3. Sistema de recompensas y castigos (recompensa)

Castigo por intentar moverse sin batería: -5 puntos.

Costo por moverse normalmente: -1 punto.

Recompensa por recargar: +5 puntos.

Bonus por llegar al objetivo en ≤ 5 pasos: +20 puntos.

Recompensa por llegar con batería ≥ 3: +15 puntos.

Recompensa por llegar con batería baja: +10 puntos.

Castigo adicional si se exceden 8 pasos sin lograr el objetivo: -3 puntos.

4. Estrategias de movimiento implementadas

Se probaron distintas formas de decisión:

Aleatoria → elige cualquier acción al azar.

Codiciosa hacia el objetivo → prioriza avanzar hacia (2,2).

Conservadora → recarga cuando la batería ≤ 2, de lo contrario se mueve hacia adelante/derecha.

🚀 Ejecución

Para ejecutar el programa:

python main.py


Al correrlo, se obtendrán simulaciones con las tres estrategias, mostrando:

Acción tomada.

Estado del robot (posición, batería, pasos).

Recompensa obtenida.

Recompensa total al final.

📊 Ejemplo de salida en consola
=== Simulación con Codiciosa hacia el objetivo ===
Paso 1: Acción=adelante, Estado={'posicion': (1, 0), 'bateria': 4, 'objetivo_alcanzado': False, 'pasos': 1}, Recompensa=-1
Paso 2: Acción=adelante, Estado={'posicion': (2, 0), 'bateria': 3, 'objetivo_alcanzado': False, 'pasos': 2}, Recompensa=-1
Paso 3: Acción=derecha, Estado={'posicion': (2, 1), 'bateria': 2, 'objetivo_alcanzado': False, 'pasos': 3}, Recompensa=-1
Paso 4: Acción=derecha, Estado={'posicion': (2, 2), 'bateria': 1, 'objetivo_alcanzado': True, 'pasos': 4}, Recompensa=20
Recompensa total con Codiciosa hacia el objetivo: 17
