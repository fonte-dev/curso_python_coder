# --- UNIDAD 4: CONTROL DE FLUJO ---
# Descripción: Compilado de ejercicios de la clase práctica (If, While, For).

import time


def separador(titulo):
    print("\n" + "=" * 50)
    print(f"--- {titulo} ---")
    print("=" * 50)


# ==========================================
# 1. GENERACIONES
# ==========================================
def generaciones():
    separador("EJERCICIO 1: GENERACIONES")
    # Consigna: Indicar generación según año. Validar huecos.

    try:
        anio = int(input("Ingresá tu año de nacimiento: "))

        if 1920 <= anio <= 1940:
            print(f"{anio}: Generación Silenciosa")
        elif 1946 <= anio <= 1964:
            print(f"{anio}: Baby Boomer")
        elif 1965 <= anio <= 1979:
            print(f"{anio}: Generación X")
        elif 1980 <= anio <= 2000:
            print(f"{anio}: Generación Y (Millennial)")
        elif 2001 <= anio <= 2010:
            print(f"{anio}: Generación Z 📱")
        else:
            print("No existe generación asociada para este año.")
    except ValueError:
        print("Error: Por favor ingresá un número válido.")


# ==========================================
# 2. CRÉDITO BANCARIO (Lógica de Booleana)
# ==========================================
def credito_bancario():
    separador("EJERCICIO 2: APROBACIÓN DE CRÉDITO")

    # Datos para probar la lógica según la consigna
    edad = 15
    antiguedad = 10
    ingreso = 1500

    print(
        f"Evaluando cliente: Edad {edad}, Antigüedad {antiguedad}, Ingreso ${ingreso}"
    )

    # Lógica desglosada
    es_mayor = edad >= 18
    tiene_perfil_financiero = (antiguedad >= 3) and (ingreso > 2500)
    es_vip = ingreso >= 4000

    # Condición Final: Mayor de edad Y (Perfil financiero O VIP)
    if es_mayor and (tiene_perfil_financiero or es_vip):
        print("Crédito APROBADO")
    else:
        print("Crédito RECHAZADO")


# ==========================================
# 3. MARVEL VS CAPCOM (Lógica de Conjuntos)
# ==========================================
def marvel_vs_capcom():
    separador("EJERCICIO 3: GRUPOS A y B")

    nombre = input("¿Cómo te llamas?: ").capitalize()
    preferencia = input("¿Tu preferencia? (Marvel/Capcom): ").strip().capitalize()

    # Grupo A:
    # (Fan Marvel AND Nombre < M) OR (Fan Capcom AND Nombre > N)

    es_fan_marvel = preferencia == "Marvel"
    es_fan_capcom = preferencia == "Capcom"

    # Python puede comparar letras alfabéticamente ("Alan" < "M")
    if (es_fan_marvel and nombre < "M") or (es_fan_capcom and nombre > "N"):
        grupo = "A"
    else:
        grupo = "B"

    print(f"Hola {nombre}, te corresponde el grupo: {grupo}")


# ==========================================
# 4. SUMA CON INPUT (While + Acumulador)
# ==========================================
def suma_numeros():
    separador("EJERCICIO 4: SUMADORA (Escribe 'exit' para salir)")

    suma_total = 0

    while True:
        entrada = input("Ingresa un número (o 'exit'): ").lower()

        if entrada == "exit":
            break  # Rompe el bucle while

        # Validación interna
        if entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit()):
            numero = int(entrada)
            suma_total += numero
            print(f"   -> Suma parcial: {suma_total}")
        else:
            print("⚠️ Eso no es un número entero.")

    print(f"\n💰 RESULTADO FINAL: {suma_total}")


# ==========================================
# 5. SENTENCIA BREAK (Análisis)
# ==========================================
def analisis_break():
    separador("EJERCICIO 5: ANÁLISIS DE BREAK")
    print("Código a analizar:")
    print("x = 5")
    print("while True:")
    print("    x -= 1")
    print("    if x == 0: break")

    print("\n--- Ejecución ---")
    x = 5
    while True:
        x -= 1
        print(f"Valor de x: {x}")
        if x == 0:
            break
    print("Fin del bucle (Break se activó cuando x llegó a 0)")


# ==========================================
# 6. CANCIÓN 'ME GUSTA' (For + Listas)
# ==========================================
def cancion_manu_chao():
    separador("EJERCICIO 6: MANU CHAO")

    # Lista de cosas que me gustan
    cosas_que_gustan = [
        "los aviones",
        "viajar",
        "la mañana",
        "el viento",
        "soñar",
        "la mar",
    ]

    # Iteramos usando FOR
    for cosa in cosas_que_gustan:
        print(f"🎵 Me gusta {cosa}, me gustas tú")


# ==========================================
# MENU PRINCIPAL
# ==========================================
def main():
    while True:
        separador("MENÚ UNIDAD 4")
        print("1. Generaciones")
        print("2. Crédito Bancario")
        print("3. Marvel vs Capcom")
        print("4. Sumadora (Input Loop)")
        print("5. Ejemplo Break")
        print("6. Canción Me Gusta")
        print("0. Salir")

        op = input("\nElección: ")

        if op == "1":
            generaciones()
        elif op == "2":
            credito_bancario()
        elif op == "3":
            marvel_vs_capcom()
        elif op == "4":
            suma_numeros()
        elif op == "5":
            analisis_break()
        elif op == "6":
            cancion_manu_chao()
        elif op == "0":
            break
        else:
            print("Opción inválida")

        time.sleep(1)


if __name__ == "__main__":
    main()
