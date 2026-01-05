# --- CLASE 5.8: ACTIVIDAD PRÁCTICA (DESAFÍO) ---
# Autor: Juan Pablo Fonte
# Tema: Consolidación de Funciones, Lógica Booleana y Validaciones.

import math


# ==========================================
# 1. AÑO BISIESTO (Lógica Condicional Compleja)
# ==========================================
def anio_bisiesto(anio):
    """
    Regla: Es bisiesto si es divisible por 4.
    EXCEPCIÓN: Si es divisible por 100, NO es bisiesto.
    CONTRA-EXCEPCIÓN: Si es divisible por 400, SÍ es bisiesto.
    """
    # Validación de tipo (Consigna: "indicar que se ingrese un número")
    # Convertimos a string para chequear si son digitos
    if type(anio) != int:
        # Si no es entero, intento ver si es un string numérico
        if isinstance(anio, str) and anio.isdigit():
            anio = int(anio)  # Lo convierto
        else:
            print("⚠️ Error: Debes ingresar un número entero.")
            return  # Corto la ejecución acá (Early Return)

    # Lógica del algoritmo
    # (Divisible x 4 AND NO divisible x 100) OR (Divisible x 400)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")


# ==========================================
# 2. ÁREA RECTÁNGULO (Cálculo Simple)
# ==========================================
def area_rectangulo(base, altura):
    return base * altura


# ==========================================
# 3. ÁREA CÍRCULO (Uso de librerías)
# ==========================================
def area_circulo(radio):
    # Formula: Pi * radio al cuadrado
    # math.pi es más preciso que 3.14159
    return math.pi * (radio**2)


# ==========================================
# 4. RELACIÓN (Comparación)
# ==========================================
def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


# ==========================================
# 5. PUNTO INTERMEDIO (Promedio)
# ==========================================
def intermedio(a, b):
    return (a + b) / 2


# ==========================================
# 6. RECORTAR (Clamping / Limitar Rango)
# ==========================================
# Sirve para limitar valores (ej: dosis máximas, temperatura, etc).
def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo  # Si es muy chico, devuelvo el piso
    elif numero > maximo:
        return maximo  # Si es muy grande, devuelvo el techo
    return numero  # Si está bien, lo dejo pasar


# ==========================================
# ZONA DE PRUEBAS (MAIN)
# ==========================================
def main():
    print("\n--- EJERCICIO 1: AÑOS BISIESTOS ---")
    anio_bisiesto(2012)  # Esperado: Sí
    anio_bisiesto(2010)  # Esperado: No
    anio_bisiesto(2000)  # Esperado: Sí (Múltiplo de 400)
    anio_bisiesto(1900)  # Esperado: No (Múltiplo de 100 pero no de 400)
    anio_bisiesto("Hola")  # Esperado: Error

    print("\n--- EJERCICIO 2: RECTÁNGULO ---")
    base, altura = 15, 10
    print(f"Base {base} x Altura {altura} = Área {area_rectangulo(base, altura)}")

    print("\n--- EJERCICIO 3: CÍRCULO ---")
    radio = 5
    # :.4f formatea a 4 decimales
    print(f"Radio {radio} = Área {area_circulo(radio):.4f}")

    print("\n--- EJERCICIO 4: RELACIÓN ---")
    print(f"5 vs 10: {relacion(5, 10)}")  # Esperado: -1
    print(f"10 vs 5: {relacion(10, 5)}")  # Esperado: 1
    print(f"5 vs 5:  {relacion(5, 5)}")  # Esperado: 0

    print("\n--- EJERCICIO 5: INTERMEDIO ---")
    n1, n2 = -12, 24
    print(f"Punto medio entre {n1} y {n2}: {intermedio(n1, n2)}")

    print("\n--- EJERCICIO 6: RECORTAR (CLAMP) ---")
    # Recortar 15 entre 0 y 10 -> Debería dar 10 (el techo)
    valor = 15
    limite_inf = 0
    limite_sup = 10
    resultado = recortar(valor, limite_inf, limite_sup)
    print(f"Recortar {valor} en rango [{limite_inf}, {limite_sup}] -> {resultado}")


# Ejecutar todo
if __name__ == "__main__":
    main()
