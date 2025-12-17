# Gestión de objetos anidados en python
# Paso 1: Crear una estructura de datos llamada "tienda" que sea una lista de diccionarios. Cada diccionario debe representar un producto con las siguientes claves
# id
# nombre
# especificaciones
# sucursales
# precios
#
# Paso 2: Tareas de acceso y navegación
# Extraer el valor de una clave de segundo nivel (Ejemplo: acceder a la ram del primer objeto)
# Acceder a un elemento especifico que este dentro del diccionario (Ejemplo: la categoría o sucursal)
#
# Paso 3: Tareas de manipulación
# Modificación de colecciones, añadir un nuevo elemento a la lista de sucursales dentro de uno de los productos sin sobrescribir la lista completa (usando métodos de lista)
# Calculo dinámico: Extraer un valor numérico del precio, calcular un 10% de descuento y guardar el resultado en una nueva variable
#
# Paso 4: Salida esperada. Imprimir un resumen que combine datos estáticos con los datos extraídos de la estructura usando f-strings


# --- PASO 1: CREAR LA ESTRUCTURA "TIENDA" ---
# Es una LISTA que contiene DICCIONARIOS.
# Adentro, hay más diccionarios (especificaciones/precios) y listas (sucursales).

tienda = [
    {
        "id": 1,
        "nombre": "Laptop Gamer X",
        "especificaciones": {
            "procesador": "Intel i9",
            "ram": "32GB",
            "video": "RTX 4090",
        },
        "sucursales": ["Centro", "Norte"],
        "precios": {"lista": 2000.00, "contado": 1800.00},
    }
]

# --- PASO 2: ACCESO Y NAVEGACIÓN ---

# A. Extraer valor de segundo nivel (Entramos a la lista -> diccionario -> diccionario)
memoria_ram = tienda[0]["especificaciones"]["ram"]

# B. Acceder a un elemento específico (La primera sucursal)
sucursal_principal = tienda[0]["sucursales"][0]

print(f"Dato extraído: {memoria_ram}")
print(f"Sucursal base: {sucursal_principal}")


# --- PASO 3: TAREAS DE MANIPULACIÓN ---

# A. Añadir una sucursal nueva SIN SOBRESCRIBIR (usamos append sobre la lista interna)
tienda[0]["sucursales"].append("Sur")

# B. Cálculo dinámico: 10% de descuento sobre el precio de lista
precio_base = tienda[0]["precios"]["lista"]
precio_final = precio_base * 0.90


# --- PASO 4: SALIDA ESPERADA (RESUMEN) ---
print("\n--- RESUMEN DE GESTIÓN ---")
print(f"Producto: {tienda[0]['nombre']}")
print(f"Specs: RAM {memoria_ram}")
print(f"Sucursales actualizadas: {tienda[0]['sucursales']}")
print(f"Precio Oferta (10% off): ${precio_final}")
