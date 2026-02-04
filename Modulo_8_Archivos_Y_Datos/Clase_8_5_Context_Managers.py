# --- UNIDAD 8.5: CONTEXT MANAGERS (WITH) ---
# Descripción: Por que usar 'with' es obligatorio y no opcional.
# Nota Mental:
# - 'with' NO es una función, es una Sentencia de Control de Flujo.
# - Se encarga de "limpiar" cuando termino de usar algo (cerrar archivos, cortar conexiones).
# - Es el equivalente a un guardia de seguridad que cierra la puerta detrás mio,
#   incluso si me desmayo (error) adentro de la habitación.


def forma_antigua_peligrosa():
    print("--- FORMA ANTIGUA (Manual) ---")
    # 1. Abro el recurso
    archivo = open("peligro.txt", "w", encoding="utf-8")

    try:
        # 2. Uso el recurso
        archivo.write("Texto de prueba.")
        # Si aca ocurre un error (ej: se corta la luz, division por cero),
        # la linea de abajo NUNCA se ejecuta y el archivo queda abierto en RAM.

    finally:
        # 3. Tengo que acordarme explícitamente de cerrar
        archivo.close()
        print("Archivo cerrado manualmente.")


def forma_nueva_segura():
    print("\n--- FORMA NUEVA (Con WITH) ---")
    # El 'with' hace los pasos 1 y 3 automáticamente.
    # Open crea el objeto y lo asigna a la variable 'archivo'.

    with open("seguro.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Texto con with.")
        print("Escribiendo datos...")
        # Apenas salgo de este bloque (por indentación), Python cierra el archivo.
        # No importa si salgo porque termine o porque hubo un error.

    # Aca afuera, el archivo ya esta cerrado.
    print("El bloque termino, archivo cerrado automáticamente.")


def prueba_de_error():
    print("\n--- PRUEBA DE ROBUSTEZ ---")
    try:
        with open("error_test.txt", "w", encoding="utf-8") as f:
            f.write("Empezando a escribir...")
            print("Simulando un error grave dentro del with...")

            # Fuerzo un error matemático para romper el programa
            x = 10 / 0

            f.write("Esto nunca se va a escribir.")

    except ZeroDivisionError:
        print("¡Ocurrió un error! (Division por cero)")

    # A pesar del error, el archivo se cerro correctamente.
    # Si no usara with, el archivo habría quedado corrupto o bloqueado.
    print("El sistema se recupero y el archivo esta cerrado y a salvo.")


if __name__ == "__main__":
    forma_antigua_peligrosa()
    forma_nueva_segura()
    prueba_de_error()
