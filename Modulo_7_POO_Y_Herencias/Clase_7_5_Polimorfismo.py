# --- UNIDAD 7.5: POLIMORFISMO ---
# Descripción: Tratando objetos distintos como si fueran lo mismo.
# Nota Mental:
# - Polimorfismo = "Muchas Formas".
# - La clave es que todos tengan un método con el MISMO NOMBRE (ej: hablar).
# - DRY: Uso herencia para no repetir la lógica base.


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        # ESTO ES UN CONTRATO (Clase Abstracta simulada):
        # Si creo un animal genérico y le digo hablar, da error.
        # Obligo a que las clases hijas (Perro, Gato) escriban su propia versión.
        raise NotImplementedError(
            "¡Error! La subclase debe implementar el método 'hablar'"
        )


class Perro(Animal):
    def hablar(self):
        # Polimorfismo: Misma función que Animal, pero comportamiento de Perro
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hablar(self):
        # Polimorfismo: Misma función que Animal, pero comportamiento de Gato
        return f"{self.nombre} dice: ¡Miau!"


class Vaca(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Muuu!"


# --- FUNCIÓN POLIMÓRFICA ---
# Esta función NO sabe si recibe un perro, un gato o una vaca.
# Solo sabe que recibe "algo que es un Animal" y que sabe "hablar".
def hacer_cantar_al_animal(animal):
    print(f"En el escenario: {animal.hablar()}")


# --- EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Creo una lista heterogénea (mezcla de objetos)
    mis_animales = [Perro("Firulais"), Gato("Michi"), Vaca("Lola"), Perro("Rex")]

    print("\n--- PRUEBA DE POLIMORFISMO ---")
    # 2. El bucle for trata a todos por igual ("animal").
    # Python decide en tiempo real cuál método .hablar() ejecutar.
    for animal in mis_animales:
        # No tengo que preguntar "if es perro... else if es gato..."
        # Simplemente llamo al método y funciona.
        hacer_cantar_al_animal(animal)

    print("\n--- PRUEBA DE CONTRATO (ERROR) ---")
    try:
        # Intento usar la clase base incompleta
        bicho_raro = Animal("Fantasma")
        bicho_raro.hablar()
    except NotImplementedError as e:
        print(f"Error esperado: {e}")
