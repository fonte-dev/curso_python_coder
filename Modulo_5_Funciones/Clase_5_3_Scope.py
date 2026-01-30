# --- CLASE 5.3: VARIABLES LOCALES Y GLOBALES (SCOPE) ---
# Concepto: "Lo que pasa en Las Vegas (función), queda en Las Vegas."

# 1. VARIABLE GLOBAL (Visible para todos)
APP_VERSION = "1.1"  # Constante de configuración
paciente_actual = "Nadie"


def mostrar_configuracion():
    # Puedo LEER variables globales sin problemas
    print(f"Sistema MERITUM v{APP_VERSION}")


# 2. VARIABLE LOCAL (Vida corta)
def calcular_dosis_temp():
    dosis = 500  # Esta variable NACE y MUERE acá adentro.
    print(f"Dosis calculada: {dosis}mg")


# 3. EL PELIGRO DE 'SHADOWING' (Sombra)
def intentar_cambiar_paciente():
    # Al poner el mismo nombre, Python crea una NUEVA variable local.
    # NO estoy tocando la global de arriba.
    paciente_actual = "Juan Perez"
    print(f"Adentro de la función: {paciente_actual}")


# 4. LA BOMBA ATÓMICA: 'GLOBAL' KEYWORD
# Usar esto es mala práctica, pero a veces necesario.
def cambiar_paciente_realmente():
    global paciente_actual  # Aviso: "Voy a tocar la variable de afuera"
    paciente_actual = "Maria Gomez"
    print("Variable global modificada con éxito.")


# --- PRUEBAS ---
print("--- TEST DE SCOPE ---")

# A. Scope Local
calcular_dosis_temp()
# print(dosis) # -> Esto daría ERROR (NameError) porque 'dosis' ya murió.

# B. Test de Shadowing
print(f"\nAntes de intentar cambiar: {paciente_actual}")
intentar_cambiar_paciente()
print(f"Después de intentar cambiar: {paciente_actual} (Sigue igual)")

# C. Test de Global
cambiar_paciente_realmente()
print(f"Después del global: {paciente_actual} (Ahora sí cambió)")
