# --- UNIDAD 8.4: MANEJO DE ARCHIVOS CSV ---
# Description: Lectura y escritura de datos tabulares (Excel-like).
# Nota Mental:
# - CSV = Valores Separados por Comas.
# - newline='' es OBLIGATORIO en open() para evitar filas en blanco en Windows.
# - reader devuelve LISTAS: ['Juan', '30'] (Accedo por indice [0]).
# - DictReader devuelve DICCIONARIOS: {'nombre': 'Juan'} (Accedo por clave ['nombre']).

import csv


def crear_csv_prueba():
    # Datos iniciales (Lista de listas)
    datos = [
        ["nombre", "edad", "rol"],
        ["Juan", "30", "Admin"],
        ["Ana", "25", "User"],
        ["Pedro", "23", "Guest"],
    ]

    # Escribo el archivo inicial
    # newline='' evita que Windows ponga un doble enter entre filas
    with open("usuarios_prueba.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)

    print("Archivo 'usuarios_prueba.csv' generado.")


def leer_csv_como_lista():
    print("\n--- LECTURA COMO LISTA (csv.reader) ---")
    # Es mas rápido pero menos legible porque accedo por números [0], [1]

    try:
        with open("usuarios_prueba.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # next(lector) sirve para saltar la primera fila (los encabezados)
            # si no hago esto, me imprime 'nombre', 'edad', 'rol' como si fuera un usuario mas
            encabezados = next(lector)
            print(f"Encabezados detectados: {encabezados}")

            for fila in lector:
                # fila es una lista: ['Juan', '30', 'Admin']
                print(f"Usuario: {fila[0]} - Rol: {fila[2]}")

    except FileNotFoundError:
        print("El archivo no existe.")


def leer_csv_como_dict():
    print("\n--- LECTURA COMO DICCIONARIO (csv.DictReader) ---")
    # Es mas profesional. No necesito saltar el encabezado manualmente con next()
    # porque DictReader usa la primera fila para crear las claves del diccionario automáticamente.

    try:
        with open("usuarios_prueba.csv", newline="", encoding="utf-8") as archivo:
            lector_dict = csv.DictReader(archivo)

            for fila in lector_dict:
                # fila es un diccionario: {'nombre': 'Juan', 'edad': '30', ...}
                # Esto es mucho mas seguro que usar indices numéricos
                print(f"Nombre: {fila['nombre']} | Edad: {fila['edad']}")

    except FileNotFoundError:
        print("El archivo no existe.")


def agregar_datos_csv():
    print("\n--- AGREGAR DATOS (APPEND) ---")
    # Modo 'a' para agregar al final sin borrar lo anterior

    nuevo_usuario = ["Luis", "40", "SuperAdmin"]

    with open("usuarios_prueba.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(nuevo_usuario)
        print("Usuario Luis agregado.")


if __name__ == "__main__":
    # 1. Crear entorno
    crear_csv_prueba()

    # 2. Leer forma básica
    leer_csv_como_lista()

    # 3. Leer forma pro
    leer_csv_como_dict()

    # 4. Modificar archivo
    agregar_datos_csv()
