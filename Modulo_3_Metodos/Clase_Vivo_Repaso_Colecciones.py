# --- CLASE EN VIVO: REPASO DE COLECCIONES Y OPERADORES ---
# Autor: Juan Pablo Fonte
# Temas: Strings, Sets, Diccionarios y Lógica Booleana.

import time


def separador(titulo):
    print("\n" + "=" * 40)
    print(f"--- {titulo} ---")
    print("=" * 40)


# ==========================================
# ACTIVIDAD 1: COLECCIONES 1 (Manipulación de Strings)
# ==========================================
separador("ACTIVIDAD 1: FIX TEXTO BÉISBOL")

texto_sucio = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"

# 1. Separar por el caracter '&'
lineas = texto_sucio.split("&")

# 2. Procesar cada línea respetando Nombres Propios (Slicing)
# No usamos .capitalize() porque rompería "Joe Castiglione" a "joe castiglione"
lineas[0] = lineas[0][0].upper() + lineas[0][1:] + "..."  # Gordon...
lineas[1] = "- " + lineas[1][0].upper() + lineas[1][1:] + "."  # Strawberry...
lineas[2] = (
    "- " + lineas[2][0].upper() + lineas[2][1:].replace("-le", "le") + "."
)  # Dos pies...
lineas[3] = "- " + lineas[3][0].upper() + lineas[3][1:] + "."  # Strawberry...

# 3. Mostrar resultado
for linea in lineas:
    print(linea)


# ==========================================
# ACTIVIDAD 2: COLECCIONES 2 (Sets / Conjuntos)
# ==========================================
separador("ACTIVIDAD 2: SETS (CONJUNTOS)")
# Los sets NO tienen orden y NO aceptan duplicados.

my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])

print(f"Set 1: {my_set_1}")
print(f"Set 2: {my_set_2}")

# 1. UNION (Juntar todo sin repetir)
union = my_set_1.union(my_set_2)
print(f"Unión (Todos): {union}")

# 2. INTERSECCIÓN (Lo que tienen en común)
interseccion = my_set_1.intersection(my_set_2)
print(f"Intersección (Comunes): {interseccion}")

# 3. DIFERENCIA (Lo que tiene el 1 que NO tiene el 2)
diferencia = my_set_1.difference(my_set_2)
print(f"Diferencia (Solo en Set 1): {diferencia}")


# ==========================================
# ACTIVIDAD 3: COLECCIONES 3 (Diccionarios)
# ==========================================
separador("ACTIVIDAD 3: DIVISAS (DICCIONARIOS)")

divisas = {"Dolar": "$", "Euro": "€", "Libra": "£"}

# .title() ayuda a que si escriben "dolar" lo convierta a "Dolar"
divisa_input = input("Ingrese la divisa (Dolar/Euro/Libra): ").strip().title()

if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    print(f"La divisa '{divisa_input}' no está disponible.")


# ==========================================
# ACTIVIDAD 4: OPERADORES RELACIONALES
# ==========================================
separador("ACTIVIDAD 4: RELACIONALES")

# Python calcula esto automáticamente y devuelve True o False
expresiones_rel = [
    False == True,  # False
    10 >= 2 * 4,  # 10 >= 8 -> True
    33 / 3 == 11,  # 11.0 == 11 -> True
    True > False,  # 1 > 0 -> True
    True * 5 == 2.5 * 2,  # 5.0 == 5.0 -> True
]
print(f"Resultados Relacionales: {expresiones_rel}")


# ==========================================
# ACTIVIDAD 5: OPERADORES LÓGICOS
# ==========================================
separador("ACTIVIDAD 5: LÓGICOS (AND/OR/NOT)")

expresiones_log = [
    not False,  # True
    not 3 == 5,  # not False -> True
    33 / 3 == 11 and 5 > 2,  # True and True -> True
    True or False,  # True
    True * 5 == 2.5 * 2 or 123 >= 23,  # True or True -> True
    12 > 7 and True < False,  # True and False -> False
]
print(f"Resultados Lógicos: {expresiones_log}")


# ==========================================
# ACTIVIDAD 6: EXPRESIONES ANIDADAS (FINAL BOSS)
# ==========================================
separador("ACTIVIDAD 6: VALIDACIÓN COMPLEJA")

print("--- Ingrese datos para validar ---")
nombre = input("Nombre: ")
edad = int(input("Edad: "))

# Todas las condiciones deben cumplirse (AND)
cumple_requisitos = (
    (nombre != "****")  # No puede ser asteriscos
    and (5 < edad < 20)  # Edad entre 6 y 19
    and (4 <= len(nombre) < 8)  # Nombre entre 4 y 7 letras
    and (edad * 3 > 35)  # Edad > 11.66
)

print(f"\n¿Cumple todas las condiciones?: {cumple_requisitos}")

# Explicación del resultado
if cumple_requisitos:
    print("Pasa la validación.")
else:
    print("No pasa la validación.")
