# Operaciones con Conjuntos

conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

print("*** Union")
union_AB = conjunto_A.union(conjunto_B)
print(union_AB)

print("*** Intersección")
interseccion_AB = conjunto_A.intersection(conjunto_B)
print(interseccion_AB)

print("*** Diferencia")
diferencia_AB = conjunto_A.difference(conjunto_B)
print(diferencia_AB)

print("*** Diferencia Simmetrica")
diferencia_simmetrica_AB = conjunto_A.symmetric_difference(conjunto_B)
print(diferencia_simmetrica_AB)

print("*** Subconjunto")
conjunto_C = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_D = {1, 2}
pregunta = conjunto_D.issubset(conjunto_C)
print(pregunta)

print("*** Superconjunto")
pregunta = conjunto_C.issuperset(conjunto_D)
print(pregunta)

print("*** Actualizar conjuntos")
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}
conjunto_A.update(conjunto_B)
print(conjunto_A)

print("*** Actualizar con la diferencia")
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}
conjunto_A.symmetric_difference_update(conjunto_B)
print(conjunto_A)
