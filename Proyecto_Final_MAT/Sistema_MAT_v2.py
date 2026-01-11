# --- SISTEMA DE GESTIÓN MAT v2.0 ---
# Arquitectura: Modular (Funciones)
# Estado: Estructura vacía (Skeleton)

import os
import time
import datetime

# --- 1. DATOS GLOBALES (Por ahora) ---
pacientes = ["Juan Perez", "Maria Gomez"]
evoluciones = []


# --- 2. FUNCIONES DE UTILIDAD (Herramientas) ---
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("       ACOMPAÑAMIENTO TERAPÉUTICO")
    print("=" * 40)
    print("1. 👥 Ver Pacientes")
    print("2. ➕ Nuevo Paciente")
    print("3. 📝 Cargar Evolución")
    print("4. 📜 Ver Historial")
    print("5. 🚪 Salir")
    print("=" * 40)


def pedir_input_validado(mensaje):
    """Pide un input y no deja que sea vacío."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0:
            return texto
        print("❌ Error: El campo no puede estar vacío.")


# --- 3. FUNCIONES DE LÓGICA (Acciones) ---
def listar_pacientes():
    print("\n--- NOMINA DE PACIENTES ---")
    for i, p in enumerate(pacientes):
        print(f"{i+1}. {p}")


def registrar_paciente():
    nombre = pedir_input_validado("\nNombre del nuevo paciente: ").title()
    if nombre in pacientes:
        print("⚠️ El paciente ya existe.")
    else:
        pacientes.append(nombre)
        print(f"✅ {nombre} registrado.")
    time.sleep(1.5)


def seleccionar_paciente():
    listar_pacientes()
    entrada = pedir_input_validado("Seleccione número de paciente: ")
    return int(entrada) - 1


def cargar_evolucion():
    print("\n--- CARGA DE EVOLUCIÓN ---")
    try:
        indice = seleccionar_paciente()
        if 0 <= indice < len(pacientes):
            paciente_selec = pacientes[indice]
            print(f"Escribiendo evolución para: {paciente_selec}")
            texto = pedir_input_validado("Detalle de la evolución: ").capitalize()
            dia = datetime.datetime.now().strftime("%d/%m %H:%M")
            registro = f"[{dia}] {paciente_selec}: {texto}"
            evoluciones.append(registro)
            print("✅ Evolución guardada.")
        else:
            print("❌ Número incorrecto (Fuera de rango).")

    except ValueError:
        print("❌ Error: Debe ingresar un número entero.")

    time.sleep(1.5)


def ver_historial():
    print("\n--- BITÁCORA DE EVOLUCIONES ---")
    if len(evoluciones) == 0:
        print("No hay registros aún.")
    else:
        for nota in evoluciones:
            print(nota)


# --- 4. ORQUESTADOR PRINCIPAL ---
def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input(">>> Selección: ")

        if opcion == "1":
            listar_pacientes()
            input("\n[Enter] para volver...")
        elif opcion == "2":
            registrar_paciente()
        elif opcion == "3":
            cargar_evolucion()
        elif opcion == "4":
            ver_historial()
            input("\n[Enter] para volver...")
        elif opcion == "5":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")
            time.sleep(1)


# Entry Point
if __name__ == "__main__":
    main()
