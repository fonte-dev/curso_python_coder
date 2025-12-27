# Ejemplos de la sentencia while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
# Bucle con condición de salida

suma = 0
numero = 1

while suma < 10:
    suma += numero
    print(f"Suma: {suma}, número: {numero}")
    numero += 1

# Bucle con bandera

# bandera = True

# while bandera:
#     numero = int(input("Ingrese un número, si es negativo, sale: "))
#     if numero < 0:
#         bandera = False
# print("Fin del bucle")

while True:
    numero = int(input("Ingrese un número, si es negativo, sale: "))
    if numero < 0:
        break
print("Fin del bucle")

import random

numero_aleatorio = random.randint(1, 6)
adivinado = False

while not adivinado:
    intento = int(input("Ingrese un número del a 1 al 6: "))
    if intento == numero_aleatorio:
        adivinado = True
        print("Adivinaste el número!")
    elif intento < numero_aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")
