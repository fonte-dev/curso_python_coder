# --- UNIDAD 8.2: LECTURA Y ESCRITURA DE ARCHIVOS ---
# Descripción: Lectura segura de archivos con manejo de errores y Context Manager.
# Nota Mental:
# - open() solo es peligroso si me olvido el close().
# - with open(): abre y cierra la puerta solo.
# - encoding='utf-8' siempre para evitar problemas con tildes.


def crear_archivos_prueba():
    """
    Genera los archivos .txt necesarios para que el ejemplo funcione.
    Usa el modo 'w' (write) que crea o sobreescribe.
    """
    print("--- 1. GENERANDO ARCHIVOS DE PRUEBA ---")

    # Archivo 1
    contenido_ejemplo = "Cadena de texto.\nMas cadenas de texto.\n"
    with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_ejemplo)

    # Archivo 2
    contenido_django = "Django es un framework web de alto nivel escrito en Python.\nSigue el patron de diseño Model-View-Controller (MVC)."
    with open("django.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido_django)

    print("Archivos 'ejemplo.txt' y 'django.txt' creados/reseteados.\n")


def leer_archivo_seguro():
    """
    Intenta leer un archivo y devuelve sus líneas en una lista.
    Maneja errores si el archivo no existe.
    """
    nombre_archivo = "django.txt"

    try:
        with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
            lectura = archivo.readlines()
            return lectura

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return []  # Retorno lista vacía para no romper el main

    except Exception as e:
        print(f"Error inesperado: {repr(e)}")
        return []


def main():
    # 1. Primero aseguro que existan los archivos
    crear_archivos_prueba()

    # 2. Intento leer
    print("--- 2. LEYENDO CONTENIDO ---")
    lectura = leer_archivo_seguro()

    # Si la lista está vacía (por error o archivo vacío), corto acá.
    if not lectura:
        print("El archivo estaba vacío o no se pudo leer.")
        return

    # 3. Muestro el contenido
    # 'enumerate(..., start=1)' empieza a contar desde 1 en vez de 0
    for indice, texto in enumerate(lectura, start=1):
        # .strip() elimina el salto de línea (\n) que ya trae el archivo,
        # para que no quede un renglón vacío extra en el print.
        print(f"{indice} - {texto.strip()}")


if __name__ == "__main__":
    main()
