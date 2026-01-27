# --- UNIDAD 6: MANEJO DE EXCEPCIONES ---
# Descripción: Patrones de manejo de errores (Try, Except, Else, Finally).


def manejo_basico():
    """Captura genérica (No recomendada para todo, pero útil)."""
    print("\n--- 1. MANEJO BÁSICO ---")
    try:
        lista = ["Pan", "Leche"]
        print(lista[5])  # Esto va a fallar (Índice fuera de rango)
    except Exception as e:
        # 'e' contiene el mensaje técnico del error
        print(f"Ocurrió un error inesperado: {e}")


def manejo_especifico():
    """Captura errores específicos por tipo."""
    print("\n--- 2. MANEJO ESPECÍFICO ---")
    try:
        # Simulamos inputs
        n1 = int(input("Numerador: "))
        n2 = int(input("Denominador: "))
        res = n1 / n2
        print(f"Resultado: {res}")

    except ValueError:
        print("Error: Debes ingresar números enteros, no letras.")
    except ZeroDivisionError:
        print("Error: No podés dividir por cero (Matemática básica).")
    except Exception as e:
        print(f"Error desconocido: {e}")


def flujo_completo():
    """
    El ciclo de vida completo de una excepción:
    TRY -> Intentar código peligroso.
    EXCEPT -> Si falla, vení acá.
    ELSE -> Si NO falla, vení acá.
    FINALLY -> Pase lo que pase, ejecutá esto (limpieza).
    """
    print("\n--- 3. FLUJO COMPLETO (TRY-EXCEPT-ELSE-FINALLY) ---")
    archivo = None
    try:
        # Intentamos abrir un archivo (simulado)
        nombre = input("Nombre del archivo a simular (escribe 'error' para fallar): ")

        if nombre == "error":
            raise FileNotFoundError("Simulación de archivo no encontrado")

        print("Archivo abierto correctamente.")

    except FileNotFoundError:
        print("Excepción: El archivo no existe.")

    else:
        print("Éxito: Esto solo se ejecuta si NO hubo errores en el try.")
        # Acá iría la lógica de leer el archivo

    finally:
        print("Limpieza: Esto se ejecuta SIEMPRE (Cerrando conexión DB/Archivo).")


# --- ORQUESTADOR ---
if __name__ == "__main__":
    while True:
        print("\n=== LABORATORIO DE EXCEPCIONES ===")
        print("1. Error de Índice (Genérico)")
        print("2. Calculadora (ValueError / ZeroDivision)")
        print("3. Ciclo Completo (Else / Finally)")
        print("0. Salir")

        op = input(">>> ")

        if op == "1":
            manejo_basico()
        elif op == "2":
            manejo_especifico()
        elif op == "3":
            flujo_completo()
        elif op == "0":
            break
        else:
            print("Opción no válida")
