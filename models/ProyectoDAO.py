from sqlite3 import Cursor
from datetime import date
from config.database import Database
from models.Proyecto import Proyecto

class ProyectoDAO:
    @staticmethod
    def agregar_proyecto(proyecto_obj: Proyecto):
        conn = Database().get_connection()
        try: 
            cursor : Cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO proyecto (
                id_proyecto, 
                nombre, 
                descripcion, 
                fecha_inicio, 
                fecha_fin,
                ubicacion)
            VALUES(?,?,?,?,?,?)"""
            ,(proyecto_obj.id_proyecto, 
              proyecto_obj.nombre,
              proyecto_obj.descripcion,
              proyecto_obj.fecha_inicio,
              proyecto_obj.fecha_fin,
              proyecto_obj.ubicacion))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar proyecto en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def crear_proyecto(fila)->Proyecto:
        fecha_inicio = fila["fecha_inicio"]
        if isinstance(fecha_inicio,str):
            fecha_inicio = date.fromisoformat(fecha_inicio)
        
        fecha_fin = fila["fecha_fin"]
        if isinstance(fecha_fin,str):
            fecha_fin = date.fromisoformat(fecha_fin)
        
        return Proyecto(
            fila["id_proyecto"],
            fila["nombre"],
            fila["descripcion"],
            fila["fecha_inicio"],
            fila["fecha_fin"],
            fila["ubicacion"]
        )         
    @staticmethod
    def obtener_proyectos():
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""SELECT id_proyecto, nombre, descripcion,
                           fecha_inicio, fecha_fin, ubicacion 
                           from proyecto""")
            return [ProyectoDAO.crear_proyecto(fila) for fila in cursor.fetchall()]
        except Exception as e:
            print(f"Error al obtener proyecto en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def obtener_proyecto_id(id_proyecto : int):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""SELECT * from proyecto WHERE id_proyecto = ?""",(id_proyecto,))
            proyecto_data = cursor.fetchone()
            return ProyectoDAO.crear_proyecto(proyecto_data) if proyecto_data else None
        except Exception as e:
            print(f"Error al obtener proyecto en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def actualizar_proyecto(proyecto_obj:Proyecto):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""UPDATE proyecto
                           SET nombre = ?, 
                           descripcion = ?, 
                           fecha_inicio = ?, 
                           fecha_fin = ?, 
                           ubicacion = ?
                           WHERE id_proyecto = ?""", 
                           (proyecto_obj.nombre,
                            proyecto_obj.descripcion,
                            proyecto_obj.fecha_inicio,
                            proyecto_obj.fecha_fin,
                            proyecto_obj.ubicacion,
                            proyecto_obj.id_proyecto))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar proyecto en BD: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def eliminar_proyecto(id_proyecto: int):
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""DELETE FROM proyecto WHERE id_proyecto = ?"""
                           ,(id_proyecto,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar proyecto en BD: {e}")
            return False
        finally:
            conn.close()
            
    