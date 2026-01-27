# --- UNIDAD 6.1: TIPOS DE ERRORES Y TYPE HINTS ---
# Descripción: Diferencias entre errores de sintaxis, nombre, semánticos y uso de tipado estático.


def error_sintaxis():
    print("\n--- 1. ERROR DE SINTAXIS (SyntaxError) ---")
    print("Ocurre cuando escribimos mal el código (falta paréntesis, dos puntos, etc).")
    print("Python detecta esto ANTES de ejecutar el programa.")

    # Ejemplo (Descomentar para ver fallar):
    # if 5 > 3
    #     print("Faltan los dos puntos")
    print("Ejemplo comentado para que el script corra.")


def error_nombre():
    print("\n--- 2. ERROR DE NOMBRE (NameError) ---")
    print("Ocurre cuando usamos una variable que no existe o está mal escrita.")

    try:
        # Intentamos imprimir una variable que no definimos
        # print(mensaje_inexistente)

        # Simulación del error:
        raise NameError("name 'mensaje_inexistente' is not defined")
    except NameError as e:
        print(f"Error capturado: {e}")


def error_semantico():
    print("\n--- 3. ERROR SEMÁNTICO (Lógica) ---")
    print("El código corre perfecto, pero el resultado está mal (falla humana).")

    # Objetivo: Sumar a + b
    a = 5
    b = 10

    # Error: Usamos multiplicación (*) en vez de suma (+)
    resultado = a * b

    print(f"Esperado: 15 (5 + 10)")
    print(f"Obtenido: {resultado} (5 * 10) <--- ¡BUG LÓGICO!")


def sistema_tipado():
    print("\n--- 4. TYPE HINTS (Tipado Estático) ---")
    print("Ayuda al editor a detectar errores de tipo antes de ejecutar.")

    # Definición con Type Hints: (param: tipo) -> tipo_retorno
    def sumar_estricto(n1: int, n2: int) -> int:
        """Suma dos enteros."""
        return n1 + n2

    # Uso correcto
    res = sumar_estricto(10, 20)
    print(f"Suma correcta (10+20): {res}")

    # Uso incorrecto (Python lo permite, pero el editor te avisa)
    # res_mal = sumar_estricto("10", "20")
    # print(f"Suma incorrecta de textos: {res_mal}")


# --- ORQUESTADOR ---
if __name__ == "__main__":
    error_sintaxis()
    error_nombre()
    error_semantico()
    sistema_tipado()
