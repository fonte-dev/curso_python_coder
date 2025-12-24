# --- MÉTODOS DE DICCIONARIOS ---

colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}

# 1. GET (El método más seguro para consultar)
# Si la clave existe, trae el valor.
print(f"Amarillo en inglés: {colores.get('amarillo')}")

# Si la clave NO existe, devuelve None (o un valor por defecto) sin romper el programa.
# print(colores['rojo']) -> Esto daría ERROR (KeyError)
print(f"Rojo en inglés: {colores.get('rojo', 'No encontrado')}")


# 2. KEYS (Solo las llaves)
keys = colores.keys()
print(f"Claves: {keys}")


# 3. VALUES (Solo los valores)
valores = colores.values()
print(f"Valores: {valores}")


# 4. ITEMS (Pares Clave-Valor en tuplas)
items = colores.items()
print(f"Items (Pares): {items}")


# 5. ITERACIÓN (Adelanto de 'For Loops')
# Desempaquetamos la clave y el valor en cada vuelta
print("\n--- Iterando el diccionario ---")
for clave, valor in colores.items():
    print(f"La clave es {clave} y el valor es {valor}")
