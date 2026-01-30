# --- PROJECT MERITUM: GESTIÓN DE PACIENTE ---

# 1. Creación del Perfil (Simulando lo que llega de un formulario web)
paciente = {
    "id": 504,
    "nombre": "Matias",
    "apellido": "Perez",
    "edad": 33,
    "obra_social": "OSDE 210",
    "historial_activo": True,
}

print("--- PERFIL INICIAL ---")
print(paciente)

# 2. LECTURA (El médico abre la ficha)
# Usamos f-strings para leer las claves
print(f"\nPaciente: {paciente['nombre']} {paciente['apellido']}")
print(f"Cobertura: {paciente['obra_social']}")

# 3. UPDATE (El paciente vino a consulta y agregamos datos)
# Llegan datos nuevos del sistema de guardia
datos_guardia = {
    "diagnostico_actual": "Gripe A",
    "temperatura": 38.5,
    "medico_tratante": "Dr. House",
}

# Fusionamos la info nueva en el perfil existente
paciente.update(datos_guardia)

print("\n--- PERFIL ACTUALIZADO (POST-CONSULTA) ---")
# Fíjate cómo ahora el diccionario tiene más datos
print(paciente)

# 4. MODIFICACIÓN (Corregimos un error de carga)
# El paciente cumplió años o cargaron mal la edad
paciente["edad"] = 34

# 5. BORRADO (Limpieza de datos temporales)
# Ya no necesitamos saber la temperatura en el perfil general
del paciente["temperatura"]

print("\n--- FICHA FINAL PARA GUARDAR ---")
print(paciente)
