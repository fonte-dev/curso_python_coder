# --- SETS: LA MAGIA DE LOS CONJUNTOS ---

# Tenemos dos listas de pacientes (con duplicados)
pacientes_ayer = ["Juan", "Ana", "Pedro", "Juan"]
pacientes_hoy = ["Ana", "Maria", "Sofia", "Pedro"]

# 1. Limpiamos duplicados convirtiendo a Set
set_ayer = set(pacientes_ayer)
set_hoy = set(pacientes_hoy)

print("Pacientes únicos ayer:", set_ayer)  # Juan aparece una sola vez

# 2. INTERSECCIÓN (&): ¿Quiénes vinieron AMBOS días?
fieles = set_ayer & set_hoy
print("Pacientes recurrentes:", fieles)  # {'Ana', 'Pedro'}

# 3. DIFERENCIA (-): ¿Quién vino ayer pero NO hoy?
perdidos = set_ayer - set_hoy
print("Pacientes que no volvieron:", perdidos)  # {'Juan'}

# 4. UNIÓN (|): Lista total de pacientes únicos
total_pacientes = set_ayer | set_hoy
print("Total de pacientes únicos:", total_pacientes)
