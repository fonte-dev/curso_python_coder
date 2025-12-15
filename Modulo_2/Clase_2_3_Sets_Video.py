# Conjuntos

mi_conjunto = {"hola", 1, 3, 4, 4, 4, "adios"}
print(mi_conjunto)

print("🔥 Obtener")
# mi_conjunto = [0] # Error
mi_lista = list(mi_conjunto)  # convierte en lista
print(mi_lista)
print(mi_lista[1:])
otro_conjunto = set(mi_lista[1:])
print(otro_conjunto)

print("🔥 Agregar")
mi_conjunto.add(1000)
print(mi_conjunto)

print("🔥 Modificar")
mi_lista = list(mi_conjunto)
indice = mi_lista.index(1000)
mi_lista[indice] = 1.5
mi_conjunto = set(mi_lista)
print(mi_conjunto)

print("🔥 eliminar")
mi_conjunto.remove(1.5)
# mi_conjunto.remove(1.5)
print(mi_conjunto)

mi_conjunto.discard(1)
mi_conjunto.discard(1)
print(mi_conjunto)

mi_conjunto.pop()  # la eliminacion es al azar
print(mi_conjunto)

mi_conjunto.clear()
print(mi_conjunto)
