from models.Proyecto import Proyecto
from models.ProyectoDAO import ProyectoDAO


class ProyectoView:
    @staticmethod
    def listar_proyectos():
        proyectos = ProyectoDAO.obtener_proyectos()
        if not proyectos:
            print("No hay proyectos registrados.")
            return

        print("\n--- LISTA DE PROYECTOS ---")
        for p in proyectos:
            print(
                f"ID: {p.id_proyecto} | "
                f"Nombre: {p.nombre} | "
                f"Fecha inicio: {p.fecha_inicio} | "
                f"Fecha fin: {p.fecha_fin} | "
                f"ubicacion: {p.ubicacion}"
            )

    @staticmethod
    def agregar_proyecto():
        print("\n--- AGREGAR PROYECTO ---")
        id_proyecto = int(input("ID del proyecto: "))
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripción del proyecto: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
        ubicacion = input("ingrese la ubicacion del proyecto: ")

        proyecto = Proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, ubicacion)

        if ProyectoDAO.agregar_proyecto(proyecto):
            print("Proyecto agregado correctamente.")
            return proyecto
        else:
            print("No se pudo agregar el proyecto.")
            return None

    @staticmethod
    def buscar_proyecto():
        id_proyecto = int(input("Ingrese ID del proyecto: "))
        proyecto = ProyectoDAO.obtener_proyecto_id(id_proyecto)

        if proyecto:
            print(f"\nID: {proyecto.id_proyecto}")
            print(f"Nombre: {proyecto.nombre}")
            print(f"Descripcion: {proyecto.descripcion}")
            print(f"Fecha inicio: {proyecto.fecha_inicio}")
            print(f"Fecha fin: {proyecto.fecha_fin}")
            print(f"ubicacion: {proyecto.ubicacion}")
        else:
            print("No se encontró el proyecto.")

    @staticmethod
    def actualizar_proyecto():
        id_proyecto = int(input("Ingrese ID del proyecto a actualizar: "))
        proyecto = ProyectoDAO.obtener_proyecto_id(id_proyecto)

        if not proyecto:
            print("Proyecto no encontrado.")
            return

        print("Deje vacío cualquier campo que no quiera cambiar.")
        nuevo_nombre = input(f"Nuevo nombre ({proyecto.nombre}): ") or proyecto.nombre
        nueva_descripcion = input(f"Nueva descripcion ({proyecto.descripcion}): ") or proyecto.descripcion
        nueva_fecha_inicio = input(f"Nueva fecha inicio ({proyecto.fecha_inicio}): ") or proyecto.fecha_inicio
        nueva_fecha_fin = input(f"Nueva fecha fin ({proyecto.fecha_fin}): ") or proyecto.fecha_fin
        nueva_ubicacion = input(f"Nueva ubicacion({proyecto.ubicacion}): " ) or proyecto.ubicacion

        proyecto.nombre = nuevo_nombre
        proyecto.fecha_inicio = nueva_fecha_inicio
        proyecto.fecha_fin = nueva_fecha_fin
        proyecto.descripcion = nueva_descripcion
        proyecto.ubicacion = nueva_ubicacion

        if ProyectoDAO.actualizar_proyecto(proyecto):
            print("Proyecto actualizado correctamente.")
        else:
            print("No se pudo actualizar el proyecto.")

    @staticmethod
    def eliminar_proyecto():
        id_proyecto = int(input("Ingrese ID del proyecto a eliminar: "))
        if ProyectoDAO.eliminar_proyecto(id_proyecto):
            print("Proyecto eliminado correctamente.")
        else:
            print("No se pudo eliminar el proyecto.")