# Metodos de cadenas

cadena = "Hola mundo"
print(len(cadena))

print(cadena.upper())
print(cadena.lower())

cadena = "hola mundo"
print(cadena.capitalize())
print(cadena.title())

cadena = "123 hola mundo 123"
cuenta = cadena.count(" ")
print(cuenta)

indice = cadena.find("123")
print(indice)

indice = cadena.rfind("123")
print(indice)

cadena = "   hola mundo   ".strip().capitalize().upper().count("M")
# cadena = cadena.strip()
# cadena = cadena.capitalize()
print(cadena)

cadena = "hola mundo"
lista = cadena.split()
print(lista)

lista = ["hola", "mundo"]
cadena = " ".join(lista)
print(cadena)

cadena = "hola mundo mundo"
cadena = cadena.replace("mundo", "Python")
cadena = cadena.replace("a", "A")
print(cadena)
