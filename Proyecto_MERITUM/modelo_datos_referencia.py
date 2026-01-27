# PROJECT MERITUM - ESTRUCTURA DE DATOS V1.0

# Perfil de Paciente (Diccionario Maestro)
paciente_A = {
    "id": "MAT-001",
    "datos_personales": {"nombre": "A... (Preservado)", "edad": 45, "barrio": "Lanus"},
    "clinica": {
        "diagnostico_principal": "Trastorno Bipolar I",
        "obra_social": "OSDE",
        "afiliado_num": "12345678",
    },
    "profesionales": ("Dr. Psiquiatra A", "Lic. Psicologo A"),
    "esquema_medicacion": [
        {"droga": "Litio", "dosis": "300mg", "frecuencia": "8hs"},
        {"droga": "Quetiapina", "dosis": "25mg", "frecuencia": "Noche"},
    ],
    "historial_visitas": [
        {"fecha": "20/12", "at": "Juan Pablo", "nota": "Paciente estable"},
        {
            "fecha": "21/12",
            "at": "Ignacio",
            "nota": "Buena adherencia a la medicación.",
        },
    ],
    "plan_tratamiento": ["Bajar de peso", "Control de peso mensual"],
}
paciente_B = {
    "id": "MAT-002",
    "datos_personales": {"nombre": "B... (Preservado)", "edad": 54, "barrio": "Tigre"},
    "clinica": {
        "diagnostico_principal": "Esquizofrenia",
        "obra_social": "OSDEPyM",
        "afiliado_num": "23456781",
    },
    "profesionales": ("Dr. Psiquiatra B", "Lic. Psicologo B"),
    "esquema_medicacion": [
        {"droga": "Quetiapina", "dosis": "25mg", "frecuencia": "Mañana"},
        {"droga": "Quetiapina", "dosis": "50mg", "frecuencia": "Noche"},
    ],
    "alertas": ({"Riesgo de Fuga", "Alergia Penicilina"}),
    "historial_visitas": [
        {"fecha": "19/12", "at": "Juan Pablo", "nota": "Paciente estable con mejora"},
        {"fecha": "19/12", "at": "Julian", "nota": "Paciente refiere ansiedad."},
    ],
    "plan_tratamiento": ["Evitar gluten", "Terapia Cognitivo Conductual semanal"],
}

paciente_C = {
    "id": "MAT-003",
    "datos_personales": {"nombre": "C... (Preservado)", "edad": 33, "barrio": "Moreno"},
    "clinica": {
        "diagnostico_principal": "TEA, Psicosis",
        "obra_social": "IOMA",
        "afiliado_num": "34567812",
    },
    "profesionales": ("Dr. Psiquiatra A", "Lic. Psicologo C"),
    "esquema_medicacion": [
        {"droga": "Quetiapina", "dosis": "25mg", "frecuencia": "Mañana"},
        {"droga": "Clonazepam", "dosis": "0.5mg", "horario": "Noche"},
    ],
    "historial_visitas": [
        {"fecha": "18/12", "at": "Lucas", "nota": "Paciente estable"},
        {"fecha": "23/12", "at": "Julian", "nota": "Crisis detectada"},
    ],
    "plan_tratamiento": ["Bajar de peso", "Caminatas diarias"],
}

print(
    f"Paciente cargado: {paciente_B['datos_personales']['nombre']}, {paciente_B['datos_personales']['edad']} años"
)
print(f"Diagnóstico: {paciente_B['clinica']['diagnostico_principal']}")
print(f"Profesionales a cargo: {paciente_B['profesionales']}")
print(f"Último AT a cargo: {paciente_B['historial_visitas'][-1]['at']}")
print(f"Medicación: {paciente_B['esquema_medicacion']}")
print(f"Historial de Visitas del AT: {paciente_B['historial_visitas']}")
