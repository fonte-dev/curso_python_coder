# --- DESAFÍO 1: STRINGS ---
cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

# Solución:
# Concatenamos agregando espacios vacíos " " para que no quede todo pegado
mensaje_final = cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1
print(mensaje_final)
# Resultado esperado: Python es un lenguaje de programación versátil


# --- DESAFÍO 2: NÚMEROS (FÚTBOL) ---
print("\n--- CALCULADORA DE TORNEO ---")

# Datos fijos (Hardcodeado según la consigna)
partidos_totales = 20

# Inputs de usuario
# Lo pasamos a int porque no podés ganar 1.5 partidos (tienen que ser enteros)
ganados = int(input("Partidos Ganados (3 pts): "))
empatados = int(input("Partidos Empatados (1 pt): "))
perdidos = int(input("Partidos Perdidos (0 pts): "))

# Lógica de Puntos
puntos_totales = (ganados * 3) + (empatados * 1) + (perdidos * 0)

# Lógica de Promedio
promedio = puntos_totales / partidos_totales

print(f"Puntos Totales: {puntos_totales}")
print(f"Promedio por partido: {promedio}")


# --- DESAFÍO 3: SLICING (BOSS FIGHT) ---
print("\n--- DESAFÍO SLICING ---")
cadena_invertida = "acitametaM ,5.8 ,otipeP ordeP"

# PASO 1: Damos vuelta la cadena (Reverse Engineering)
# [:: -1] lee de atrás para adelante
cadena_volteada = cadena_invertida[::-1]
print("Cadena normalizada:", cadena_volteada)
# Resultado: "Pedro Pepito, 8.5, Matematica"

# PASO 2: Extraemos los datos con Slicing
# Contamos los espacios a mano para sacar los índices correctos
nombre_alumno = cadena_volteada[0:12]  # "Pedro Pepito"
nota = cadena_volteada[14:17]  # "8.5"
materia = cadena_volteada[19:]  # "Matematica" (Hasta el final)

# PASO 3: Imprimimos el reporte final
# Usamos concatenación (+) como pide la consigna
# "se sacó un" suena más natural que "ha sacado un"
print(nombre_alumno + " se sacó un " + nota + " en " + materia)
