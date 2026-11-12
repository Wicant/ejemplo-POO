from views.vista_empleado import VistaEmpleado


class EmpleadoController:
    @staticmethod
    def menu() -> None:
        while True:
            print("\n" + "=" * 35)
            print("GESTIÓN DE EMPLEADOS")
            print("=" * 35)
            print("1. Ver empleados")
            print("2. Modificar empleado")
            print("3. Crear empleado")
            print("4. Buscar empleado por ID")
            print("5. Eliminar empleado")
            print("0. Volver")
            print("=" * 35)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                VistaEmpleado.mostrar_empleados()
            elif opcion == "2":
                VistaEmpleado.modificar_empleado()
            elif opcion == "3":
                VistaEmpleado.crear_empleado()
            elif opcion == "4":
                VistaEmpleado.buscar_por_id()
            elif opcion == "5":
                VistaEmpleado.mostrar_empleados()
                VistaEmpleado.eliminar_empleado()
            elif opcion == "0":
                return
            else:
                print("\nOpción no válida.")