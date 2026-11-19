class Moneda:
    def __init__(self,
                 nombre : str, 
                 codigo : str, 
                 simbolo : str,
                 valor : float, 
                 fecha : str):
        self.nombre =   nombre
        self.codigo =   codigo
        self.simbolo =  simbolo
        self.valor =    valor
        self.fecha =    fecha

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre : str)->None:
        if not isinstance (nombre,str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre


    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,codigo : str)->None:
        if not isinstance (codigo,str) or not codigo.strip():
            raise ValueError("El codigo no puede estar vacio")
        self._codigo = codigo
       
    
    @property
    def simbolo(self):
        return self._simbolo
    @simbolo.setter
    def simbolo(self,simbolo : str)->None:
        if not isinstance (simbolo,str) or not simbolo.strip():
            raise ValueError("El simbolo no puede estar vacio")
        self._simbolo = simbolo        
    
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self,valor : float)->None:
        if not isinstance (valor,float) or valor <= 0:
            raise ValueError("El valor no puede estar vacio")
        self._valor = valor

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha : str)->None:
        if not isinstance (fecha,str) or not fecha.strip():
            raise ValueError("La fecha no puede estar vacia")
        self._fecha = fecha 