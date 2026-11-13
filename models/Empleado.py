from datetime import date
from models.persona import persona

ESTADO = ["activo", "inactivo", "vacaciones", "suspendido"] 

class empleado(persona):
    def __init__(self,id_departamento:int | None ,sueldo:int,inicio_contrato:date,rut:str,
                 nombre:str,direccion:str,telefono:str,correo:str, estado:str):
        super().__init__(rut,nombre,direccion,telefono,correo)
        self._id_departamento = id_departamento
        self._sueldo = sueldo
        self._inicio_contrato = inicio_contrato 
        self._estado = estado  # Estado inicial del empleado
        
    @property
    def id_departamento(self)-> int | None:
        return self._id_departamento
    
    @id_departamento.setter
    def id_departamento (self,valor:int | None)-> None:
        if valor is not None and (not isinstance(valor, int) or valor < 0):
            raise ValueError("Identificador de area de trabajo debe ser un número positivo")
        self._id_departamento = valor
    
    @property
    def sueldo(self)->int:
        return self._sueldo
    
    @sueldo.setter
    def sueldo (self, valor:int)-> None:
        if not isinstance(valor,int) or valor < 0:
            raise ValueError("El sueldo debe ser un numero y no debe ser negativo")
        self._sueldo = valor

    @property
    def inicio_contrato (self)-> date:
            return self._inicio_contrato
        
    @inicio_contrato.setter
    def inicio_contrato(self,valor:date) -> None:
        if not isinstance(valor,date):
            raise ValueError("El dato ingresado debe ser una fecha")
        self._inicio_contrato = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if isinstance(valor,str) and valor in ESTADO:
            self._estado = valor
        else:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(ESTADO)}")

    def mostrar_detalle(self) -> str:
        return (
            f"RUT: {self.rut}\n"
            f"Nombre: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.telefono}\n"
            f"Correo: {self.correo}\n"
            f"ID de departamento: {self.id_departamento}\n"
            f"Sueldo: {self.sueldo}\n"
            f"Inicio de contrato: {self.inicio_contrato}\n"
            f"Estado: {self.estado}"
        )