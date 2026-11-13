import hashlib
import hmac
import re

class Usuario:
    """
    Modelo de Dominio para la entidad Usuario.
    Implementa:
    - Encriptación irreversible de credenciales mediante SHA-256 (hashlib).
    - Comparación segura en tiempo constante (hmac.compare_digest).
    - Validación defensiva con @property y @setter evitando valores vacíos o incorrectos.
    """

    def __init__(
        self,
        username: str,
        password_hash: str,
        rut_empleado: str,
        rol_admin: bool = False,
        id_usuario: int | None = None
    ):
        self.id_usuario = id_usuario
        self.username = username
        self.rut_empleado = rut_empleado
        self.password_hash = password_hash
        self.rol_admin = rol_admin

    @property
    def id_usuario(self) -> int | None:
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor: int | None) -> None:
        if valor is not None and (not isinstance(valor, int) or valor <= 0):
            raise ValueError("El ID debe ser un entero positivo.")
        self._id_usuario = valor
    
    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre de usuario no puede estar vacío.")
        limpio = valor.strip().lower()
        if len(limpio) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
        if not re.match(r"^[a-zA-Z0-9_.-]+$", limpio):
            raise ValueError("El nombre de usuario solo puede contener letras, números, puntos, guiones o guiones bajos.")
        self._username = limpio

    @property
    def rut_empleado(self) -> str:
        return self._rut_empleado

    @rut_empleado.setter
    def rut_empleado(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El RUT del empleado no puede estar vacío.")
        self._rut_empleado = valor.strip()
    
    @property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El hash de la contraseña no puede estar vacío.")
        limpio = valor.strip().lower()
        if len(limpio) != 64 or not re.match(r"^[a-f0-9]{64}$", limpio):
            raise ValueError("La credencial debe almacenarse como un hash SHA-256 válido de 64 caracteres hexadecimales.")
        self._password_hash = limpio

    @property
    def rol_admin(self) -> bool:
        return self._rol_admin
    @rol_admin.setter
    def rol_admin(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise ValueError("El rol de administrador debe ser True o False.")
        self._rol_admin = valor

    @staticmethod
    def encriptar_credencial(clave_plana: str) -> str:
        """
        Valida que la contraseña en texto plano no esté vacía ni sea demasiado corta,
        y retorna su representación encriptada mediante el algoritmo criptográfico SHA-256.
        """
        if not isinstance(clave_plana, str) or not clave_plana.strip():
            raise ValueError("La contraseña no puede estar vacía ni contener solo espacios.")
        clave_limpia = clave_plana.strip()
        if len(clave_limpia) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres.")
        return hashlib.sha256(clave_limpia.encode("utf-8")).hexdigest()

    @staticmethod
    def validar_credenciales_ingreso(username: str, clave_plana: str) -> tuple[bool, str]:
        """
        Valida las credenciales ingresadas por el usuario antes de procesar el login,
        evitando valores vacíos o con formato incorrecto.
        """
        if not isinstance(username, str) or not username.strip():
            return (False, "El campo 'Usuario' no puede estar vacío.")
        if not isinstance(clave_plana, str) or not clave_plana.strip():
            return (False, "El campo 'Contraseña' no puede estar vacío.")

        user_limpio = username.strip()
        clave_limpia = clave_plana.strip()

        if len(user_limpio) < 3:
            return (False, "El nombre de usuario ingresado es inválido (mínimo 3 caracteres).")
        if not re.match(r"^[a-zA-Z0-9_.-]+$", user_limpio):
            return (False, "El nombre de usuario contiene caracteres no permitidos.")
        if len(clave_limpia) < 4:
            return (False, "La contraseña ingresada es inválida (mínimo 4 caracteres).")

        return (True, "Formato de credenciales válido.")

    def verificar_credencial(self, clave_ingresada: str) -> bool:
        """
        Compara la contraseña ingresada (en texto plano) con el hash encriptado del usuario
        utilizando comparación en tiempo constante para mitigar ataques de temporización.
        """
        if not isinstance(clave_ingresada, str) or not clave_ingresada.strip():
            return False
        try:
            hash_ingresado = self.encriptar_credencial(clave_ingresada)
            return hmac.compare_digest(self._password_hash, hash_ingresado)
        except ValueError:
            return False

    def __str__(self) -> str:
        id_str = self.id_usuario if self.id_usuario is not None else "Nuevo"
        hash_resumen = f"{self.password_hash[:12]}...{self.password_hash[-6:]}"
        return (
            f"Usuario [ID: {id_str}] | "
            f"Login: {self.username} | "
            f"RUT empleado: {self.rut_empleado} | "
            f"Administrador: {self.rol_admin} | "
            f"Hash SHA-256: {hash_resumen}"
        )