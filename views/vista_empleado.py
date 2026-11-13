import sqlite3
from datetime import date

from models.Empleado import ESTADO, empleado
from models.EmpleadoDAO import EmpleadoDAO


class VistaEmpleado:
    @staticmethod
    def mostrar_empleados() -> None:
        try:
            empleados: list[empleado] = EmpleadoDAO.obtener_todos_empleados()
        except sqlite3.Error as error:
            print(f"\nNo se pudieron consultar los empleados: {error}")
            return

        if not empleados:
            print("\nNo hay empleados para mostrar.")
            return

        print(f"\nEmpleados encontrados: {len(empleados)}")
        print("=" * 45)
        for persona in empleados:
            print(persona.mostrar_detalle())
            print("-" * 45)

    @staticmethod
    def modificar_empleado() -> None:
        rut = input("\nIngrese el RUT del empleado que desea modificar: ").strip()
        if not rut:
            print("El RUT no puede estar vacío.")
            return

        try:
            persona = EmpleadoDAO.obtener_empleado_por_rut(rut)
        except (sqlite3.Error, ValueError) as error:
            print(f"\nNo se pudo consultar el empleado: {error}")
            return

        if persona is None:
            print(f"\nNo se encontró un empleado con RUT {rut}.")
            return

        print("\nDatos actuales:")
        print(persona.mostrar_detalle())
        print("\nDeje el campo vacío y presione Enter para conservar el valor actual.")

        persona.nombre = VistaEmpleado._leer_texto("Nombre", persona.nombre)
        persona.direccion = VistaEmpleado._leer_texto("Dirección", persona.direccion)
        persona.telefono = VistaEmpleado._leer_texto("Teléfono", persona.telefono)
        persona.correo = VistaEmpleado._leer_texto("Correo", persona.correo)
        persona.id_departamento = VistaEmpleado._leer_entero(
            "ID de departamento", persona.id_departamento
        )
        persona.sueldo = VistaEmpleado._leer_entero("Sueldo", persona.sueldo)
        persona.inicio_contrato = VistaEmpleado._leer_fecha(persona.inicio_contrato)
        persona.estado = VistaEmpleado._leer_estado(persona.estado)

        confirmar = input("\n¿Guardar los cambios? (s/n): ").strip().lower()
        if confirmar not in ("s", "si", "sí"):
            print("Cambios descartados.")
            return

        try:
            actualizado = EmpleadoDAO.actualizar_empleado(persona)
        except sqlite3.Error as error:
            print(f"\nNo se pudieron guardar los cambios: {error}")
            return

        if actualizado:
            print("Información del empleado actualizada correctamente.")
        else:
            print("No se actualizaron los datos. Verifique que el empleado exista.")
    
    @staticmethod
    def crear_empleado() -> None:
        print("\n--- AGREGAR  ---")
        try:
            rut = input("RUT: ").strip()
            nombre = input("Nombre: ").strip()
            direccion = input("Dirección: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo: ").strip()
            valor_departamento = input("ID departamento (opcional): ").strip()
            id_departamento = int(valor_departamento) if valor_departamento else None
            sueldo = int(input("Sueldo: ").strip())
            inicio_contrato = date.fromisoformat(input("Inicio de contrato (AAAA-MM-DD): ").strip())
            estado = input(f"Estado ({', '.join(ESTADO)}): ").strip().lower()
        except ValueError as e:
            print(f"Error: {e}")
            return

        try:
            nuevo_empleado = empleado(
                id_departamento=id_departamento,
                sueldo=sueldo,
                inicio_contrato=inicio_contrato,
                rut=rut,
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
                estado=estado
            )

            guardado = EmpleadoDAO.agregar_empleado(nuevo_empleado)

            if guardado:
                print("\nEmpleado registrado correctamente.")
            else:
                print("\nNo se pudo registrar el empleado.")

        except ValueError as error:
            print(f"\nError al crear el empleado: {error}")
        except sqlite3.Error as error:
            print(f"\nError al guardar el empleado en BD: {error}")
    @staticmethod
    def _leer_texto(etiqueta: str, actual: str) -> str:
        valor = input(f"{etiqueta} [{actual}]: ").strip()
        return valor or actual

    @staticmethod
    def _leer_entero(etiqueta: str, actual: int| None) -> int | None:
        while True:
            valor = input(f"{etiqueta} [{actual}]: ").strip()
            if not valor:
                return actual
            try:
                numero = int(valor)
                if numero < 0:
                    raise ValueError
                return numero
            except ValueError:
                print("Ingrese un número entero igual o mayor que cero.")

    @staticmethod
    def _leer_fecha(actual: date) -> date:
        while True:
            valor = input(f"Inicio de contrato [{actual.isoformat()}] (AAAA-MM-DD): ").strip()
            if not valor:
                return actual
            try:
                return date.fromisoformat(valor)
            except ValueError:
                print("Fecha inválida. Use el formato AAAA-MM-DD.")

    @staticmethod
    def _leer_estado(actual: str) -> str:
        opciones = ", ".join(ESTADO)
        while True:
            valor = input(f"Estado ({opciones}) [{actual}]: ").strip().lower()
            if not valor:
                return actual
            if valor in ESTADO:
                return valor
            print(f"Estado inválido. Elija uno de estos valores: {opciones}.")

    @staticmethod
    def buscar_por_id():
        id_empleado = input("Ingrese el RUT del empleado: ").strip()
        empleado = EmpleadoDAO.obtener_empleado_por_rut(id_empleado)
        if empleado:
            print(f"\nRut: {empleado.rut}")
            print(f"Nombre: {empleado.nombre}")
            print(f"telefono: {empleado.telefono}")
            print(f"correo: {empleado.correo}")
            print(f"ID_departamento: {empleado.id_departamento}")
            print(f"Sueldo: {empleado.sueldo}")
            print(f"Inicio de contrato: {empleado.inicio_contrato}")
            print(f"Estado: {empleado.estado}")
        else:
            print("No se encontró el empleado.")
            
    @staticmethod
    def eliminar_empleado():
        id_empleado = input("Ingrese el RUT del empleado: ").strip()
        if EmpleadoDAO.eliminar_empleado(id_empleado):
            print("Empleado eliminado correctamente")
        else:
            print("No se pudo eliminar al empleado")