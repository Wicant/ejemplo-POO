from views.vista_principal import MainView
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controller import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.tiempo_controller import TiempoController
from controllers.informe_controller import InformeController
from controllers.auth_controller import AuthController
from controllers.clima_controller import ClimaController
from controllers.moneda_controller import MonedaController


class MainController:
    @staticmethod
    def iniciar() -> None:
        auth = AuthController()
        usuario = auth.iniciar_sesion()

        if usuario is None:
            print("\nCerrando aplicación...")
            return
        
        while True:
            opcion = MainView.mostrar_menu()

            if opcion == 1:
                EmpleadoController.menu()
            elif opcion == 2:
                DepartamentoController.menu()
            elif opcion == 3:
                ProyectoController.menu()
            elif opcion == 4:
                TiempoController.menu()
            elif opcion == 5:
                InformeController.menu()
            elif opcion == 6:
                ClimaController.menu()
            elif opcion == 7:
                MonedaController.menu()
            elif opcion == 0:
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")