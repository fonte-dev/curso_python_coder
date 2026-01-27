# --- UNIDAD 6.5: TUTORIAL DE EXCEPCIONES ---
# Fuente: Replicación del PDF "Tutorial de Excepciones"
# Descripción: Ejemplos de errores de conversión, IndexError y TypeError.


def ejemplo_basico_conversion():
    print("\n--- 1. EL ERROR DE CONVERSIÓN ---")
    print("Intentando convertir '¡Hola mundo!' a entero...")

    try:
        # Esto lanza ValueError porque no son números
        print(int("¡Hola, mundo estoy aprendiendo Python!"))
    except ValueError as e:
        print(f"Excepción capturada: {e}")


def ejemplo_bucle_robusto():
    print("\n--- 2. EL BUCLE DE VALIDACIÓN (INT + INPUT) ---")
    print("El código no avanza hasta que el usuario ingrese un número válido.")

    while True:
        try:
            # 1. Intentamos convertir
            edad = int(input("Escribe tu edad: "))

            # 2. Si la línea anterior falla, saltamos al except.
            #    Si funciona, seguimos acá:
            if edad >= 18:
                print("✅ Eres un adulto.")
            else:
                print("✅ Aún no eres un adulto.")

            # 3. Rompemos el bucle solo si todo salió bien
            break

        except ValueError:
            # 4. Si falló la conversión, caemos acá y el bucle se repite
            print("Error: Eso no es un número. Intenta de nuevo.")


def otros_errores_comunes():
    print("\n--- 3. OTROS TIPOS DE EXCEPCIONES ---")

    # CASO A: IndexError (Fuera de límites)
    print("A) Intentando acceder a la posición 5 de una lista de 4 elementos...")
    lenguajes = ["Java", "R", "C++", "Python"]
    try:
        print(lenguajes[5])
    except IndexError as e:
        print(f"IndexError: {e}")

    # CASO B: TypeError (Tipo de dato incorrecto)
    print("\nB) Intentando convertir una lista entera a un solo int...")
    try:
        # No podés convertir una lista [2, 4] a un número entero
        print(int([2, 4]))
    except TypeError as e:
        print(f"TypeError: {e}")


# --- ORQUESTADOR ---
if __name__ == "__main__":
    ejemplo_basico_conversion()
    ejemplo_bucle_robusto()
    otros_errores_comunes()
