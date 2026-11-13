from abc import ABC, abstractmethod

class persona(ABC):
    def __init__(self,rut:str,nombre:str,direccion:str,telefono:str,
                 correo:str):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

# Obtencion de atributo mediante un metodo
    @property 
    def rut(self) -> str:
        return self._rut
    # guardar un valor del objeto METODO
    @rut.setter
    def rut(self, valor: str)-> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El rut no puede estar vacio")
        self._rut = valor
        

    @property
    def nombre(self) -> str: 
        return self._nombre
    @nombre.setter
    def nombre(self, valor:str)-> None:
        if not isinstance(valor,str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = valor
        
    @property
    def direccion(self)-> str:
        return self._direccion
    @direccion.setter
    def direccion(self, valor:str):
        if not isinstance (valor,str) or not valor.strip():
            raise ValueError("La direccion no puede estar vacia")
        self._direccion = valor
        
    @property
    def telefono(self)->str:
        return self._telefono 
    @telefono.setter
    def telefono(self,valor:str)->None:
        self._telefono = valor

    @property
    def correo(self)->str:
        return self._correo
    @correo.setter
    def correo(self, valor: str)->None:
        self._correo = valor

    def __repr__(self) -> str:
        return f"Persona:(rut={self.rut}, Nombre={self.nombre}, Direccion={self.direccion}, telefono={self.telefono}, correo={self.correo})"

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass