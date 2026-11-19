from models.informeDAO import InformeDAO 

class InformeView:
    @staticmethod
    def mostrar_empleados():
        datos = InformeDAO.obtener_empleado()
        if not datos:
            return

        print("\n--- INFORME DE EMPLEADOS ---")
        for fila in datos:
            print(f"Nombre: {fila[0]} | Sueldo: {fila[1]} | Inicio contrato: {fila[2]} | Departamento: {fila[3]}")

    @staticmethod
    def mostrar_departamentos():
        datos = InformeDAO.obtener_departamento()
        if not datos:
            print("No hay datos para mostrar.")
            return

        print("\n--- INFORME DE DEPARTAMENTOS ---")
        for fila in datos:
            print(f"Nombre: {fila[0]} | Gerente: {fila[1]} | Presupuesto: {fila[2]}")

    @staticmethod
    def mostrar_tiempos_por_proyecto():
        datos = InformeDAO.obtener_tiempo_proyecto()
        if not datos:
            print("No hay datos para mostrar.")
            return

        print("\n--- TIEMPOS POR PROYECTO ---")
        for fila in datos:
            print(f"Empleado: {fila[0]} | RUT: {fila[1]} | Entrada: {fila[2]} | Salida: {fila[3]} | Proyecto: {fila[4]} | Inicio: {fila[5]} | Fin: {fila[6]}")