# Diccionarios

un_diccionario = {"a": 1, "b": 2}
print(len(un_diccionario))
print(type(un_diccionario))

otro_diccionario = dict(c=3, d=4)
print(otro_diccionario)

print("🔥 Obtener")
elemento = un_diccionario["a"]
print(elemento)

print("🔥 Agregar")
un_diccionario["e"] = 5
print(un_diccionario)

print("🔥 Modificar")
un_diccionario["a"] = 1000
print(un_diccionario)

un_diccionario.update(otro_diccionario)
print(un_diccionario)

print("🔥 Borrar")
del un_diccionario["a"]
print(un_diccionario)

un_diccionario.pop("d")
print(un_diccionario)

un_diccionario.clear()
print(un_diccionario)
print(len(un_diccionario))
