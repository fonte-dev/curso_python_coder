# --- CLASE EN VIVO: MÓDULOS, SYS Y __MAIN__ ---
# Descripción: Cómo recibir datos desde la consola y entender la modularización.

import sys


# 1. DEFINICIÓN DE FUNCIONES (Esto sería mi Módulo)
def saludar_formal(nombre):
    return f"Estimado/a {nombre}, bienvenido al sistema."


def calcular_doble(numero):
    return numero * 2


# 2. EL BLOQUE DE EJECUCIÓN (El "Portero")
# Este bloque SOLO se ejecuta si lanzo este archivo directamente.
# Si alguien hace 'import Clase_Vivo_Modulos_Sys', esto se ignora.
if __name__ == "__main__":
    print("--- INICIO DEL SCRIPT (Modo __main__) ---")

    # 3. USO DE SYS.ARGV (Argumentos de consola)
    # sys.argv es una LISTA con las palabras que escribo en la terminal.
    # Ejemplo de uso en terminal: python este_archivo.py Pepe 5

    print(f"Argumentos recibidos: {sys.argv}")

    try:
        # sys.argv[0] es siempre el nombre del archivo.
        # sys.argv[1] es el primer dato que paso.
        if len(sys.argv) > 1:
            usuario = sys.argv[1]
            print(saludar_formal(usuario))
        else:
            print(
                "Tip: Probá ejecutar esto en terminal así: python archivo.py TuNombre"
            )
            # Si no pasan argumentos, uso uno por defecto
            print(saludar_formal("Usuario Anónimo"))

    except Exception as e:
        print(f"Error procesando argumentos: {e}")

    print("--- FIN DEL SCRIPT ---")
else:
    # Esta línea se imprime si este archivo es importado por otro.
    print("El módulo 'Clase_Vivo_Modulos_Sys' ha sido importado correctamente.")
