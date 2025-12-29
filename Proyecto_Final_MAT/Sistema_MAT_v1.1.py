# --- PROJECT MAT v1.1: SISTEMA DE GESTIÓN ---
# Autor: Juan Pablo Fonte (AT)
# Descripción: Sistema de gestión de pacientes y evoluciones (CLI).

import os
import time

# Base de datos volátil (Listas)
pacientes = ["Juan Perez", "Maria Gomez"]
evoluciones = []


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


print("INICIANDO SISTEMA MAT...")
time.sleep(1)

while True:
    limpiar_pantalla()
    print("\n" + "=" * 40)
    print("       ACOMPAÑAMIENTO TERAPÉUTICO")
    print("=" * 40)
    print(f"Pacientes activos: {len(pacientes)}")
    print("-" * 40)
    print("1. 👥 Ver Lista de Pacientes")
    print("2. ➕ Registrar Nuevo Paciente")
    print("3. 📝 Cargar Evolución Diaria")
    print("4. 📜 Ver Historial de Evoluciones")
    print("5. 🚪 Salir")
    print("=" * 40)

    opcion = input(">>> Tu elección: ")

    # --- OPCIÓN 1: VER PACIENTES ---
    if opcion == "1":
        print("\n--- NOMINA DE PACIENTES ---")
        for i, p in enumerate(pacientes):
            print(f"{i+1}. {p}")

        input("\n[Presione Enter para volver al menú...]")

    # --- OPCIÓN 2: AGREGAR PACIENTE ---
    elif opcion == "2":
        # Validación: No permitir nombre vacío
        while True:
            nuevo_p = input("\nNombre del nuevo paciente: ").strip().title()
            if len(nuevo_p) > 0:
                break
            print("❌ El nombre no puede estar vacío.")

        if nuevo_p in pacientes:
            print("⚠️ Ese paciente ya existe.")
        else:
            pacientes.append(nuevo_p)
            print(f"✅ {nuevo_p} agregado al sistema.")
        time.sleep(1.5)

    # --- OPCIÓN 3: CARGAR EVOLUCIÓN ---
    elif opcion == "3":
        print("\n--- CARGA DE EVOLUCIÓN ---")
        for i, p in enumerate(pacientes):
            print(f"{i+1}. {p}")

        try:
            indice = int(input("Seleccione número de paciente: ")) - 1
            if 0 <= indice < len(pacientes):
                paciente_selec = pacientes[indice]
                print(f"Escribiendo evolución para: {paciente_selec}")

                # Validación de contenido (evitar notas vacías)
                while True:
                    texto = input("Detalle: ").strip()
                    if len(texto) > 0:
                        break
                    else:
                        print("❌ Error: No se puede guardar una nota vacía.")

                dia = "29/12"  # TODO: Implementar fecha automática
                registro = f"[{dia}] {paciente_selec}: {texto}"
                evoluciones.append(registro)
                print("✅ Evolución guardada.")
            else:
                print("❌ Número incorrecto.")
        except ValueError:
            print("❌ Debe ingresar un número.")

        time.sleep(1.5)

    # --- OPCIÓN 4: LEER HISTORIAL ---
    elif opcion == "4":
        print("\n--- BITÁCORA DE EVOLUCIONES ---")
        if len(evoluciones) == 0:
            print("No hay registros aún.")
        else:
            for nota in evoluciones:
                print(nota)
        input("\n[Presione Enter para volver...]")

    # --- SALIR ---
    elif opcion == "5":
        print("Cerrando sesión. ¡Buen descanso!")
        break

    else:
        print("Opción no válida.")
        time.sleep(1)
