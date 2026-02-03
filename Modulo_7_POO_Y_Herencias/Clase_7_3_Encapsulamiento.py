# --- UNIDAD 7.3: ENCAPSULAMIENTO ---
# Descripción: Cómo proteger mis variables para que no hagan desastres desde afuera.
# Nota Mental:
# - Público (sin guion): "Pasá, servite lo que quieras".
# - Protegido (_un_guion): "Por favor no toques, pero si querés, podés" (Convención).
# - Privado (__dos_guiones): "PROHIBIDO EL PASO. Zona Restringida" (Name Mangling).


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Atributo Público: Cualquiera lo ve y lo cambia
        self.titular = titular

        # Atributo Protegido (_): Es una señal de "No tocar", pero Python te deja.
        self._tipo_cuenta = "Caja de Ahorro"

        # Atributo Privado (__): Python le cambia el nombre para ocultarlo.
        # Solo se puede tocar desde ADENTRO de los métodos de esta clase.
        self.__saldo = saldo_inicial

    # --- GETTER (La forma correcta de LEER un privado) ---
    def obtener_saldo(self):
        # Acá podría pedir password o validar usuario antes de devolver el dato
        return self.__saldo

    # --- SETTER (La forma correcta de ESCRIBIR un privado) ---
    def depositar(self, monto):
        # VALIDACIÓN: Esta es la gracia del encapsulamiento.
        # Evito que alguien ponga saldos negativos o rompa la lógica.
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Error: No podés depositar montos negativos o cero.")

    # --- MÉTODO PRIVADO (Solo para uso interno) ---
    def __auditoria_interna(self):
        print(f"AUDITANDO: El saldo real es {self.__saldo}")

    # Método público que usa el privado
    def realizar_balance_mensual(self):
        print("Iniciando balance...")
        self.__auditoria_interna()  # Desde acá ADENTRO sí puedo llamar al privado


# --- PRUEBAS DEL SISTEMA ---
if __name__ == "__main__":
    mi_cuenta = CuentaBancaria("Juan", 1000)

    print("\n--- 1. ACCESO PÚBLICO ---")
    print(f"Titular: {mi_cuenta.titular}")  # Funciona directo

    print("\n--- 2. ACCESO PROTEGIDO (_) ---")
    # Python me deja leerlo, pero mi editor me marca una advertencia (amarillo)
    print(f"Tipo: {mi_cuenta._tipo_cuenta}")

    print("\n--- 3. INTENTO DE ACCESO PRIVADO (__) ---")
    try:
        # Esto va a fallar. Python dice "No sé qué es __saldo".
        print(mi_cuenta.__saldo)
    except AttributeError as e:
        print(f"BLOQUEADO: {e}")

    print("\n--- 4. LA FORMA CORRECTA (Getters y Setters) ---")
    mi_cuenta.depositar(500)  # Paso por la validación
    mi_cuenta.depositar(-200)  # Intento romperlo (la validación me frena)
    print(f"Saldo final consultado: ${mi_cuenta.obtener_saldo()}")

    print("\n--- 5. CURIOSIDAD HACKER (Name Mangling) ---")
    # Python no es "estricto" como Java. En realidad, solo le cambia el nombre.
    # Si sabés el truco, podés entrar igual (pero no debés).
    # El nombre secreto es: _NombreClase__nombreAtributo
    print(f"Accediendo a la fuerza bruta: {mi_cuenta._CuentaBancaria__saldo}")
