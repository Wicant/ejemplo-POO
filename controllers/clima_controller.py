from views.vista_clima import ClimaView
from models.ProyectoDAO import ProyectoDAO


class ClimaController:

    @staticmethod
    def menu():
        proyectos = ProyectoDAO.obtener_proyectos()

        if proyectos is False:
            print("Error al obtener los proyectos.")
            return

        id_proyecto = ClimaView.seleccionar_proyecto(proyectos)

        if id_proyecto is None:
            return

        proyecto = ProyectoDAO.obtener_proyecto_id(id_proyecto)

        if proyecto is None or proyecto is False:
            print("No se encontró el proyecto seleccionado.")
            return

        ClimaView.consultar_clima(proyecto.ubicacion)