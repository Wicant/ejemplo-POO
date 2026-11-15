import sqlite3
from sqlite3 import Cursor
from config.database import Database
from config.settings import Settings 
from models.usuario import Usuario
from models.Empleado import empleado
from models.EmpleadoDAO import EmpleadoDAO
from datetime import date

class UsuarioDAO:
    """
    Data Access Object para la entidad Usuario.
    Gestiona la persistencia de cuentas y credenciales encriptadas en SQLite
    utilizando consultas parametrizadas (?) contra SQL Injection (Bandit B608).
    """

    @staticmethod
    def crear(usuario: Usuario) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuario (username, password_hash, rut_empleado, rol_admin) VALUES (?, ?, ?, ?)",
                (usuario.username, usuario.password_hash, usuario.rut_empleado, usuario.rol_admin)
            )
            conn.commit()
            usuario.id_usuario = cursor.lastrowid
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error de integridad al crear usuario: {e}")
            return False
        except sqlite3.Error as e:
            print(f"Error al crear usuario en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_por_username(username: str) -> Usuario | None:
        if not isinstance(username, str) or not username.strip():
            return None
        conn = Database().get_connection()
        usuario = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "SELECT username, password_hash, rut_empleado, rol_admin, id_usuario FROM usuario WHERE username = ?",
                (username.strip().lower(),)
            )
            fila = cursor.fetchone()
            if fila:
                usuario = Usuario(
                    username=fila["username"],
                    password_hash=fila["password_hash"],
                    rut_empleado=fila["rut_empleado"],
                    rol_admin=bool(fila["rol_admin"]),
                    id_usuario=fila["id_usuario"]
                )
        except sqlite3.Error as e:
            print(f"Error al consultar usuario: {e}")
        finally:
            conn.close()
        return usuario
    
    @staticmethod
    def obtener_por_id(id_usuario: int) -> Usuario | None:
        conn = Database().get_connection()
        usuario = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "SELECT id_usuario, username, password_hash, rut_empleado, rol_admin FROM usuario WHERE id_usuario = ?",
                (id_usuario,)
            )
            fila = cursor.fetchone()
            if fila:
                usuario = Usuario(
                    username=fila["username"],
                    password_hash=fila["password_hash"],
                    rut_empleado=fila["rut_empleado"],
                    rol_admin=bool(fila["rol_admin"]),
                    id_usuario=fila["id_usuario"]
                )
        except sqlite3.Error as e:
            print(f"Error al obtener usuario por ID: {e}")
        finally:
            conn.close()
        return usuario

    @staticmethod
    def obtener_todos() -> list[Usuario]:
        conn = Database().get_connection()
        usuarios: list[Usuario] = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "SELECT id_usuario, username, password_hash, rut_empleado, rol_admin FROM usuario ORDER BY id_usuario ASC"
            )
            for fila in cursor.fetchall():
                usuarios.append(
                    Usuario(
                        username=fila["username"],
                        password_hash=fila["password_hash"],
                        rut_empleado=fila["rut_empleado"],
                        rol_admin=bool(fila["rol_admin"]),
                        id_usuario=fila["id_usuario"]
                    )
                )
        except sqlite3.Error as e:
            print(f"Error al listar usuarios: {e}")
        finally:
            conn.close()
        return usuarios

    @staticmethod
    def eliminar(id_usuario: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def inicializar_admin_por_defecto(cls) -> None:
        """
        Crea el empleado y el usuario administrador inicial si no existen usuarios.
        """
        usuarios_existentes = cls.obtener_todos()
        print("Usuarios encontrados:", len(usuarios_existentes))

        if not usuarios_existentes:
            datos_admin = [
                Settings.ADMIN_INITIAL_USER,
                Settings.ADMIN_INITIAL_CLAVE,
                Settings.ADMIN_INITIAL_RUT,
                Settings.ADMIN_INITIAL_NOMBRE,
                Settings.ADMIN_INITIAL_DIRECCION,
                Settings.ADMIN_INITIAL_TELEFONO,
                Settings.ADMIN_INITIAL_CORREO
                ]

            if any(not isinstance(dato, str) or not dato.strip() for dato in datos_admin):
                print("Error: Faltan datos para configurar el administrador inicial en el archivo .env.")
                return
            try:
                # 1. Crear el empleado administrador
                admin_empleado = EmpleadoDAO.obtener_empleado_por_rut(
                Settings.ADMIN_INITIAL_RUT
                )
                
                # 2. Si no existe, crearlo
                if admin_empleado is None:
                    admin_empleado = empleado(
                        id_departamento=None,
                        sueldo=0,
                        inicio_contrato=date.today(),
                        rut=Settings.ADMIN_INITIAL_RUT,
                        nombre=Settings.ADMIN_INITIAL_NOMBRE,
                        direccion=Settings.ADMIN_INITIAL_DIRECCION,
                        telefono=Settings.ADMIN_INITIAL_TELEFONO,
                        correo=Settings.ADMIN_INITIAL_CORREO,
                        estado="activo"
                    )

                    if not EmpleadoDAO.agregar_empleado(admin_empleado):
                        print("No se pudo crear el empleado administrador.")
                        return

                # 3. Generar el hash de la contraseña
                hash_inicial = Usuario.encriptar_credencial(
                    Settings.ADMIN_INITIAL_CLAVE
                )
                print("Hash generado:", hash_inicial)

                # 4. Crear el usuario asociado al empleado
                admin_default = Usuario(
                    username=Settings.ADMIN_INITIAL_USER,
                    password_hash=hash_inicial,
                    rut_empleado=admin_empleado.rut,
                    rol_admin=True
                )

                # 5. Guardar el usuario
                if cls.crear(admin_default):
                    print("Administrador inicial creado correctamente.")

            except ValueError as e:
                print(f"Error al inicializar el administrador: {e}")