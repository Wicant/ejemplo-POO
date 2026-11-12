from models.Tiempo import Tiempo
from models.TiempoDAO import TiempoDAO #hacer controllers


class TiempoView:
    @staticmethod
    def listar_tiempos():
        tiempos = TiempoDAO.obtener_tiempos()
        if not tiempos:
            print("No hay tiempos registrados.")
            return

        print("\n--- LISTA DE TIEMPOS ---")
        for t in tiempos:
            print(f"ID: {t.id_tiempo} |"
                  f"Fecha: {t.fecha} | " 
                  f"Entrada: {t.hora_entrada} |" 
                  f"Salida: {t.hora_salida} |" 
                  f"ID Empleado: {t.id_empleado} |" 
                  f"ID Proyecto: {t.id_proyecto}")

    @staticmethod
    def agregar_tiempo():
        print("\n--- AGREGAR TIEMPO ---")
        fecha = input("Fecha (YYYY-MM-DD): ")
        hora_entrada = input("Hora de entrada (HH:MM): ")
        hora_salida = input("Hora de salida (HH:MM): ")
        id_empleado = input("ID empleado: ")
        id_proyecto = input("ID proyecto: ")

        tiempo = Tiempo(
            id_tiempo=None,
            fecha=fecha,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            id_empleado=id_empleado,
            id_proyecto=id_proyecto
        )

        if TiempoDAO.agregar_tiempo(tiempo):
            print("Tiempo agregado correctamente.")
        else:
            print("No se pudo agregar el tiempo.")

    @staticmethod
    def buscar_tiempo():
        id_tiempo = int(input("Ingrese ID del tiempo: "))
        tiempo = TiempoDAO.obtener_tiempo_id(id_tiempo)

        if tiempo:
            print(f"\nID: {tiempo.id_tiempo}")
            print(f"Fecha: {tiempo.fecha}")
            print(f"Hora entrada: {tiempo.hora_entrada}")
            print(f"Hora salida: {tiempo.hora_salida}")
            print(f"ID empleado: {tiempo.id_empleado}")
            print(f"ID proyecto: {tiempo.id_proyecto}")
        else:
            print("No se encontró el tiempo.")

    @staticmethod
    def actualizar_tiempo():
        id_tiempo = int(input("Ingrese ID del tiempo a actualizar: "))
        tiempo = TiempoDAO.obtener_tiempo_id(id_tiempo)

        if not tiempo:
            print("Tiempo no encontrado.")
            return

        print("Deje vacío cualquier campo que no quiera cambiar.")
        nueva_fecha = input(f"Nueva fecha ({tiempo.fecha}): ") or tiempo.fecha
        nueva_entrada = input(f"Nueva hora entrada ({tiempo.hora_entrada}): ") or tiempo.hora_entrada
        nueva_salida = input(f"Nueva hora salida ({tiempo.hora_salida}): ") or tiempo.hora_salida
        nuevo_id_empleado = input(f"Nuevo ID empleado ({tiempo.id_empleado}): ") or tiempo.id_empleado
        nuevo_id_proyecto = input(f"Nuevo ID proyecto ({tiempo.id_proyecto}): ") or tiempo.id_proyecto

        tiempo.fecha = nueva_fecha
        tiempo.hora_entrada = nueva_entrada
        tiempo.hora_salida = nueva_salida
        tiempo.id_empleado = nuevo_id_empleado
        tiempo.id_proyecto = nuevo_id_proyecto

        if TiempoDAO.actualizar_tiempo(tiempo):
            print("Tiempo actualizado correctamente.")
        else:
            print("No se pudo actualizar el tiempo.")

    @staticmethod
    def eliminar_tiempo():
        id_tiempo = int(input("Ingrese ID del tiempo a eliminar: "))
        if TiempoDAO.eliminar_tiempo(id_tiempo):
            print("Tiempo eliminado correctamente.")
        else:
            print("No se pudo eliminar el tiempo.")