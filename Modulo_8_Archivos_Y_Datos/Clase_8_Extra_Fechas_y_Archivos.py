# --- BONUS: ARCHIVOS CON FECHA (LOGS) ---
# Descripción: Usando 'datetime' para crear archivos con nombre único.
# Nota Mental:
# - datetime.now() me da la fecha actual.
# - strftime() le da formato de texto (ej: "04-02-2026").
# - Esto sirve para no sobrescribir backups viejos.

import datetime
import os


def crear_log_diario():
    print("--- SISTEMA DE LOGS ---")

    # 1. Obtener fecha y hora actual
    ahora = datetime.datetime.now()
    print(f"Momento exacto: {ahora}")

    # 2. Formatear la fecha para que sirva como nombre de archivo
    # %Y = Año, %m = Mes, %d = Día, %H = Hora, %M = Minuto
    nombre_archivo = ahora.strftime("log_%Y_%m_%d.txt")  # Ej: log_2026_02_04.txt

    contenido = f"Registro de actividad.\nHora de inicio: {ahora.strftime('%H:%M:%S')}\nUsuario: Juan\n"

    # 3. Guardar el archivo
    try:
        # Modo 'a' (Append) por si ejecuto el script varias veces el mismo día
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(contenido + "-" * 20 + "\n")

        print(f"Se guardó la actividad en: {nombre_archivo}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    crear_log_diario()
