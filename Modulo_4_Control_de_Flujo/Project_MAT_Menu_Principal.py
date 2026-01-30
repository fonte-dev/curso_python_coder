# --- PROJECT MERITUM: MENÚ PRINCIPAL ---
# Notas: Estructura base para navegar por el sistema.
# Usa un while True para mantenerse vivo.

import os

while True:
    print("\n" + "=" * 40)
    print("   SISTEMA DE GESTIÓN: ACOMPAÑAMIENTO T.")
    print("=" * 40)
    print("1. Ingresar Evolución")
    print("2. Evaluación de Crisis (Triaje)")
    print("3. Salir")
    print("-" * 40)

    opcion = input(">>> Su elección: ")

    if opcion == "1":
        print("\n[MODULO] Ingresando datos del paciente...")
        # Acá iría la lógica de inputs y listas
        input("Presione Enter para volver al menú...")

    elif opcion == "2":
        print("\n[MODULO] Protocolo de Crisis")

        # validación DE INPUT (no permitir números equivocados como 32)
        while True:
            try:
                excitacion = int(input("Nivel de excitación (1-10): "))
                if 1 <= excitacion <= 10:
                    break  # Salgo del bucle de validación
                else:
                    print("Error: Debe ser entre 1 y 10.")
            except ValueError:
                print("Error: Escriba un numero, no letras.")

        # Ahora sí, evaluamos con el dato limpio
        if excitacion >= 6:
            print("ALERTA: Paciente desregulado.")
        else:
            print("Paciente estable.")

        input("Enter para continuar...")

    elif opcion == "3":
        print("\nCerrando sistema")
        break  # Rompe el bucle principal y termina

    else:
        print("\nOpción errónea. Prueba de nuevo.")
