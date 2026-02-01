# --- UNIDAD 7.2: POO - ATRIBUTOS Y MÉTODOS ---
# Descripción: Aprendiendo la diferencia entre métodos de Instancia, Clase y Estáticos.
# Nota Mental:
# - Self = Yo (el objeto específico).
# - Cls = La Fábrica (la clase entera).
# - Static = Una herramienta suelta (no sabe quién soy).


class Persona:
    # ATRIBUTO DE CLASE
    # Esto es compartido por TODOS. Si lo cambio, cambia para todos.
    que_soy = "Una sustancia individual de naturaleza racional"

    def __init__(self, nombre, domicilio, edad=None) -> None:
        # ATRIBUTOS DE INSTANCIA
        # Estos son únicos de CADA objeto.
        self.nombre = nombre
        self.domicilio = domicilio
        self.edad = edad
        # Inicializo una lista vacía para guardar historial (memoria del objeto)
        self.mis_palabras = []

    # --- 1. MÉTODOS DE INSTANCIA (Llevan 'self') ---
    # Necesitan un objeto creado para funcionar.

    def presentarme(self):
        # Accedo a 'Persona.que_soy' (clase) y a 'self.nombre' (instancia)
        print(
            f"Soy {Persona.que_soy}, me llamo {self.nombre}, vivo en {self.domicilio}."
        )
        if self.edad:
            print(f"Tengo {self.edad} años.")

    def hablar(self, palabras):
        print(f"{self.nombre} dice: '{palabras}'")
        # Guardo en la memoria de ESTE objeto
        self.mis_palabras.append(palabras)

    def ver_historial(self):
        print(f"\n--- Historial de {self.nombre} ---")
        if self.mis_palabras:
            for i, frase in enumerate(self.mis_palabras, 1):
                print(f"{i}. {frase}")
        else:
            print("No ha dicho nada aún.")

    # --- 2. MÉTODOS DE CLASE (Llevan 'cls' + @classmethod) ---
    # No necesitan una instancia. Hablan por la 'fábrica'.

    @classmethod
    def obtener_especie(cls):
        # Nota: Uso 'cls' en vez de 'Persona'
        return "Homo Sapiens"

    @classmethod
    def cambiar_definicion(cls, nueva_def):
        # OJO: Si cambio esto, cambia para TODOS los objetos creados
        cls.que_soy = nueva_def

    # --- 3. MÉTODOS ESTÁTICOS (Sin self/cls + @staticmethod) ---
    # Son herramientas auxiliares. No saben quién es 'Bach' ni la clase 'Persona'.

    @staticmethod
    def es_mayor_de_edad(edad_a_verificar):
        # Simplemente una calculadora de lógica.
        # No puedo usar self.nombre ni cls.que_soy acá dentro.
        return edad_a_verificar >= 18


# --- EJECUCIÓN DEL CÓDIGO ---
if __name__ == "__main__":

    print("\n--- 1. INSTANCIACIÓN ---")
    bach = Persona(nombre="Bach", domicilio="Alemania", edad=65)
    mozart = Persona("Mozart", "Austria", 35)

    print("\n--- 2. USO DE MÉTODOS DE INSTANCIA ---")
    bach.presentarme()
    bach.hablar("La música es el lenguaje del alma.")
    bach.hablar("He compuesto mucha música sacra.")
    bach.ver_historial()

    # Mozart tiene su propio historial separado
    mozart.ver_historial()  # Debería estar vacío

    print("\n--- 3. USO DE MÉTODOS DE CLASE Y ESTÁTICOS ---")
    # Los puedo llamar desde la CLASE, sin usar a Bach o Mozart
    print(f"Especie: {Persona.obtener_especie()}")

    # Probando el estático (Validación)
    edad_test = 15
    es_adulto = Persona.es_mayor_de_edad(edad_test)
    print(f"¿Alguien de {edad_test} es mayor?: {es_adulto}")

    print("\n--- 4. CAMBIO GLOBAL (Cuidado con esto) ---")
    # Cambio el atributo de clase
    Persona.cambiar_definicion("Un músico excelente")

    # Verifico que cambió para todos
    print(f"Bach ahora es: {bach.que_soy}")  # Un músico excelente
    print(f"Mozart ahora es: {mozart.que_soy}")  # Un músico excelente
