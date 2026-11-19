
class MonedaView:
    

    @staticmethod
    def consultar_moneda():
        print("\n--- CONSULTAR MONEDA ---")
        print("1.- Dólar estadounidense")
        print("2.- Euro")
        print("0.- Volver")

        opcion = input("\nSeleccione una moneda: ")

        if opcion == "1":
            return "F073.TCO.PRE.Z.D"

        elif opcion == "2":
            return "F072.CLP.EUR.N.O.D"

        elif opcion == "0":
            return None

        else:
            print("Seleccione una opción válida.")
            return None
    
    @staticmethod
    def mostrar_moneda(moneda):
        print("\n--- COTIZACIÓN MONETARIA ---")
        print(f"Moneda: {moneda.nombre}")
        print(f"Código: {moneda.simbolo}")
        print(f"Valor en CLP: ${moneda.valor}")
        print(f"Fecha de cotización: {moneda.fecha}")
        
    @staticmethod
    def menu():
        print("\n====== GESTIÓN DE MONEDAS ======")
        print("1.- Consultar cotización de una divisa")
        print("2.- Consultar sueldo de empleado en otra divisa")
        print("0.- Volver")

        opcion = input("\nSeleccione una opción: ")

        return opcion
    
    @staticmethod
    def seleccionar_empleado(empleados):
        print("\n--- EMPLEADOS REGISTRADOS ---")

        if not empleados:
            print("No hay empleados registrados.")
            return None

        for empleado in empleados:
            print(
                f"{empleado.rut}.- "
                f"{empleado.nombre} | "
                f"Sueldo: ${empleado.sueldo:,.0f} CLP"
            )
        rut = input("\nIngrese el rut del empleado elegido: ").strip()

        if not rut:
            print("Debe ingresar un RUT.")
            return None

        return rut
    
    @staticmethod
    def mostrar_conversion_sueldo(empleado, moneda, resultado):
        print("\n--- CONVERSIÓN DE SUELDO ---")
        print(f"Empleado: {empleado.nombre}")
        print(f"RUT: {empleado.rut}")
        print(f"Sueldo original: ${empleado.sueldo:,.0f} CLP")
        print(f"Divisa: {moneda.nombre} ({moneda.simbolo})")
        print(f"Cotización: ${moneda.valor} CLP")
        print(f"Sueldo convertido: {resultado:,.2f} {moneda.simbolo}")
    
    @staticmethod
    def preguntar_guardar_cotizacion():
        print("\n¿Desea guardar esta cotización en el historial?")
        print("1.- Sí")
        print("2.- No")

        opcion = input("\nSeleccione una opción: ").strip()

        return opcion == "1"