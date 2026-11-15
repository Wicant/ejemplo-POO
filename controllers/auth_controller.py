from config.settings import Settings
from models.usuario import Usuario
from models.UsuarioDAO import UsuarioDAO
from views.AuthView import AuthView

class AuthController:
    """
    Controlador de Autenticación y Gestión de Usuarios.
    Orquesta el inicio de sesión validando que las credenciales no estén vacías
    ni sean incorrectas, y comparando contraseñas mediante hashes SHA-256.
    """

    def __init__(self):
        self.view = AuthView()

    def iniciar_sesion(self) -> Usuario | None:
        """
        Ejecuta el flujo de inicio de sesión antes de permitir el acceso al menú principal.
        Retorna la instancia de Usuario autenticado o None si agota los intentos.
        """
        UsuarioDAO.inicializar_admin_por_defecto()
        max_intentos = Settings.MAX_LOGIN_ATTEMPTS

        for intento in range(1, max_intentos + 1):
            self.view.mostrar_banner_login(intento, max_intentos)
            credenciales = self.view.solicitar_credenciales()
            username = credenciales["username"]
            clave = credenciales["clave"]

            # 1. Validar que las credenciales ingresadas no estén vacías ni tengan formato inválido
            es_valido, mensaje_validacion = Usuario.validar_credenciales_ingreso(username, clave)
            if not es_valido:
                self.view.mostrar_error(f"Validación fallida: {mensaje_validacion}")
                continue

            # 2. Buscar el usuario en la base de datos y verificar su credencial encriptada
            usuario_bd = UsuarioDAO.obtener_por_username(username)
            if usuario_bd is not None and usuario_bd.verificar_credencial(clave):
                self.view.mostrar_bienvenida(usuario_bd)
                return usuario_bd

            self.view.mostrar_error(
                "Credenciales incorrectas: el usuario no existe o la contraseña no coincide."
            )

        self.view.mostrar_error(
            f"Ha superado el número máximo de intentos permitidos ({max_intentos}). "
            "Acceso bloqueado por seguridad."
        )
        return None

