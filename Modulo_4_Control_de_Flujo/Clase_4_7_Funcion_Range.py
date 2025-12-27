# --- CLASE 4.7: FUNCIÓN RANGE ---
# Sintaxis: range(start, STOP, step)
# REGLA DE ORO: El 'STOP' nunca se incluye (es exclusivo).

# 1. BÁSICO (0 hasta N-1)
# Si pongo range(5), me da 5 números: 0, 1, 2, 3, 4
print("--- Rango Simple ---")
for i in range(3):
    print(f"Iteración {i}")

# 2. START / STOP (Desde X hasta Y-1)
print("\n--- Rango Acotado ---")
for n in range(10, 13):  # 10, 11, 12 (El 13 no entra)
    print(f"Numero: {n}")

# 3. STEP (Saltando números)
# Util para recorrer índices pares o escalas
print("\n--- Saltos (Pares) ---")
for par in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(f"Par: {par}")

# 4. REVERSA (Cuenta Regresiva)
# El step tiene que ser negativo. El STOP sigue siendo exclusivo (si pongo 0, frena en 1).
print("\n--- Cuenta Regresiva (Despegue) ---")
import time

for i in range(5, 0, -1):
    print(f"T-minus: {i}")
    time.sleep(0.5)  # Control de tiempo de prints

print("¡DESPEGUE!")

# 5. APLICACIÓN PRÁCTICA (Música)
# Generar tracklist simulada
print("\n--- GENERADOR DE TRACKLIST ---")
total_tracks = 8

# range(1, total + 1) es el truco para que llegue hasta el numero final exacto
for track_num in range(1, total_tracks + 1):
    print(
        f"Track {track_num:02}: (Sin Título)"
    )  # :02 le pone el cero adelante (01, 02...)
