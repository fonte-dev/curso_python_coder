# --- MÉTODOS DE LISTAS ---

# 1. CLEAR
letras = ["a", "b", "c", "d", "e"]
letras.clear()
print(f"Lista limpia: {letras}")

# 2. EXTEND
numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(f"Extend: {numeros}")

# 3. INSERT
numeros = [1, 2, 3, 4]
numeros.insert(2, "Hola")
print(f"Insert: {numeros}")

# 4. REVERSE
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(f"Reverse: {numeros}")

# 5. SORT
lista_numeros = [5, 2, 9, 1, 5, 6]
lista_numeros.sort()
print(f"Sort Ascendente: {lista_numeros}")

lista_numeros.sort(reverse=True)
print(f"Sort Descendente: {lista_numeros}")
