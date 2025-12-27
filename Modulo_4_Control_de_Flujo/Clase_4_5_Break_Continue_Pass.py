# --- CLASE 4.5: CONTROL DE BUCLES (BREAK, CONTINUE, PASS) ---
# Referencia técnica: Sentencias para manipular el flujo natural de iteraciones.

# 1. BREAK (Interrupción Inmediata)
# Caso de uso: Búsqueda lineal. Detener el proceso al encontrar el objetivo para ahorrar recursos.

print("--- INICIANDO BÚSQUEDA ---")
target = 7

for i in range(1, 11):
    print(f"Evaluando índice: {i}")
    if i == target:
        print(">> Objetivo encontrado. Interrumpiendo bucle.")
        break  # Optimización: Evita iteraciones innecesarias una vez cumplida la condición.

# 2. CONTINUE (Salto de Iteración)
# Caso de uso: Filtrado. Omitir lógica para ciertos elementos sin detener el bucle completo.

print("\n--- FILTRADO DE DATOS (Solo Impares) ---")
for n in range(1, 6):
    if n % 2 == 0:
        continue  # Omite el resto del bloque actual y pasa a la siguiente iteración.

    print(f"Procesando impar: {n}")


# 3. PASS (Placeholder Sintáctico)
# Caso de uso: Estructurar esqueleto del código (scaffolding) sin implementar lógica aún.
# Evita errores de sintaxis en bloques vacíos (if, def, class).

print("\n--- EJEMPLO DE ESTRUCTURA PENDIENTE (TODO) ---")

paciente_riesgo = True

if paciente_riesgo:
    # TODO: Implementar módulo de notificación a familiares.
    pass  # Marcador de posición. Permite ejecutar el script sin errores.
else:
    print("Paciente sin riesgo.")

# 4. OPERADOR TERNARIO
# Condicional en línea para asignación o impresión directa.
# Sintaxis: valor_si_true if condición else valor_si_false

encontrado = True
estado = "EXITO" if encontrado else "FALLO"
print(f"Estado de la operación: {estado}")
