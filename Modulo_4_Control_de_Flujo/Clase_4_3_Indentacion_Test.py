# --- CLASE 4.3: NOTAS SOBRE INDENTACIÓN ---
# Python no usa llaves {} como otros lenguajes. Usa espacios.
# Regla de oro: 4 espacios por nivel.

# 1. Estructura de Bloques
if True:
    print("Nivel 1: Entré al bloque")
    if True:
        # Cada nivel suma 4 espacios más a la izquierda
        print("    Nivel 2: Estoy anidado")

print("Nivel 0: Volví al flujo principal")


# 2. El engaño de la tecla TAB
# Cuando aprieto TAB, VS Code pone 4 espacios automáticamente.
# NOTA: Nunca usar el caracter de tabulación real (\t), Python 3 lo odia.
if True:
    print("    Aca hay 4 espacios, aunque haya apretado Tab una vez.")


# 3. ERRORES TÍPICOS (Descomentar para probar)

# ERROR A: Indentar sin razón (El "Unexpected indent")
# print("Linea normal")
#    print("Linea indentada mal") # -> Esto rompe porque no hay un if/for antes.

# ERROR B: Mezclar Tabs y Espacios (El "TabError")
# if True:
#     print("Indentado con espacios")
# 	  print("Indentado con Tab real") # -> Python explota acá si mezclo.
