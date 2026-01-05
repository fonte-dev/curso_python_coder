# --- CLASE 5.2: BUENAS PRÁCTICAS DE NOMBRES ---
# Regla: Usar snake_case (minusculas_con_guiones).
# Regla de Semántica: VERBO + SUSTANTIVO (Acción + Objeto).


# --- EJEMPLOS INCORRECTOS (BAD SMELL) ---
# 1. Nombres crípticos (Ahorrar letras sale caro después)
def calc(p):
    pass


# 2. CamelCase (Esto es para Java o Javascript, no Python)
def CalcularDosis():
    pass


# 3. Ambiguedad (¿Es una variable o una función?)
def paciente():
    pass


# --- EJEMPLOS CORRECTOS (PROJECT MAT) ---


# 1. Acciones claras
def calcular_dosis_diaria(peso_paciente):
    """Calcula mg de medicación según peso."""
    pass


def registrar_evolucion(paciente, texto):
    """Guarda una nota nueva en el historial."""
    pass


def validar_usuario_sistema(password):
    """Devuelve True si la contraseña es correcta."""
    pass


# 2. Funciones Booleanas (Suelen empezar con 'es', 'tiene', 'esta')
def es_paciente_de_riesgo(diagnostico):
    return True  # o False


# 3. Getters (Obtener datos)
def obtener_historial_clinico(id_paciente):
    pass
