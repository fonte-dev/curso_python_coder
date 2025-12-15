# --- CLASE 2.6: ACTIVIDAD PRÁCTICA INTEGRADORA ---

# ==========================================
# EJERCICIO 1: IDENTIFICACIÓN DE TIPOS DE DATOS
# ==========================================
print("\n--- EJERCICIO 1: TIPOS DE DATOS ---")
# "Hola Mundo"        -> str (String)
# [1, 10, 100]        -> list (Lista)
# -25                 -> int (Entero)
# (8, 100, -12)       -> tuple (Tupla)
# 1.167               -> float (Decimal)
# ["Hola", "Mundo"]   -> list (Lista de strings)
# ' '                 -> str (String vacío/espacio)
# (1, -5, "Hola!")    -> tuple (Tupla heterogénea)
print("Tipos identificados en el código (ver comentarios).")


# ==========================================
# EJERCICIO 2: LÓGICA MENTAL (RESULTADOS)
# ==========================================
print("\n--- EJERCICIO 2: RESULTADOS ESPERADOS ---")
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e = (4, 5, 6)

print(a * 5)  # 50
print(a - b)  # 15 (Menos por menos es más: 10 - (-5))
print(c + "Mundo")  # "HolaMundo" (Concatenación)
print(c * 2)  # "HolaHola" (Repetición)
print(c[-1])  # "a" (Último caracter)
print(c[1:])  # "ola" (Slicing desde índice 1 al final)
print(d + d)  # [1, 2, 3, 1, 2, 3] (Suma de listas no suma números, une listas)
print(e[1])  # 5 (Elemento en índice 1)
print(e + (7, 8, 9))  # (4, 5, 6, 7, 8, 9) (Concatenación de tuplas)


# ==========================================
# EJERCICIO 3: EL BUG DEL PROMEDIO (DEBUGGING)
# ==========================================
print("\n--- EJERCICIO 3: CORRIGIENDO EL PROMEDIO ---")
numero_1 = 9
numero_2 = 3
numero_3 = 6

# EL ERROR: Python respeta la precedencia matemática. Primero divide, después suma.
# media_mala = numero_1 + numero_2 + numero_3 / 3  -> Esto hace 9 + 3 + (6/3) = 14

# LA SOLUCIÓN: Usar paréntesis para forzar la suma primero.

media_corregida = (numero_1 + numero_2 + numero_3) / 3
print(f"La nota media corregida es: {media_corregida}")


# ==========================================
# EJERCICIO 4: PROMEDIO PONDERADO (AUDIO MIXING LOGIC)
# ==========================================
print("\n--- EJERCICIO 4: NOTAS PONDERADAS ---")
# Es como mezclar audio: El Kick (nota 3) tiene más volumen (50%) que el HiHat (nota 1)
nota_1 = 10  # Vale 15%
nota_2 = 7  # Vale 35%
nota_3 = 4  # Vale 50%

# Calculamos el aporte de cada nota
nota_final = (nota_1 * 0.15) + (nota_2 * 0.35) + (nota_3 * 0.50)
print(f"La nota final ponderada es: {nota_final}")


# ==========================================
# EJERCICIO 5: MATRIZ Y SLICING
# ==========================================
print("\n--- EJERCICIO 5: COMPLETANDO LA MATRIZ ---")
# La consigna pide agregar un 4to elemento que sea la suma de los 3 anteriores.
# Como no vimos bucles (for) todavía, lo hacemos manual (Hardcodeado) o usando append.

matriz = [[1, 5, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]

# Modificamos fila por fila agregando la suma al final
# sum(lista) suma todo lo que hay adentro
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)
# Resultado: [[1, 5, 1, 7], [2, 1, 2, 5], [3, 0, 1, 4], [1, 4, 4, 9]]


# ==========================================
# EJERCICIO 6: SETS (PAISES)
# ==========================================
print("\n--- EJERCICIO 6: SETS DE PAISES ---")
paises = {"Inglaterra", "USA", "Mexico"}

# Agregamos nuevos (USA está repetido, Islandia, Italia, Argentina, Portugal)
paises.update({"Islandia", "Italia", "Argentina", "Portugal", "USA"})

print(f"Set actual: {paises}")
# PREGUNTA: ¿Qué pasó con el elemento USA?
# RESPUESTA: Nada. Los Sets eliminan duplicados automáticamente. Solo queda un "USA".

# Eliminar Chile e Italia
paises.discard("Italia")  # Usamos discard por seguridad
# paises.remove("Chile")
paises.discard("Chile")
# PREGUNTA: ¿Qué pasa si usamos remove con Chile?
# RESPUESTA: Da KeyError (Error de llave) porque Chile no está en la lista.
# Por eso usamos .discard("Chile"), que no tira error si falla.

print(f"Set final sin Italia ni Chile: {paises}")


# ==========================================
# EJERCICIO 7: DICCIONARIOS (INPUT DE USUARIO)
# ==========================================
print("\n--- EJERCICIO 7: DICCIONARIO DE USUARIO ---")
# Solicitamos datos (Descomenta los inputs para probarlo)
nombre = "Juan"  #
edad = 25  # input("Tu edad: ")
direccion = "Carrera 7 - Bogota"  # input("Tu direccion: ")

usuario = {"nombre": nombre, "edad": edad, "direccion": direccion}

print(
    f"{usuario['nombre']} tiene {usuario['edad']} años, y vive en {usuario['direccion']}"
)
