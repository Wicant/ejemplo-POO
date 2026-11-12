
class clima:
    def __init__(self,
                 ubicacion : str, 
                 temperatura_minima : float, 
                 temperatura_maxima : float,
                 humedad : int, 
                 condicion : str, 
                 probabilidad_lluvia : int, 
                 fecha_consulta : str,
                 fecha_pronostico : str):
        self.ubicacion =            ubicacion
        self.temperatura_minima =   temperatura_minima
        self.temperatura_maxima =   temperatura_maxima
        self.humedad =              humedad
        self.condicion =            condicion
        self.probabilidad_lluvia =  probabilidad_lluvia
        self.fecha_consulta =       fecha_consulta
        self.fecha_pronostico =     fecha_pronostico 
    
    @property
    def ubicacion(self):
        return self._ubicacion
    @ubicacion.setter
    def ubicacion(self,ubicacion : str)->None:
        if not isinstance (ubicacion,str) or not ubicacion.strip():
            raise ValueError("La ubicacion no puede estar vacia")
        self._ubicacion = ubicacion
        return self._ubicacion
    
    @property
    def temperatura_minima(self):
        return self._temperatura_minima
    @temperatura_minima.setter
    def temperatura_minima(self, temperatura_minima : float) -> None:
        if not isinstance(temperatura_minima,(int,float)):
            raise ValueError("La temperatura debe ser un numero")
        self._temperatura_minima = temperatura_minima
        return self._temperatura_minima

    @property
    def temperatura_maxima(self):
        return self._temperatura_maxima
    @temperatura_maxima.setter
    def temperatura_maxima(self, temperatura_maxima : float) -> None:
        if not isinstance(temperatura_maxima,(int,float)):
            raise ValueError("La temperatura debe ser un numero")
        self._temperatura_maxima = temperatura_maxima
        return self._temperatura_maxima
    
    @property
    def humedad(self):
        return self._humedad
    @humedad.setter
    def humedad(self, humedad: int)->None:
        if not isinstance(humedad,int) or not 0 <= humedad <= 100:
            raise ValueError("La humedad no puede ser menor a 0")
        self._humedad = humedad
        return self._humedad
    
    @property
    def condicion(self):
        return self._condicion
    @condicion.setter
    def condicion(self, condicion : str) -> None:
        if not isinstance(condicion, str) or not condicion.strip():
            raise ValueError("la condicion no puede estar vacia.")
        self._condicion = condicion.strip()
        return self._condicion
    
    @property
    def probabilidad_lluvia(self):
        return self._probabilidad_lluvia
    @probabilidad_lluvia.setter
    def probabilidad_lluvia(self, value : int):
        if not isinstance(value,int) or not 0 <= value <=100:
            raise ValueError("La probabilidad de lluvia no deber ser menor a 0 o mayor a 100")
        self._probabilidad_lluvia = value
        return self._probabilidad_lluvia
    
    @property
    def fecha_consulta(self):
        return self._fecha_consulta
    @fecha_consulta.setter
    def fecha_consulta(self, fecha_consulta : str):
        if not isinstance(fecha_consulta,str) or not fecha_consulta.strip():
            raise ValueError("La fecha de consulta no puede estar vacia")
        self._fecha_consulta = fecha_consulta.strip()
        return self._fecha_consulta
    
    @property
    def fecha_pronostico(self):
        return self._fecha_pronostico
    @fecha_pronostico.setter
    def fecha_pronostico(self, fecha_pronostico : str):
        if not isinstance(fecha_pronostico,str) or not fecha_pronostico.strip():
            raise ValueError("La fecha de pronostico no puede estar vacia")
        self._fecha_pronostico = fecha_pronostico.strip()
        return self._fecha_pronostico
    