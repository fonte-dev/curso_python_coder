# --- UNIDAD 8.3: ARCHIVOS JSON ---
# Descripción: Guardando datos complejos (Listas y Diccionarios) en texto plano.
# Nota Mental:
# - JSON es el "Inglés" de la programación: Todos los lenguajes lo entienden.
# - dump (sin S) = Vuelca a un ARCHIVO.
# - dumps (con S) = Vuelca a un STRING (cadena de texto en RAM).

import json

# Datos complejos (Lista de Diccionarios)
datos_usuarios = [
    {
        "nombre": "Leonidas",
        "edad": 30,
        "ciudad": "Santiago, Chile",
        "skills": ["Python", "Java"],  # JSON soporta listas adentro de listas
        "activo": False,
    },
    {
        "nombre": "Ricardo",
        "edad": 25,
        "ciudad": "Mendoza, Argentina",
        "skills": ["Django", "Flask"],
        "activo": True,
    },
]


def guardar_configuracion(datos):
    """Escribe los datos en disco."""
    try:
        print("Guardando archivo JSON...")
        # 'w' sobreescribe todo.
        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            # indent=4: Para que se vea con sangría y no todo en una línea.
            # ensure_ascii=False: CLAVE para que guarde tildes y ñ correctamente.
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print("Archivo 'usuarios.json' creado con éxito.")

    except Exception as e:
        print(f"Error al guardar: {e}")


def leer_configuracion():
    """Recupera los datos del disco."""
    try:
        print("\nLeyendo archivo JSON...")
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            # .load() convierte el texto del archivo otra vez en Listas/Diccionarios de Python
            datos_recuperados = json.load(archivo)
            return datos_recuperados

    except FileNotFoundError:
        print("El archivo no existe.")
        return []
    except json.decoder.JSONDecodeError:
        print("El archivo está corrupto o vacío.")
        return []


def prueba_string_en_ram():
    """Ejemplo de dumps (con S) para trabajar en memoria."""
    print("\n--- PRUEBA EN RAM (dumps) ---")
    data_simple = {"id": 1, "status": "ok"}

    # Convierto dict a texto (String)
    texto_json = json.dumps(data_simple)
    print(f"Como texto: {texto_json} (Tipo: {type(texto_json)})")

    # Convierto texto a dict
    dict_python = json.loads(texto_json)
    print(f"Como objeto: {dict_python['status']} (Tipo: {type(dict_python)})")


if __name__ == "__main__":
    # 1. Guardar
    guardar_configuracion(datos_usuarios)

    # 2. Leer
    mis_datos = leer_configuracion()

    if mis_datos:
        print("--- DATOS RECUPERADOS ---")
        for usuario in mis_datos:
            print(f"{usuario['nombre']} ({usuario['ciudad']})")

    # 3. Diferencia dump vs dumps
    prueba_string_en_ram()
