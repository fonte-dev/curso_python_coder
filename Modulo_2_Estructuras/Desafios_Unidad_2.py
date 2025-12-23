# --- DESAFÍOS UNIDAD 2: ESTRUCTURAS DE DATOS ---

# ==========================================
# 1. DESAFÍO DE LISTAS
# ==========================================
print("\n--- 1. DESAFÍO LISTAS ---")

# Crear listas iniciales con valores arbitrarios
lista_1 = [10, 20, 30]
lista_2 = ["Python", "Java", "C++"]

# Añadir elementos a lista_1
lista_1.append(456789)
lista_1.append("Hola Mundo")

# Añadir elementos a lista_2
lista_2.append("Hola y adiós")
lista_2.append(5555)

print(f"Lista 1 base: {lista_1}")
print(f"Lista 2 base: {lista_2}")

# Generar lista_3 (Todo lista_1 menos el último)
lista_3 = lista_1[:-1]

# Generar lista_4 (Todo lista_2 menos el primero y el último)
lista_4 = lista_2[1:-1]

# Generar lista_5 (Concatenación de lista_4 y lista_3)
lista_5 = lista_4 + lista_3

print(f"Lista 3 (Sin el último): {lista_3}")
print(f"Lista 4 (Sin primero ni último): {lista_4}")
print(f"Lista 5 (Combinada): {lista_5}")


# ==========================================
# 2. DESAFÍO DE TUPLAS
# ==========================================
print("\n--- 2. DESAFÍO TUPLAS ---")

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print(f"Tupla original: {tupla}")

# El último ítem
print(f"Último ítem: {tupla[-1]}")

# Número de ítems (Largo)
print(f"Largo de la tupla: {len(tupla)}")

# Posición (índice) donde está el 87
# .index() busca el valor y te dice la posición
print(f"Posición del número 87: {tupla.index(87)}")

# Lista con los últimos tres ítems
# Slicing desde -3 hasta el final
print(f"Últimos 3 ítems: {list(tupla[-3:])}")

# Ítem en la posición 8
print(f"Ítem en posición 8: {tupla[8]}")

# Número de veces que aparece el 7
# .count() cuenta las repeticiones
print(f"Cantidad de veces que aparece el 7: {tupla.count(7)}")


# ==========================================
# 3. DESAFÍO DE SETS (CONJUNTOS)
# ==========================================
print("\n--- 3. DESAFÍO SETS ---")

colores = {"Rojo", "Blanco", "Azul"}
print(f"Set inicial: {colores}")

# Agregar Violeta y Dorado
colores.update({"Violeta", "Dorado"})
print(f"Set actualizado: {colores}")

# Eliminar Celeste, Blanco y Dorado
# PREGUNTA: ¿Qué pasa al eliminar 'Celeste' con discard?
# RESPUESTA: 'Celeste' no existe en el set.
# Si usamos .remove("Celeste") -> Python tira ERROR y detiene el programa.
# Si usamos .discard("Celeste") -> Python no hace nada y sigue (Es más seguro).

colores.discard("Celeste")  # No hace nada, no rompe nada.
colores.discard("Blanco")
colores.discard("Dorado")

print(f"Set final (Limpieza): {colores}")


# ==========================================
# 4. DESAFÍO DE DICCIONARIOS (FIFA)
# ==========================================
print("\n--- 4. DESAFÍO DICCIONARIOS (MUNDIALES) ---")

ganadores_mundial = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
    2018: "Francia",
}

print("Ganadores FIFA 1990-2018:")
print(ganadores_mundial)

# Extra: Si quisieras ver solo el de 2010
# print(f"Ganador 2010: {ganadores_mundial[2010]}")
