# --- CLASE 5.4: RETORNO DE VALORES (RETURN) ---
# Diferencia clave:
# PRINT: Muestra algo en pantalla (para el humano). El programa NO puede usar ese dato.
# RETURN: Devuelve el dato al programa (para la computadora). El dato se puede guardar y reusar.


# 1. RETURN SIMPLE
def sumar_precios(precio1, precio2):
    # Proceso el dato
    total = precio1 + precio2
    # Lo entrego (Devuelvo la "caja" con el valor)
    return total


# 2. RETURN MÚLTIPLE (Tuplas)
# Python permite devolver varias cosas separadas por coma.
def analizar_paciente(nombre, edad):
    # Lógica de negocio simulada
    es_mayor = edad >= 18
    grupo_riesgo = edad > 60

    # Devuelvo TRES cosas a la vez
    return nombre.title(), es_mayor, grupo_riesgo


# 3. EARLY RETURN (Retorno Temprano)
# El return MATA a la función. Lo que haya abajo no se ejecuta.
# Sirve para salir rápido si hay un error.
def dividir_seguro(a, b):
    if b == 0:
        return None  # Corto acá. No sigo.

    return a / b


# --- ZONA DE PRUEBAS ---
print("--- PRUEBAS DE RETURN ---")

# A. Usando el return simple
resultado = sumar_precios(1500, 300)
# Ahora 'resultado' tiene el valor 1800. Puedo usarlo para otra cosa.
con_iva = resultado * 1.21
print(f"Total con IVA: ${con_iva}")

# B. Usando el return múltiple (Desempaquetado)
# Capturo los 3 valores en 3 variables distintas en una sola linea
nombre_f, es_adulto, es_riesgo = analizar_paciente("juan perez", 65)

print(f"\nReporte de {nombre_f}:")
print(f"- Adulto: {es_adulto}")
print(f"- Riesgo: {es_riesgo}")


# C. PROJECT MAT: Validaciones
def limpiar_texto(texto_sucio):
    """Recibe texto con espacios y minúsculas, devuelve texto limpio."""
    if not texto_sucio:  # Si esta vacio
        return "Desconocido"
    return texto_sucio.strip().title()


# Simulando input de usuario sucio
paciente_ingresado = "   maria gomez   "
paciente_limpio = limpiar_texto(paciente_ingresado)
print(f"\nPaciente guardado como: '{paciente_limpio}'")
