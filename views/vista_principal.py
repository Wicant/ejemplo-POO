#Esta sera la primera interfaz a ejecutar
from views.utils import leer_numero

class MainView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "="*30)
        print("    ECOTECH - MENÚ PRINCIPAL")
        print("="*30)
        print("1.- Gestionar Empleados")
        print("2.- Gestión de Departamentos")
        print("3.- Gestion de Proyectos")
        print("4.- Gestion de Tiempo")
        print("5.- Gestion de Informes")
        print("0.- Salir")
        print("="*30)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")