from models.usuario import Usuario

class AuthView:
    """
    Vista de consola para el Inicio de Sesión y la Gestión de Usuarios con Credenciales Encriptadas.
    """

    @staticmethod
    def mostrar_banner_login(intento_actual: int, max_intentos: int) -> None:
        print("\n" + "=" * 55)
        print("          ECOTECH - INICIO DE SESIÓN")
        print("=" * 55)
        print(f"Intento {intento_actual} de {max_intentos}")
        print("-" * 55)

    @staticmethod
    def solicitar_credenciales() -> dict:
        username = input("Usuario    : ").strip()
        clave = input("Contraseña : ").strip()

        return {
            "username": username,
            "clave": clave
        }

    @staticmethod
    def mostrar_bienvenida(usuario: Usuario) -> None:
        print("\n" + "*" * 55)
        print(f"  ¡Bienvenido/a, {usuario.username}!")
        print(f"  Rol: {'Administrador' if usuario.rol_admin else 'Usuario'}")
        print("*" * 55)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[AUTENTICACIÓN] {mensaje}")

    @staticmethod
    def mostrar_error(error: str) -> None:
        print(f"\n[ERROR DE AUTENTICACIÓN] {error}")