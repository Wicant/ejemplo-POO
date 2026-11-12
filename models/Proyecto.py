from models.Empleado import empleado

class Proyecto:
    """
    La clase proyecto representa un proyecto en el que los trabajadores trabajan
    esto despues estara conectado con la base de datos de tiempo para gestionar estos
    """
    
    def __init__(self, id_proyecto:int,nombre:str, descripcion:str, fecha_inicio:str,fecha_fin:str,ubicacion:str):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.ubicacion = ubicacion
        
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

    """Nombre: Representamos el nombre del proyecto"""

    @property
    def id_proyecto(self):
        return self._id_proyecto
    
    @id_proyecto.setter
    def id_proyecto(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID del departamento debe ser un número entero mayor a 0.")
        self._id_proyecto = value
        return self._id_proyecto

    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        self._nombre = nombre.strip()
        return self._nombre

    """Descripcion: Representamos la descripcion del proyecto"""

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción del proyecto no puede estar vacía")
        self._descripcion = descripcion.strip()
        return self._descripcion

    """Fecha de inicio: Representamos la fecha de inicio del proyecto"""
    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        if not isinstance(fecha_inicio, str) or not fecha_inicio.strip():
            raise ValueError("La fecha de inicio del proyecto no puede estar vacía")
        self._fecha_inicio = fecha_inicio.strip()
        return self._fecha_inicio
    
    @property
    def fecha_fin(self):
        return self._fecha_fin
    
    @fecha_fin.setter
    def fecha_fin(self, fecha_fin: str) -> None:
        if not isinstance(fecha_fin, str) or not fecha_fin.strip():
            raise ValueError("La fecha de inicio del proyecto no puede estar vacía")
        self._fecha_fin = fecha_fin.strip()
        return self._fecha_fin
    
    @property
    def ubicacion(self):
        return self._ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion: str) -> None:
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        self._ubicacion = ubicacion.strip()
        return self._ubicacion