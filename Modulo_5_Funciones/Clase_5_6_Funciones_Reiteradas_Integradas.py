# --- CLASE 5.6: RECURSIVIDAD Y FUNCIONES INTEGRADAS ---
# Conceptos:
# 1. Recursividad: Una función que se llama a sí misma (Cuidado con el bucle infinito).
# 2. Built-ins: Herramientas que ya vienen en Python (len, sum, filter, int).

# ==========================================
# PARTE 1: RECURSIVIDAD (Lo que faltaba en el video)
# ==========================================


# Ejemplo Clásico: Factorial (Matemática)
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n == 0:  # CASO BASE (Freno de mano)
        return 1
    else:
        # LLAMADA RECURSIVA
        return n * factorial(n - 1)


# Ejemplo Útil: Simular Reintentos de Conexión
def intentar_conectar_db(intentos_restantes):
    if intentos_restantes <= 0:
        print("Error fatal: No se pudo conectar tras varios intentos.")
        return False

    print(f"Intentando conectar... (Quedan {intentos_restantes} intentos)")
    # Simulo fallo y pruebo de nuevo llamandome a mi mismo
    # En la vida real, acá habría un try/except
    return intentar_conectar_db(intentos_restantes - 1)


# ==========================================
# PARTE 2: FUNCIONES INTEGRADAS (BUILT-INS)
# ==========================================

print("\n--- TEST DE RECURSIVIDAD ---")
print(f"Factorial de 5: {factorial(5)}")
intentar_conectar_db(3)

print("\n--- TEST DE BUILT-INS ---")

# A. Conversión de Tipos (Casting)
# Fundamental para limpiar inputs de usuarios
edad_input = "45"
peso_input = "70.5"

edad = int(edad_input)  # String -> Int
peso = float(peso_input)  # String -> Float
print(f"Paciente de {edad} años, peso: {peso}kg")

# B. Análisis de Listas (len, sum, max, min)
costos_tratamiento = [1500, 2000, 500, 3000]

print(f"Cant. Tratamientos: {len(costos_tratamiento)}")
print(f"Costo Total: ${sum(costos_tratamiento)}")
print(f"Tratamiento más caro: ${max(costos_tratamiento)}")


# ==========================================
# PARTE 3: FILTER (PROGRAMACIÓN FUNCIONAL)
# ==========================================
# Filter sirve para sacar elementos de una lista según una condición.
# Sintaxis: filter(funcion_que_devuelve_true_o_false, lista)

print("\n--- USO DE FILTER (PROJECT MERITUM) ---")

pacientes_mix = ["juan", "maria", "pedro", "ana", "luis"]


# Quiero solo los nombres cortos (menos de 5 letras)
def es_nombre_corto(nombre):
    return len(nombre) < 5


# Aplicando el filtro
# Nota: filter devuelve un objeto iterador, por eso uso list() para verlo.
nombres_cortos = list(filter(es_nombre_corto, pacientes_mix))

print(f"Lista original: {pacientes_mix}")
print(f"Filtrados (cortos): {nombres_cortos}")

# --- FILTER CON LAMBDA ---
# Una 'lambda' es una función anónima en una sola línea.
# Lo mismo de arriba pero en una línea:
nombres_largos = list(filter(lambda x: len(x) >= 5, pacientes_mix))
print(f"Filtrados (largos con lambda): {nombres_largos}")
