# --- PRIMERA ENTREGA - CODERHOUSE: "ARMA TU LOGIN" ---
# AUTOR: Fonte Juan Pablo

import time
import os

# --- BASE DE DATOS ---
id_dict = {
    "admin": "admin123",
}

# --- ESTADO GLOBAL ---
active_user = ""
active_password = ""


# --- UTILIDADES ---
def limpiar_pantalla():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")


# --- FUNCIONES GENERALES ---
def user_sign_in():
    """Registra un nuevo usuario en el sistema."""
    print("\n--- REGISTRO DE USUARIO ---")
    user = input("Ingrese su nombre de Usuario: ").strip().lower()
    if user in id_dict:
        print("El usuario ya existe.")
        time.sleep(1)
        return
    password = input("Ingrese una contraseña: ")
    verification = input("Verifique la contraseña: ")
    if password == verification and user not in id_dict:
        save_user(user, password)
        print("Usuario registrado exitosamente.")
    else:
        print("Las contraseñas no coinciden.")
    time.sleep(1)


def user_login():
    """Abre sesión como usuario."""
    global active_user, active_password
    print("\n--- INGRESO DE USUARIO ---")
    while True:
        user_input = input("Ingrese su nombre de usuario: ")
        password_input = input("Ingrese su contraseña: ")
        if user_input == "admin" and password_input == id_dict["admin"]:
            active_user = user_input
            active_password = password_input
            admin_panel()
            return
        elif user_input in id_dict and password_input == id_dict[user_input]:
            active_user = user_input
            active_password = password_input
            user_panel()
            return
        elif user_input not in id_dict:
            print("El usuario no existe.")
            time.sleep(1)
        else:
            print("Contraseña invalida.")
            time.sleep(1)
        if input("¿Salir? (s/n): ").lower() == "s":
            return


def change_password():
    """Permite al usuario logueado cambiar su contraseña."""
    global active_password
    print("\n--- CAMBIO DE CONTRASEÑA ---")
    old_password = input("Ingrese su contraseña actual: ")
    if old_password != active_password:
        print("Contraseña incorrecta.")
        time.sleep(1)
        return
    new_password = input("Ingrese su nueva contraseña: ")
    validation = input("Repita la nueva contraseña: ")
    if new_password == validation:
        if new_password == active_password:
            print("La nueva contraseña es igual a la actual.")
        else:
            active_password = new_password
            id_dict[active_user] = new_password
            print("Cambio de contraseña exitoso.")
    else:
        print("Las contraseñas nuevas no coinciden.")
    time.sleep(1.5)


def delete_account():
    """Elimina la cuenta actual y cierra sesión."""
    global active_user, active_password
    print("\n--- ELIMINAR CUENTA ---")
    confirm = input(f"¿Seguro que desea borrar a '{active_user}'? (s/n): ").lower()
    if confirm == "s":
        password_input = input("Confirme con su contraseña: ")
        if password_input == active_password:
            del id_dict[active_user]
            print("Cuenta eliminada.")
            close_session()
        else:
            print("Contraseña incorrecta. No se ha borrado.")
    time.sleep(1)


def save_user(usuario, contrasena):
    """Guarda el usuario en la base de datos."""
    id_dict[usuario] = contrasena


def close_session():
    global active_user, active_password
    active_user = ""
    active_password = ""


# --- FUNCIONES DE ADMIN ---
def user_list():
    while True:
        print("\n=== Listado de Usuarios ===")
        for key, value in id_dict.items():
            print(f"User: {key} Pass: {value}")
        print("\n1. Eliminar Usuario")
        print("2. Volver al Panel de Admin")

        try:
            op = int(input(">>> Su elección: "))
            if op == 1:
                admin_delete_account()
            elif op == 2:
                return
            else:
                print("Opción no válida")
            time.sleep(1)

        except ValueError:
            print("Error: Debe ingresar un NÚMERO entero.")
            time.sleep(1.5)


def admin_delete_account():
    global active_user, active_password
    while True:
        password_input = input("Ingrese su contraseña: ")
        validation_input = input("Ingrese nuevamente su contraseña para validar: ")
        if password_input == active_password and validation_input == active_password:
            user_to_pop = input("Ingrese el nombre de usuario a eliminar: ")
            if user_to_pop != "admin":
                id_dict.pop(user_to_pop, None)
                print("Cuenta Eliminada con éxito!")
                time.sleep(1)
                return
            else:
                print("La cuenta admin no se puede eliminar")
                time.sleep(1)
                return
        elif password_input != active_password or validation_input != active_password:
            print("Contraseña Invalida")
            time.sleep(1)
            return
        time.sleep(1)


# --- PANELES ---
def user_panel():
    while True:
        if not active_user:
            break
        limpiar_pantalla()
        print(f"\n=== Bienvenido {active_user} ===")
        print("=== Elija la opción deseada ===")
        print("1. Cambiar Contraseña")
        print("2. Borrar Cuenta")
        print("3. Cerrar Sesión")

        try:
            op = int(input(">>> Su elección: "))
            if op == 1:
                change_password()
            elif op == 2:
                delete_account()
            elif op == 3:
                close_session()
                return
            else:
                print("Opción no válida.")
                time.sleep(1.5)

        except ValueError:
            print("Error: Debe ingresar un NÚMERO entero.")
            time.sleep(1.5)

        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Cerrando sistema...")
            break


def admin_panel():
    while True:
        limpiar_pantalla()
        print(f"\n=== Bienvenido {active_user} ===")
        print("=== Elija la opción deseada ===")
        print("1. Cambiar Contraseña")
        print("2. Ver listado de Cuentas")
        print("3. Cerrar Sesión")

        try:
            op = int(input(">>> Su elección: "))

            if op == 1:
                change_password()
            elif op == 2:
                user_list()
            elif op == 3:
                close_session()
                return
            else:
                print("Opción no válida.")
                time.sleep(1)

        except ValueError:
            print("Error: Debe ingresar un NÚMERO entero.")
            time.sleep(1.5)

        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Cerrando sistema...")
            break


# --- ORQUESTADOR ---
def main_menu():
    """Bucle principal de la aplicación."""
    while True:
        limpiar_pantalla()
        print("\n=== Por favor elija la opción deseada ===")
        print("1. Registrar Usuario")
        print("2. Ingresar")
        print("0. Salir")

        try:
            op = int(input(">>> Su elección: "))

            if op == 1:
                user_sign_in()
            elif op == 2:
                user_login()
            elif op == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")
                time.sleep(1.5)

        except ValueError:
            print("Error: Debe ingresar un NÚMERO entero.")
            time.sleep(1.5)

        except KeyboardInterrupt:
            print("\n\nInterrupción detectada. Cerrando sistema...")
            break


# --- ENTRY POINT ---
if __name__ == "__main__":
    main_menu()
