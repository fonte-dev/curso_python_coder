# Listas
numeros = [1, 2, 3, 4, 5, 5, 5, 5]
print(numeros)
print(len(numeros))  # len = longitud de la  lista/cantidad de elementos
cuenta = numeros.count(5)  # count = contar repeticiones de elemento especifico
print("La cantidad de veces es:", cuenta)

desarrollo = ["Python", "C++", "Java", "C#", "JavaScript"]

print("Obtener")
mi_elemento = desarrollo[0]
print(mi_elemento)

# funcion index()

java = desarrollo.index("Java")
print(java)
print(desarrollo[java])

print("Crear")
desarrollo.append("Rust")  # apprend = agregar elemento al final de la lista de a uno
print(desarrollo)
desarrollo += ["Go", "Swift"]  # += agregar multiples elementos al mismo tiempo
print(desarrollo)

print("Modificar")
indice = desarrollo.index("C#")
desarrollo[indice] = "Mojo"  # llamo al indice y cambio su valor
print(desarrollo)

mas_lenguajes = ["Assembler", "Basic"]
desarrollo.extend(
    mas_lenguajes
)  # extiendo la lista original agregando una nueva a esta
print(desarrollo)

print("Eliminar")
indice = desarrollo.index("Basic")
del desarrollo[indice]  # remueve elemento especifico
print(desarrollo)

desarrollo.remove("Rust")  # remueve elemento especifico
print(desarrollo)

desarrollo.pop()  # remueve ultimo elemento
desarrollo.pop()
desarrollo.pop(1)  # remueve elemento de especifico indice
print(desarrollo)

desarrollo.clear()  # remueve todos los elementos de una lista
print(desarrollo)
