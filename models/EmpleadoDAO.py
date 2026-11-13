from sqlite3 import Cursor
from datetime import date
from typing import Optional

from config.database import Database
from models.Empleado import empleado


class EmpleadoDAO:
    """
    Data Access Object para la entidad Paciente.
    Maneja todas las operaciones CRUD en la base de datos.
    """
    @staticmethod
    def agregar_empleado(empleado: empleado) -> bool:
        """
        Agrega un nuevo empleado a la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO empleado (rut, nombre, direccion, telefono, correo,id_departamento, sueldo, inicio_contrato, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, 
                (
                    empleado.rut, empleado.nombre, empleado.direccion, empleado.telefono,
                    empleado.correo, empleado.id_departamento, 
                    empleado.sueldo, empleado.inicio_contrato, empleado.estado
                )
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar empleado en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def crear_empleado(fila) -> empleado:
        inicio_contrato = fila["inicio_contrato"]
        if isinstance(inicio_contrato, str):
            inicio_contrato = date.fromisoformat(inicio_contrato)

        return empleado(
        fila["id_departamento"],
        fila["sueldo"],
        inicio_contrato,
        fila["rut"],
        fila["nombre"],
        fila["direccion"],
        fila["telefono"],
        fila["correo"],
        fila["estado"]
        )

    @staticmethod
    def obtener_todos_empleados() -> list[empleado]:
        """
        Obtiene todos los empleados de la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                SELECT rut, nombre, direccion, telefono, correo,
                       id_departamento, sueldo, inicio_contrato , estado
                FROM empleado
                ORDER BY nombre
                """
            )
            return [EmpleadoDAO.crear_empleado(fila) for fila in cursor.fetchall()]
        finally:
            conn.close()

    @staticmethod
    def obtener_todos_empleado_estado(estado: str) -> list[empleado]:
        """
        Obtiene todos los empleados de la base de datos por su estado.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                SELECT rut, nombre, direccion, telefono, correo,
                    id_departamento, sueldo, inicio_contrato, estado
                    FROM empleado
                    WHERE estado = ?
                    ORDER BY nombre
                """,
                (estado,)
            )
            return [EmpleadoDAO.crear_empleado(fila) for fila in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener empleados por estado de BD: {e}")
            return []
        finally:
            conn.close()

    
    @staticmethod
    def obtener_empleado_por_rut(rut: str) -> Optional[empleado]:
        """
        Obtiene un empleado de la base de datos por su RUT.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                SELECT rut, nombre, direccion, telefono, correo, 
                       id_departamento, sueldo, inicio_contrato, estado
                FROM empleado
                WHERE rut = ?
                """,
                (rut,),
            )
            fila = cursor.fetchone()
            return EmpleadoDAO.crear_empleado(fila) if fila else None
        finally:
            conn.close()

    @staticmethod
    def actualizar_empleado(empleado: empleado) -> bool:
        """
        Actualiza los datos de un empleado en la base de datos.
        """
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE empleado
                SET nombre = ?, direccion = ?, telefono = ?, correo = ?,
                    id_departamento = ?, sueldo = ?, inicio_contrato = ?, estado = ?
                WHERE rut = ?
                """,
                (
                    empleado.nombre,
                    empleado.direccion,
                    empleado.telefono,
                    empleado.correo,
                    empleado.id_departamento,
                    empleado.sueldo,
                    empleado.inicio_contrato.isoformat(),
                    empleado.estado,
                    empleado.rut,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod # revisar
    def eliminar_empleado(rut: str) -> bool:
        """
        Elimina un empleado de la base de datos por su RUT.
        """
        conn = Database().get_connection()
        cursor: Cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM empleado WHERE rut = ?", (rut,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar empleado de BD: {e}")
            return False
        finally:
            conn.close()