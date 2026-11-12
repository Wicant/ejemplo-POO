from views.vista_tiempo import TiempoView


class TiempoController:
    @staticmethod
    def menu() -> None:
        while True:
            print("\n" + "=" * 35)
            print("GESTIÓN DE TIEMPOS")
            print("=" * 35)
            print("1. Listar tiempos")
            print("2. Agregar tiempo")
            print("3. Buscar tiempo")
            print("4. Actualizar tiempo")
            print("5. Eliminar tiempo")
            print("0. Volver")
            print("=" * 35)

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                TiempoView.listar_tiempos()
            elif opcion == "2":
                TiempoView.agregar_tiempo()
            elif opcion == "3":
                TiempoView.buscar_tiempo()
            elif opcion == "4":
                TiempoView.actualizar_tiempo()
            elif opcion == "5":
                TiempoView.listar_tiempos()
                TiempoView.eliminar_tiempo()
            elif opcion == "0":
                return
            else:
                print("\nOpción no válida.")