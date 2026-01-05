# --- CLASE 5.1: INTRODUCCIÓN A FUNCIONES ---
# Concepto: "Caja Negra". Meto datos -> Pasan cosas -> Sale un resultado.


# 1. FUNCIÓN SIMPLE (VOID)
# No recibe nada, no devuelve nada. Solo "hace" algo (Efecto secundario).
def saludar_generico():
    print("👋 Hola! Soy una función simple.")


# 2. FUNCIÓN CON PARÁMETROS
# Recibe datos para trabajar (Argumentos).
def saludar_personalizado(nombre):
    print(f"👋 Hola, {nombre}! ¿Todo bien?")


# 3. FUNCIÓN CON RETURN (LA IMPORTANTE)
# Procesa datos y ENTREGA un resultado para que el programa lo use después.
# NO imprime nada, devuelve el valor.
def sumar(a, b):
    resultado = a + b
    return resultado


# --- ZONA DE EJECUCIÓN ---
print("--- PRUEBAS DE FUNCIONES ---")

# Llamada simple
saludar_generico()

# Llamada con argumento
saludar_personalizado("Juan Pablo")

# Uso del Return
# Como la función 'sumar' devuelve un valor, lo puedo guardar en una variable.
total = sumar(10, 20)
print(f"El total calculado es: {total}")

# 4. REGLA DE ORO
# "Las funciones deben hacer UNA sola cosa."
# Mal: calcular_y_imprimir_y_guardar()
# Bien: calcular() -> imprimir() -> guardar()
