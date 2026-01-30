# --- CLASE 5.5: PARÁMETROS, ARGUMENTOS Y MODULARIDAD ---
# Concepto: Dividir el problema en "responsabilidades" (SRP), o bloques lógicos (Input -> Proceso -> Output).


# 1. FUNCIÓN DE INPUT (Responsabilidad: Conseguir datos limpios)
def ingresar_notas():
    notas = []
    while True:
        entrada = input("Ingrese una nota (escriba 'fin' para salir): ")

        if entrada == "fin":
            break
        elif entrada == "":
            print("No se ingresó ninguna nota")
            continue

        # Validación de tipo y rango
        if entrada.isdecimal():
            nota = int(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10")
        else:
            print("La nota debe ser un número entero")

    return notas  # Devuelve la lista limpia


# 2. FUNCIÓN DE PROCESO (Responsabilidad: Calcular lógica pura. No imprime ni pide datos. Recibe -> Calcula -> Devuelve.)
def calcular_promedio(notas):
    # Evitamos división por cero
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


# 3. FUNCIÓN DE OUTPUT (Responsabilidad: Mostrar los resultados de forma linda al usuario)
def mostrar_datos(promedio, notas):
    print("\n" + "-" * 30)
    print(f"Notas registradas: {notas}")
    print(f"Promedio final: {promedio:.2f}")  # .2f limita a mostrar 2 decimales
    print("-" * 30)


# 4. FUNCIÓN PRINCIPAL (Orquestador. Responsabilidad: Coordinar a las otras 3 funciones.)
def main():
    print("--- INICIO DEL SISTEMA ---")

    # A. Paso 1: Conseguir datos
    mis_notas = ingresar_notas()

    # B. Paso 2: Calcular (Solo si hay notas)
    if len(mis_notas) > 0:
        prom_final = calcular_promedio(mis_notas)
        # C. Paso 3: Mostrar
        mostrar_datos(prom_final, mis_notas)
    else:
        print("No se cargaron notas.")


# Entry Point (Punto de entrada estándar en Python)
main()
