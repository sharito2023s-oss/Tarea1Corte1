import random


def recompensa(accion, estado, pasos):
    if accion == "recargar":
        return 5
    elif estado["objetivo_alcanzado"]:
        if pasos <= 5:
            return 20
        if estado["bateria"] >= 3:
            return 15
        return 10
    elif accion in ["adelante", "atras", "izquierda", "derecha"]:
        if estado["bateria"] == 0:
            return -5
        return -1
    if pasos > 8 and not estado["objetivo_alcanzado"]:
        return -3
    return 0

def mover_robot(estado, accion):
    x, y = estado["posicion"]

    if accion == "recargar":
        estado["bateria"] = 5
    elif estado["bateria"] > 0:
        if accion == "adelante":
            x = min(x + 1, 2)
        elif accion == "atras":
            x = max(x - 1, 0)
        elif accion == "derecha":
            y = min(y + 1, 2)
        elif accion == "izquierda":
            y = max(y - 1, 0)
        estado["posicion"] = (x, y)
        estado["bateria"] -= 1

    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    estado["pasos"] += 1
    return estado


# ========================
# ESTRATEGIAS
# ========================
def estrategia_aleatoria(estado):
    return random.choice(["adelante", "atras", "izquierda", "derecha", "recargar"])

def estrategia_meta(estado):
    x, y = estado["posicion"]
    if estado["bateria"] == 0:
        return "recargar"
    if x < 2: return "adelante"
    if y < 2: return "derecha"
    return "recargar"

def estrategia_recargar(estado):
    if estado["bateria"] <= 2:
        return "recargar"
    return random.choice(["adelante", "derecha"])

# ========================
# SIMULADOR GENERAL
# ========================
def simular(estrategia, nombre, pasos=20):
    estado = {"posicion": (0,0), "bateria": 5, "objetivo_alcanzado": False, "pasos": 0}
    recompensa_total = 0
    print(f"\n=== Simulación con {nombre} ===")
    for paso in range(pasos):
        accion = estrategia(estado)
        estado = mover_robot(estado, accion)
        r = recompensa(accion, estado, estado["pasos"])
        recompensa_total += r
        print(f"Paso {paso+1}: Acción={accion}, Estado={estado}, Recompensa={r}")
    print(f"Recompensa total con {nombre}: {recompensa_total}\n")
    return recompensa_total


simular(estrategia_aleatoria, "Aleatoria")
simular(estrategia_meta, "Codiciosa hacia el objetivo")
simular(estrategia_recargar, "Conservadora")
