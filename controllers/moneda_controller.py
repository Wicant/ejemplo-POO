from views.vista_moneda import MonedaView
from services.moneda_service import MonedaServices
from models.EmpleadoDAO import EmpleadoDAO
from models.cotizacionMoneda import CotizacionMoneda
from models.cotizacionMonedaDAO import CotizacionMonedaDAO
from datetime import date, datetime


class MonedaController:

    @staticmethod
    def menu():
        opcion = MonedaView.menu()

        if opcion == "1":
            codigo = MonedaView.consultar_moneda()

            if codigo is None:
                return

            moneda, mensaje = MonedaServices.obtener_moneda(codigo)

            if not moneda:
                print(f"\nError: {mensaje}")
                return
            if mensaje:
                print(mensaje)
            MonedaView.mostrar_moneda(moneda)
            if MonedaView.preguntar_guardar_cotizacion():
                MonedaController.guardar_cotizacion(moneda)

        elif opcion == "2":
            MonedaController.convertir_sueldo()

        elif opcion == "0":
            return

        else:
            print("\nOpción no válida.")
            
    @staticmethod
    def convertir_sueldo():
        empleados = EmpleadoDAO.obtener_todos_empleados()

        rut = MonedaView.seleccionar_empleado(empleados)

        if rut is None:
            return

        empleado = EmpleadoDAO.obtener_empleado_por_rut(rut)

        if empleado is None:
            print("\nNo se encontró un empleado con ese RUT.")
            return

        codigo = MonedaView.consultar_moneda()

        if codigo is None:
            return

        moneda, mensaje = MonedaServices.obtener_moneda(codigo)

        if not moneda:
            print(f"\nError: {mensaje}")
            return
        if mensaje:
            print(mensaje)

        resultado = empleado.sueldo / moneda.valor

        MonedaView.mostrar_conversion_sueldo(
            empleado,
            moneda,
            resultado
        )
        if MonedaView.preguntar_guardar_cotizacion():
            MonedaController.guardar_cotizacion(moneda)
    
    @staticmethod
    def guardar_cotizacion(moneda):
        cotizacion = CotizacionMoneda(
            codigo_moneda=moneda.simbolo,
            valor=moneda.valor,
            fecha_cotizacion=datetime.strptime(moneda.fecha, "%d-%m-%Y").date().isoformat(),
            fecha_guardado=date.today().isoformat()
        )

        resultado = CotizacionMonedaDAO.agregar_cotizacion(cotizacion)

        if resultado:
            print("\nCotización guardada correctamente.")
        else:
            print("\nNo se pudo guardar la cotización.")