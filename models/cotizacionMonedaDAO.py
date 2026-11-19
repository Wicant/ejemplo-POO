from sqlite3 import Cursor
from config.database import Database
from models.cotizacionMoneda import CotizacionMoneda

class CotizacionMonedaDAO:
    
    @staticmethod
    def agregar_cotizacion(cotizacion: CotizacionMoneda) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO conversion_moneda(
                        codigo_moneda,
                        valor, 
                        fecha_cotizacion,
                        fecha_guardado)
                        VALUES(?,?,?,?)""",(
                            cotizacion.codigo_moneda,
                            cotizacion.valor,
                            cotizacion.fecha_cotizacion,
                            cotizacion.fecha_guardado
                        )
                    )
            conn.commit()
            cotizacion.id_cotizacion = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al agregar cotizacion en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def crear_moneda(fila)-> CotizacionMoneda:
        return CotizacionMoneda(
            fila["codigo_moneda"],
            fila["valor"],
            fila["fecha_cotizacion"],
            fila["fecha_guardado"],
            fila["id_cotizacion"]
        )
    
    @staticmethod
    def obtener_por_moneda(codigo_moneda : str) -> list[CotizacionMoneda]:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("""SELECT * FROM conversion_moneda
                           WHERE codigo_moneda = ?
                           ORDER BY fecha_cotizacion DESC;""",(codigo_moneda,))
            moneda_data = cursor.fetchall()
            cotizaciones = []

            for fila in moneda_data:
                cotizacion = CotizacionMonedaDAO.crear_moneda(fila)
                cotizaciones.append(cotizacion)

            return cotizaciones
        except Exception as e:
            print(f"Error al obtener la cotizaciones en BD: {e}")
            return []
        finally:
            conn.close()

            
    @staticmethod
    def eliminar_cotizacion_moneda(id_cotizacion: int)-> bool:
        conn = Database().get_connection()
        try:
            cursor : Cursor = conn.cursor()
            cursor.execute("""DELETE FROM conversion_sueldo WHERE id_cotizacion = ?"""
                            ,(id_cotizacion,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar cotización en BD: {e}")
            return False
        finally:
            conn.close()