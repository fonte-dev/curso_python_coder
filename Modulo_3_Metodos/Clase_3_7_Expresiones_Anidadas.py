# --- CLASE 3.7: PRECEDENCIA Y LÓGICA ---

# 1. Pruebas matemáticas (PAPOMUDAS)
# Paréntesis -> Potencia -> Multi/Div -> Suma/Resta

x = 5 + 2 * 3  # 5 + 6 = 11
y = (5 + 2) * 3  # 7 * 3 = 21

print(f"Sin paréntesis: {x}")
print(f"Con paréntesis: {y}")

# OJO con esto: Potencia gana al signo menos
# El formateador automático odia esto, por eso lo apagamos acá:
# fmt: off
prueba_potencia = -3**2  # Hace -(3^2) -> -9
# fmt: on
prueba_potencia_fix = (-3) ** 2  # Hace (-3)^2 -> 9
print(f"Potencia sin cubrir: {prueba_potencia}")
print(f"Potencia cubierta: {prueba_potencia_fix}")


# 2. Lógica Booleana (Test para Project MAT)
# Caso: Internar paciente si (Tiene Riesgo O Tiene Síntomas Graves) Y (No tiene familia)

riesgo_inminente = False
sintomas_graves = True
tiene_familia = True

# Prueba SIN paréntesis (Peligroso)
# Python evalúa: sintomas AND not tiene_familia primero.
decision_mala = riesgo_inminente or sintomas_graves and not tiene_familia

# Prueba CON paréntesis (Lo que quiero)
decision_buena = (riesgo_inminente or sintomas_graves) and not tiene_familia

print(f"Decision mala (lógica rota): {decision_mala}")
print(f"Decision buena (segura): {decision_buena}")

# Nota: Siempre usar paréntesis para separar los OR de los AND
