# --- UNIDAD 6.3: INTRODUCCIÓN A POO ---
# Descripción: Comparación entre Paradigma Estructurado vs Orientado a Objetos.
# Ejemplo: Sistema de Biblioteca


def enfoque_estructurado():
    print("\n--- 1. ENFOQUE ESTRUCTURADO (El viejo método) ---")
    print("Acá los datos (variables) y las acciones (funciones) están separados.")
    print("Es difícil mantener el orden si el sistema crece.")

    # Datos sueltos (Diccionarios)
    libro_1 = {"titulo": "1984", "autor": "Orwell", "disponible": True}
    libro_2 = {"titulo": "El Principito", "autor": "Saint-Exupéry", "disponible": True}

    # Función suelta que recibe datos
    def prestar_libro(libro):
        if libro["disponible"]:
            libro["disponible"] = False
            print(f"Prestaste: {libro['titulo']}")
        else:
            print(f"{libro['titulo']} ya está prestado.")

    # Uso
    prestar_libro(libro_1)
    # prestar_libro(libro_1) # Si descomento, dirá que ya está prestado.


def enfoque_orientado_a_objetos():
    print("\n--- 2. ENFOQUE POO (El nuevo método) ---")
    print("Acá creamos un 'Molde' (Clase). Datos y acciones viven juntos.")

    # DEFINICIÓN DE LA CLASE (El Molde)
    class Libro:
        # El Constructor (__init__): Se ejecuta al crear el objeto
        def __init__(self, titulo, autor):
            # Atributos (Datos)
            self.titulo = titulo
            self.autor = autor
            self.disponible = True  # Por defecto, nace disponible

        # Métodos (Acciones)
        def prestar(self):
            if self.disponible:
                self.disponible = False
                print(f"Prestaste: {self.titulo} (Autor: {self.autor})")
            else:
                print(f"{self.titulo} no está disponible.")

        def devolver(self):
            self.disponible = True
            print(f"🔄 Devolviste: {self.titulo}")

    # INSTANCIACIÓN (Crear Objetos / Galletas)
    mi_libro = Libro("Cien Años de Soledad", "García Márquez")
    otro_libro = Libro("Fahrenheit 451", "Bradbury")

    # Uso (Notación de punto)
    mi_libro.prestar()  # El objeto sabe prestarse a sí mismo
    mi_libro.prestar()  # Intento prestarlo de nuevo
    mi_libro.devolver()  # Lo devuelvo

    # El otro libro es totalmente independiente
    otro_libro.prestar()


# --- ORQUESTADOR ---
if __name__ == "__main__":
    enfoque_estructurado()
    enfoque_orientado_a_objetos()
