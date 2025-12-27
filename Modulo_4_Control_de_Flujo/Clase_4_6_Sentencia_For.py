# --- CLASE 4.6: BUCLE FOR ---
# Referencia: Herramienta principal para recorrer colecciones (Listas, Tuplas, Strings).

# 1. ITERACIÓN SIMPLE (Lectura)
# Patrón: "Por cada elemento en la colección, hacé esto..."

pacientes = ["Juan", "Maria", "Pedro", "Luisa"]
print("--- LISTA DE PACIENTES ---")
for p in pacientes:
    print(f"-> Procesando legajo de: {p}")


# 2. ITERACIÓN CON MODIFICACIÓN (La forma 'C++')
# Si necesito MODIFICAR la lista original, necesito el índice [i].
# Uso: range(len(lista)) genera 0, 1, 2, 3...

mediciones_presion = [110, 120, 135, 105]
print(f"\nOriginal: {mediciones_presion}")

for i in range(len(mediciones_presion)):
    # Simulo calibración del equipo (+5 puntos a todo)
    mediciones_presion[i] += 5

print(f"Calibrado: {mediciones_presion}")


# 3. ENUMERATE (La forma 'Pythonic')
# Me da el índice Y el valor al mismo tiempo. Es más limpio.

sintomas = ["fiebre", "dolor", "tos"]
print("\n--- REPORTE CLÍNICO (ENUMERATE) ---")

for indice, sintoma in enumerate(sintomas):
    # indice arranca en 0, le sumo 1 para que quede lindo en el print
    print(f"Sintoma #{indice + 1}: {sintoma.upper()}")


# 4. APLICACIÓN PROJECT MAT: NORMALIZACIÓN DE DATOS
# Caso real: Los usuarios cargan nombres mal (minúsculas, espacios).
# Script para limpiar la base de datos.

base_datos_pacientes = ["  juan perez", "maria GOMEZ", "pedro alvarez  "]
print(f"\nBase sucia: {base_datos_pacientes}")

for i, nombre in enumerate(base_datos_pacientes):
    # .strip() saca espacios, .title() pone Mayuscula Inicial
    base_datos_pacientes[i] = nombre.strip().title()

print(f"Base limpia: {base_datos_pacientes}")
