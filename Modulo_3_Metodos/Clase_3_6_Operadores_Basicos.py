# Operaciones en Python

# 1. Operaciones aritméticas
# + * / // % **


# 2. Operaciones de comparación
# == != > >= < <=

a = 10
b = 5
print("a es igual a b:", a == b)
print("a es diferente a b:", a != b)
print("a es mayor a b:", a > b)
print("a es menor a b:", a < b)
print("a es mayor o igual a b:", a >= b)
print("a es menor o igual a b:", a <= b)

# 3. Operadores Lógicos
# and or not
x = True
y = False
print("x and y:", x and y)
# print(True and True and True and False)

print("x and y:", x or y)
# print(True or False or False or False)

# 4. all() y any()

hay_energia = True
lampara_enchufada = True
lampara_encendida = True

luz_en_habitacion = all([hay_energia, lampara_enchufada, lampara_encendida])
print("Luz en habitación:", luz_en_habitacion)

hay_ganas = True
hay_habilidad = False
hay_pelota = True

hoy_jugamos = any([hay_ganas, hay_habilidad, hay_pelota])
print("Hoy jugamos:", hoy_jugamos)
