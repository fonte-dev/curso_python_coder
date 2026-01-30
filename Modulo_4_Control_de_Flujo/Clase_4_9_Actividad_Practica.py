# --- ACTIVIDAD PRÁCTICA UNIDAD 4 (CONTROL DE FLUJO) ---
# Ejercicios integradores: Menús, Whiles, Rangos y Listas.

# ==========================================
# EJERCICIO 1: CALCULADORA CON MENÚ
# ==========================================
print("\n--- EJERCICIO 1: CALCULADORA ---")

# Pido los numeros afuera del bucle (según consigna)
n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))

while True:
    print("\n[1] Sumar")
    print("[2] Restar")
    print("[3] Multiplicar")
    print("[4] Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print(f"Resultado: {n1} + {n2} = {n1 + n2}")
    elif opcion == "2":
        print(f"Resultado: {n1} - {n2} = {n1 - n2}")
    elif opcion == "3":
        print(f"Resultado: {n1} * {n2} = {n1 * n2}")
    elif opcion == "4":
        print("Saliendo del programa...")
        break  # Rompe el while
    else:
        print("Opción incorrecta. Probá de nuevo.")


# ==========================================
# EJERCICIO 2: VALIDAR IMPAR
# ==========================================
print("\n--- EJERCICIO 2: VALIDAR IMPAR ---")

while True:
    try:
        numero = int(input("Ingresá un número IMPAR: "))
        if numero % 2 != 0:  # Si el resto no es 0, es impar
            print(f"Correcto! El {numero} es impar.")
            break  # Salgo del bucle
        else:
            print("Ese es par. Intentá de nuevo.")
    except ValueError:
        print("Eso no es un número entero.")


# ==========================================
# EJERCICIO 3: SUMA DE IMPARES (0-100)
# ==========================================
print("\n--- EJERCICIO 3: SUMA IMPARES 0-100 ---")

# Truco: range(inicio, fin, salto).
# Uso sum() directo sobre el range para no hacer un for.
suma_impares = sum(range(1, 101, 2))
print(f"La suma total es: {suma_impares}")


# ==========================================
# EJERCICIO 4: MEDIA ARITMÉTICA (PROMEDIO)
# ==========================================
print("\n--- EJERCICIO 4: PROMEDIO ---")

cantidad = int(input("¿Cuántos números vas a ingresar?: "))
acumulador = 0

for i in range(cantidad):
    num = float(input(f"Ingresá el número {i+1}: "))
    acumulador += num

# Evito dividir por cero por si puse cantidad 0
if cantidad > 0:
    promedio = acumulador / cantidad
    print(f"El promedio es: {promedio}")
else:
    print("No ingresaste números.")


# ==========================================
# EJERCICIO 5: ADIVINAR EN LISTA (0-9)
# ==========================================
print("\n--- EJERCICIO 5: BUSCAR EN LISTA ---")

# Defino una lista arbitraria como pide el ejercicio
lista_secreta = [1, 3, 5, 6, 9]
numero_usuario = -1  # Inicio con valor invalido para entrar al while

# 1. Validar que sea del 0 al 9
while numero_usuario < 0 or numero_usuario > 9:
    try:
        numero_usuario = int(input("Ingresá un número del 0 al 9: "))
        if numero_usuario < 0 or numero_usuario > 9:
            print("Fuera de rango. Tiene que ser 0-9.")
    except ValueError:
        print("Error: Ingresá un número entero.")

# 2. Comprobar si está en la lista
if numero_usuario in lista_secreta:
    print(f"¡Magia! El {numero_usuario} ESTÁ en la lista secreta {lista_secreta}.")
else:
    print(f"El {numero_usuario} no está en la lista. Mala suerte.")


# ==========================================
# EJERCICIO 6: LISTAS CON RANGE
# ==========================================
print("\n--- EJERCICIO 6: GENERANDO LISTAS ---")
# OJO: El limite superior del range (stop) NUNCA se incluye.

# 0 al 10 (Pongo 11 para que llegue a 10)
lista_1 = list(range(0, 11))
print(f"1. 0 al 10: {lista_1}")

# -10 al 0 (Pongo 1 para que llegue a 0)
lista_2 = list(range(-10, 1))
print(f"2. -10 al 0: {lista_2}")

# Pares 0 al 20 (Pongo 21, paso 2)
lista_3 = list(range(0, 21, 2))
print(f"3. Pares 0-20: {lista_3}")

# Impares -20 a 0
# Empiezo en -19 (primer impar) hasta 0, paso 2
lista_4 = list(range(-19, 0, 2))
print(f"4. Impares -20 a 0: {lista_4}")

# Multiplos de 5 (0 al 50)
lista_5 = list(range(0, 51, 5))
print(f"5. Multiplos de 5: {lista_5}")
