from views.vista_departamento import DepartamentoView


class DepartamentoController:
    @staticmethod
    def menu() -> None:
        while True:
            print("\n" + "=" * 35)
            print("GESTIÓN DE DEPARTAMENTOS")
            print("=" * 35)
            print("1. Listar departamentos")
            print("2. Agregar departamento")
            print("3. Buscar departamento")
            print("4. Actualizar departamento")
            print("5. Eliminar departamento")
            print("0. Volver")
            print("=" * 35)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                DepartamentoView.listar_departamentos()
            elif opcion == "2":
                DepartamentoView.agregar_departamento()
            elif opcion == "3":
                DepartamentoView.buscar_departamento()
            elif opcion == "4":
                DepartamentoView.actualizar_departamento()
            elif opcion == "5":
                DepartamentoView.listar_departamentos()
                DepartamentoView.eliminar_departamento()
            elif opcion == "0":
                return
            else:
                print("\nOpción no válida.")