# --- UNIDAD 5: FUNCIONES A FONDO ---
# Descripción: Resumen de clase + Ejercicios prácticos (Docstrings, Args, Recursión).

# ==========================================
# 1. TEORÍA: DOCSTRINGS Y SCOPE
# ==========================================


def ejemplo_docstring():
    """
    Esta es la documentación de la función.
    Si pasas el mouse por encima del nombre de la función,
    verás este texto explicativo.
    """
    pass


# Variable Global
variable_test = 10


def test_scope():
    # Esta función puede LEER la variable global, pero si intenta
    # modificarla sin usar 'global', creará una nueva variable local.
    print(f"Leyendo variable global dentro de función: {variable_test}")


# ==========================================
# 2. EJERCICIOS BÁSICOS
# ==========================================


def welcome(ciudad):
    """Saluda al usuario indicando la ciudad."""
    # Uso f-strings para formatear más limpio
    print(f"¡Hola, bienvenidx a {ciudad}!")


def calcular_media(lista_numeros):
    """Recibe una lista y devuelve el promedio."""
    if len(lista_numeros) == 0:
        return 0  # Evito división por cero
    return sum(lista_numeros) / len(lista_numeros)


def es_multiplo():
    """Pide dos números y evalúa multiplicidad."""
    print("\n--- Chequeo de Múltiplos ---")
    try:
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))

        # Valido que no divida por cero
        if n1 == 0 or n2 == 0:
            print("El cero no es un divisor válido para este ejercicio.")
            return

        if n1 % n2 == 0 or n2 % n1 == 0:
            print("Son múltiplos.")
        else:
            print("No son múltiplos.")
    except ValueError:
        print("Error: Ingresá números enteros.")


# ==========================================
# 3. EJERCICIO AVANZADO: CONVERSOR INTELIGENTE (*ARGS)
# ==========================================


def conversor_medidas(*args):
    """
    Convierte unidades de distancia.
    - Si recibe 1 argumento (mm) -> Devuelve (m, cm, mm)
    - Si recibe 3 argumentos (m, cm, mm) -> Devuelve mm totales
    """
    # CASO 1: Recibe Milímetros (1 arg) -> Desglosar
    if len(args) == 1:
        total_mm = args[0]
        metros = total_mm // 1000
        resto = total_mm % 1000
        centimetros = resto // 10
        milimetros = resto % 10
        return f"{total_mm}mm equivalen a: {metros}m, {centimetros}cm, {milimetros}mm"

    # CASO 2: Recibe M, CM, MM (3 args) -> Unificar
    elif len(args) == 3:
        m, cm, mm = args
        total = (m * 1000) + (cm * 10) + mm
        return f"{m}m, {cm}cm, {mm}mm equivalen a: {total}mm"

    else:
        return "Cantidad de argumentos incorrecta (Use 1 o 3)."


# ==========================================
# 4. RECURSIVIDAD (Factorial)
# ==========================================


def factorial(n):
    """
    Calcula el factorial de n llamándose a sí misma.
    Ej: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 0 or n == 1:  # Caso Base (Freno)
        return 1
    else:
        return n * factorial(n - 1)  # Llamada Recursiva


# ==========================================
# ORQUESTADOR (MAIN)
# ==========================================
if __name__ == "__main__":
    print("--- 1. DOCSTRINGS ---")
    help(ejemplo_docstring)  # Muestra el docstring en consola

    print("\n--- 2. SCOPE ---")
    test_scope()

    print("\n--- 3. EJERCICIOS CLASE ---")
    welcome("Madrid")

    mis_nums = [2, 4, 4, 10]
    print(f"La media de {mis_nums} es: {calcular_media(mis_nums)}")

    es_multiplo()

    print("\n--- 4. CONVERSOR (*ARGS) ---")
    # Prueba A: De mm a desglosado
    print(conversor_medidas(1234))
    # Prueba B: De desgolsado a mm
    print(conversor_medidas(1, 23, 4))

    print("\n--- 5. RECURSIVIDAD ---")
    num = 5
    print(f"El factorial de {num} es: {factorial(num)}")
