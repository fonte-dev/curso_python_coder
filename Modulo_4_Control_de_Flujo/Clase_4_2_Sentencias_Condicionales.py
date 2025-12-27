# VIDEO 1: Ejemplo de Sentencia If

numero = 7

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
elif numero == 7:
    print("El número es 7")
else:
    print("El número es cero")

print("Fin del programa")

print("*** MENU *** ")
print("verduras")
print("pastas")
print("carnes")
pedido = input("Selecciona una comida del menú: ")

if pedido == "verduras":
    print("✅Pedido recibido")
elif pedido == "pastas":
    print("✅Pedido recibido")
elif pedido == "carnes":
    print("✅Pedido recibido")
else:
    print("❌ Pedido no disponible")

# VIDEO 2: Ejemplos prácticos con condicionales


# Uso de operadores de comparación
temperatura = 10

if temperatura >= 30:
    print("Hace calor")
elif temperatura < 15:
    print("Hace frío")
else:
    print("Esta templado")

# Uso de operadores lógicos
numero = 500

if numero >= 10 and numero <= 20:
    print("El número está entre 10 y 20")
elif numero >= 20 and numero <= 30:
    print("El número está entre 20 y 30")
else:
    print("El número está fuera de los límites")

# Verificación de usuario y contraseña

usuario_sistema = "admin"
contraseña_sistema = "admin123"

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == usuario_sistema and contraseña == contraseña_sistema:
    print("Bienvenido, acceso concedido")
else:
    print("Usuario o contraseña incorrectos")

# Determinar el mayor de tres números

a = 5
b = 10
c = 300

if a > b and a > c:
    print("El número mayor es", a)
elif b > a and b > c:
    print("El número mayor es", b)
else:
    print("El número mayor es", c)

# Evaluación de calificaciones

calificacion = int(input("Ingresa tu nota: "))

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")
