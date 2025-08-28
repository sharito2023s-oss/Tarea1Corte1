# 🤖 Tarea 1 – Simulador de Robot con Estrategias

Este repositorio contiene el desarrollo de un simulador de un robot que se desplaza en una cuadrícula **3x3**, con **batería limitada** y un sistema de **recompensas/castigos**.  
El objetivo es llegar a la posición `(2,2)` optimizando el recorrido y la gestión de batería.  

---

## ✅ Ítems desarrollados

### 1. Modificación de la función `mover_robot`  
- Cada movimiento consume **1 unidad de batería**.  
- El robot solo puede moverse si la batería > 0.  
- La acción `recargar` restaura la batería a 5.  

### 2. Restricción por batería  
- Si la batería llega a **0**, el robot **no se mueve** hasta recargar.  

### 3. Sistema de recompensas y castigos (`recompensa`)  
- `+5` → por recargar.  
- `-1` → por moverse normalmente.  
- `-5` → por intentar moverse sin batería.  
- `+20` → bonus por llegar al objetivo en ≤ 5 pasos.  
- `+15` → si llega al objetivo con batería ≥ 3.  
- `+10` → si llega con batería baja.  
- `-3` → si supera 8 pasos sin alcanzar el objetivo.  

### 4. Estrategias implementadas
Se probaron diferentes estrategias:  
- **Aleatoria** → elige movimientos o recargar al azar.  
- **Codiciosa hacia el objetivo** → prioriza llegar a `(2,2)` recargando solo si es necesario.  
- **Conservadora** → recarga cuando la batería ≤ 2, de lo contrario avanza hacia adelante/derecha.  

---

## 🗺️ Representación de la cuadrícula (3x3)

```text
+---+---+---+
| R |   |   |   ← (0,0) posición inicial
+---+---+---+
|   |   |   |
+---+---+---+
|   |   | G |   ← (2,2) objetivo
+---+---+---+
