from sqlite3 import Cursor 
from config.database import Database
from models.Tiempo import Tiempo

class TiempoDAO:
    @staticmethod
    def agregar_tiempo(tiempo:Tiempo):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""INSERT INTO tiempo
                           (fecha, 
                           hora_entrada, 
                           hora_salida, 
                           id_empleado,
                           id_proyecto)
                           VALUES(?,?,?,?,?)""",
                           (tiempo.fecha,
                           tiempo.hora_entrada,
                           tiempo.hora_salida,
                           tiempo.id_empleado,
                           tiempo.id_proyecto))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar tiempo en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def crear_tiempo(fila)-> Tiempo:
        return Tiempo(
            fila["id_tiempo"],
            fila["fecha"],
            fila["hora_entrada"],
            fila["hora_salida"],
            fila["id_empleado"],
            fila["id_proyecto"]
        )
    @staticmethod
    def obtener_tiempo_id(id_tiempo: int):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""SELECT id_tiempo, fecha, hora_entrada, hora_salida, id_empleado, id_proyecto
                           FROM tiempo WHERE id_tiempo = ?""",
                           (id_tiempo,))
            tiempo_data = cursor.fetchone() #corregir para que devuelva
            return TiempoDAO.crear_tiempo(tiempo_data) if tiempo_data else None
        except Exception as e:
            print(f"Error al obtener tiempo en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def obtener_tiempos():
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""SELECT id_tiempo, fecha, hora_entrada, hora_salida, id_empleado, id_proyecto FROM tiempo""")
            return [TiempoDAO.crear_tiempo(fila) for fila in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener tiempo en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def actualizar_tiempo(tiempo_obj: Tiempo):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""UPDATE tiempo
                           SET fecha = ?, 
                           hora_entrada = ?,
                           hora_salida = ?,
                           id_empleado = ?,
                           id_proyecto = ? 
                           WHERE id_tiempo = ?""",
                           (tiempo_obj.fecha,
                            tiempo_obj.hora_entrada,
                            tiempo_obj.hora_salida,
                            tiempo_obj.id_empleado,
                            tiempo_obj.id_proyecto,
                            tiempo_obj.id_tiempo))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar tiempo en BD: {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def eliminar_tiempo(id_tiempo : int):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""DELETE from tiempo 
                           WHERE id_tiempo = ?""", (id_tiempo,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar tiempo en BD: {e}")
            return False
        finally:
            conn.close()