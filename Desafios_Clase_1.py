# --- DESAFÍO 1: STRINGS ---
cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

# Solución:
# Usamos espacios vacíos " " para que no quede todo pegado
mensaje_final = cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1
print(mensaje_final)
# Resultado esperado: Python es un lenguaje de programación versátil

# --- DESAFÍO 2: NÚMEROS (FÚTBOL) ---
# Datos fijos (Hardcoded por consigna)
partidos_totales = 20

# Inputs de usuario (Convertimos a int porque no puedes ganar 1.5 partidos)
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
cadena_invertida = "acitametaM ,5.8 ,otipeP ordeP"

# PASO 1: Dar vuelta la cadena (Reverse Engineering)
# [Inicio : Fin : Paso] -> El paso -1 lee de atrás para adelante
cadena_volteada = cadena_invertida[::-1]
print("Cadena normalizada:", cadena_volteada)
# Resultado: "Pedro Pepito, 8.5, Matematica"

# PASO 2: Extraer datos con Slicing (Hardcodeado según la consigna)
# Contamos los espacios manualmente para encontrar los índices
nombre_alumno = cadena_volteada[0:12]  # "Pedro Pepito"
nota = cadena_volteada[14:17]  # "8.5"
materia = cadena_volteada[19:]  # "Matematica" (Hasta el final)

# PASO 3: Imprimir con formato
# Usamos concatenación (+) como pide la consigna, aunque f-string es mejor
print(nombre_alumno + " ha sacado un " + nota + " en " + materia)
