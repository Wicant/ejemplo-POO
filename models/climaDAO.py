from sqlite3 import Cursor
from config.database import Database
from models.clima import clima

class ClimaDAO:
    
    @staticmethod
    def agregar_clima(clima: clima) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO clima(
                        id_proyecto,
                        ubicacion, 
                        temperatura_minima,
                        temperatura_maxima,
                        humedad, 
                        condicion, 
                        probabilidad_lluvia,
                        fecha_consulta,
                        fecha_pronostico)
                        VALUES(?,?,?,?,?,?,?,?,?)""",(
                            clima.id_proyecto,
                            clima.ubicacion,
                            clima.temperatura_minima,
                            clima.temperatura_maxima,
                            clima.humedad,
                            clima.condicion,
                            clima.probabilidad_lluvia,
                            clima.fecha_consulta,
                            clima.fecha_pronostico
                        )
                    )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar clima en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def crear_clima(fila)-> clima:
        return clima(
            fila["id_clima"],
            fila["id_proyecto"],
            fila["ubicacion"],
            fila["temperatura_minima"],
            fila["temperatura_maxima"],
            fila["humedad"],
            fila["condicion"],
            fila["probabilidad_lluvia"],
            fila["fecha_consulta"],
            fila["fecha_pronostico"]
        )
    
    @staticmethod
    def obtener_clima_proyecto(id_proyecto : int) -> clima:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""SELECT id_clima,
                           id_proyecto,
                           ubicacion,
                           temperatura_minima,
                           temperatura_maxima,         
                           humedad, 
                           condicion, 
                           probabilidad_lluvia, 
                           fecha_consulta,
                           fecha_pronostico
                           FROM clima c
                           JOIN proyecto p 
                           ON c.id_proyecto = p.id_proyecto
                           WHERE id_proyecto = ?""",(id_proyecto,))
            clima_data = cursor.fetchone()
            return ClimaDAO.crear_clima(clima_data) if clima_data else None
        except Exception as e:
            print(f"Error al obtener el clima en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_ultimo_clima(id_proyecto : int) -> clima:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""SELECT id_clima,
                           id_proyecto,
                           ubicacion,
                           temperatura_minima,
                           temperatura_maxima,         
                           humedad, 
                           condicion, 
                           probabilidad_lluvia, 
                           fecha_consulta,
                           fecha_pronostico
                           FROM clima c
                           JOIN proyecto p 
                           ON c.id_proyecto = p.id_proyecto
                           WHERE id_proyecto = ?
                           ORDER BY ID_CLIMA DESC"""
                           ,(id_proyecto,))
            clima_data = cursor.fetchone()
            return ClimaDAO.crear_clima(clima_data) if clima_data else None
        except Exception as e:
            print(f"Error al obtener el clima en BD: {e}")
            return False
        finally:
            conn.close()
            
    @staticmethod
    def obtener_clima_ubicacion(ubicacion : str) -> clima:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""SELECT id_clima,
                           id_proyecto,
                           ubicacion,
                           temperatura_minima,
                           temperatura_maxima,         
                           humedad, 
                           condicion, 
                           probabilidad_lluvia, 
                           fecha_consulta,
                           fecha_pronostico
                           FROM clima 
                           WHERE ubicacion = ?
                           ORDER BY ID_CLIMA DESC"""
                           ,(ubicacion,))
            clima_data = cursor.fetchone()
            return ClimaDAO.crear_clima(clima_data) if clima_data else None
        except Exception as e:
            print(f"Error al obtener el clima en BD: {e}")
            return False
        finally:
            conn.close()