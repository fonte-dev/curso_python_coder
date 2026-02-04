# --- UNIDAD 7.4: HERENCIA Y HERENCIA MÚLTIPLE ---
# Descripción: Cómo no repetir código usando padres, hijos y el "Problema del Diamante".

# ==========================================
# PARTE 1: HERENCIA SIMPLE
# ==========================================
# Nota Mental: "DRY" (Don't Repeat Yourself). Si todos tienen nombre, creá una clase Padre 'Persona' y que el resto herede.


class Persona:
    def __init__(self, nombre, domicilio):
        self.nombre = nombre
        self.domicilio = domicilio

    def hablar(self, palabras):
        print(f"{self.nombre} dice: {palabras}")


# 'Usuario' HEREDA de 'Persona' (Usuario ES UNA Persona)
class Usuario(Persona):
    def __init__(self, nombre, domicilio, email, password):
        # super() llama al __init__ del Padre (Persona).
        # Es clave para no tener que escribir self.nombre = nombre de nuevo.
        super().__init__(nombre, domicilio)
        self.email = email
        self.password = password

    # SOBREESCRITURA (Overriding):
    # Cambiamos el comportamiento de 'hablar' solo para Usuarios.
    def hablar(self):
        print(f"{self.nombre} dice: >>> Hackeando el sistema... <<<")

    def iniciar_sesion(self):
        pw = input(f"Password para {self.email}: ")
        if pw == self.password:
            print("Login exitoso")
        else:
            print("Acceso denegado")


# 'Empleado' HEREDA de 'Usuario' (que a su vez hereda de Persona)
class Empleado(Usuario):
    def __init__(self, nombre, domicilio, email, password, salario):
        # Llamo al padre directo (Usuario)
        super().__init__(nombre, domicilio, email, password)
        self.salario = salario

    def iniciar_sesion(self):
        # EXTENSIÓN: Primero hago lo que hace el padre...
        super().iniciar_sesion()
        # ...y después agrego funcionalidad extra.
        print("¡A trabajar!")


# ==========================================
# PARTE 2: HERENCIA MÚLTIPLE
# ==========================================
# Nota Mental: Un hijo con DOS padres.
# Tengo que tener cuidado con el orden de los padres por el MRO (Method Resolution Order).


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


class Mamifero(Animal):
    def amamantar(self):
        print(f"{self.nombre} está amamantando.")

    def moverse(self):
        print(f"{self.nombre} camina por el suelo.")


class Volador(Animal):
    def volar(self):
        print(f"{self.nombre} está volando alto.")

    def moverse(self):
        print(f"{self.nombre} se desplaza por el aire.")


# Murcielago hereda de Mamifero Y de Volador
class Murcielago(Mamifero, Volador):
    def __init__(self, nombre, alias):
        # Acá hay que tener cuidado con super() en herencia múltiple.
        # Por simplicidad, llamamos al abuelo directo o usamos super() básico.
        super().__init__(nombre)
        self.alias = alias

    def presentarse(self):
        print(f"Soy {self.nombre}, alias {self.alias}.")


# ==========================================
# EJECUCIÓN Y PRUEBAS
# ==========================================
if __name__ == "__main__":
    print("\n--- 1. PRUEBA DE HERENCIA SIMPLE ---")
    empleado = Empleado("Julian", "Caseros", "juan@dev.com", "1234", 50000)

    # Heredado del Abuelo (Persona)
    empleado.hablar()  # Nota: Usa el hablar() de Usuario porque lo sobreescribió

    # Heredado del Padre (Usuario) + Extensión
    empleado.iniciar_sesion()

    print("\n--- 2. PRUEBA DE HERENCIA MÚLTIPLE ---")
    batman = Murcielago("Bruce", "El Caballero de la Noche")

    batman.amamantar()  # Viene de Mamifero
    batman.volar()  # Viene de Volador

    print("\n--- 3. EL CONFLICTO (MRO) ---")
    # Ambos padres tienen el método 'moverse'.
    # Usa el del PRIMER padre que pusiste en el paréntesis: class Murcielago(Mamifero, Volador)
    batman.moverse()

    print("\n--- 4. MRO (Method Resolution Order) ---")
    print("Orden de búsqueda de métodos:")
    # Esto te muestra el mapa: Murcielago -> Mamifero -> Volador -> Animal -> Object
    print(Murcielago.mro())
