# --- SISTEMA DE ALERTA: CRISIS PSIQUIÁTRICA ---

paciente = "Paciente L"
nivel_excitacion = int(input("Nivel de excitación motriz (1-10): "))
riesgo_terceros = input("¿Hay riesgo para sí o terceros? (si/no): ")

# LÓGICA DE INTERVENCIÓN AT
# Prioridad 1: Crisis Aguda (Llamar a Emergencias/Psiquiatra)
# Prioridad 2: Desregulación (Contención verbal/ambiental)
# Prioridad 3: Estabilidad (Rutina habitual)

if riesgo_terceros == "si" or nivel_excitacion >= 9:
    print(f"🚨 ALERTA ROJA: {paciente} en crisis aguda.")
    print("ACCIÓN: Protocolo de contención y llamar a Psiquiatra/Familia.")

elif nivel_excitacion >= 6:
    print(f"⚠️ ALERTA AMARILLA: {paciente} desregulado.")
    print(
        "ACCIÓN: Intentar contención verbal, reducir estímulos, ofrecer PRN si está indicado."
    )

else:
    print(f"✅ ESTADO VERDE: {paciente} estable.")
    print("ACCIÓN: Continuar cronograma de actividades.")
