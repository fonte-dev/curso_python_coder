# --- CLASE EN VIVO: POO, HERENCIA Y DIAGRAMAS ---
# Descripción: Resumen de actividades prácticas.
# Nota Mental:
# 1. '__str__' es para que el objeto se imprima lindo en consola.
# 2. Herencia Múltiple = Un hijo con habilidades de dos padres distintos.


# ==========================================
# ACTIVIDAD 1: CLASE ALUMNO
# ==========================================
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # MÉTODO DE INSTANCIA
    def imprimir(self):
        print(f"Ficha: {self.nombre} tiene un {self.nota}")

    # MÉTODO __str__
    # Reemplaza lo que sale cuando hago print(objeto)
    def __str__(self):
        return f"{self.nombre} (Nota: {self.nota})"

    # LÓGICA DE NEGOCIO
    def resultado(self):
        if self.nota < 5:
            print(f"{self.nombre} ha DESAPROBADO.")
        else:
            print(f"{self.nombre} ha APROBADO.")


# ==========================================
# ACTIVIDAD 2: HERENCIA MÚLTIPLE (Mamífero + Marino = Cetáceo)
# ==========================================


class Mamifero:
    def amamantar(self):
        print("Amamantando a las crías...")


class AnimalMarino:
    def nadar(self):
        print("Nadando bajo el agua...")


# HERENCIA MÚLTIPLE: Cetaceo hereda de los dos de arriba
class Cetaceo(Mamifero, AnimalMarino):
    def __init__(self, especie):
        self.especie = especie

    def presentarse(self):
        print(f"Soy una {self.especie}, soy mamífero y vivo en el mar.")


# ==========================================
# EJECUCIÓN (MAIN)
# ==========================================
if __name__ == "__main__":

    print("\n--- 1. PROBANDO CLASE ALUMNO ---")
    # Instancio dos objetos (Requisito de la actividad)
    alumno1 = Alumno("Juan", 8)
    alumno2 = Alumno("Pepito", 4)

    # Pruebo el método __str__
    print(f"Objeto 1: {alumno1}")  # Gracias al __str__ se lee bien

    # Pruebo la lógica de aprobado/desaprobado
    alumno1.resultado()
    alumno2.resultado()

    print("\n--- 2. PROBANDO HERENCIA MÚLTIPLE ---")
    ballena = Cetaceo("Ballena Azul")
    ballena.presentarse()

    # Uso métodos de AMBOS padres
    ballena.amamantar()  # Viene de Mamifero
    ballena.nadar()  # Viene de AnimalMarino
