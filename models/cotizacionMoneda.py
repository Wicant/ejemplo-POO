from datetime import date
class CotizacionMoneda:
    def __init__(self,
                 codigo_moneda :str,  
                 valor: float,
                 fecha_cotizacion : str,
                 fecha_guardado : str,
                 id_cotizacion: int | None = None):
        self.id_cotizacion = id_cotizacion
        self.codigo_moneda = codigo_moneda
        self.valor = valor
        self.fecha_cotizacion = fecha_cotizacion
        self.fecha_guardado = fecha_guardado
            
    @property
    def codigo_moneda(self):
        return self._codigo_moneda
    @codigo_moneda.setter
    def codigo_moneda(self, codigo_moneda: str) -> None:
        if not isinstance(codigo_moneda, str) or not codigo_moneda.strip():
            raise ValueError("El codigo no puede estar vacío")
        self._codigo_moneda = codigo_moneda.strip().upper()

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor: float | int) -> None:
        if not isinstance(valor, float | int) or  valor <= 0:
            raise ValueError("El valor no puede ser menor a 0")
        self._valor = valor
        
    @property
    def fecha_cotizacion(self):
        return self._fecha_cotizacion
    @fecha_cotizacion.setter
    def fecha_cotizacion(self, fecha_cotizacion: str | date) -> None:
        if isinstance(fecha_cotizacion, str):
            if not fecha_cotizacion.strip():
                raise ValueError("La fecha de cotizacion no puede estar vacía")
            try:
                fecha_cotizacion = date.fromisoformat(fecha_cotizacion)
            except ValueError:
                raise ValueError("El formato de la fecha de cotización no es válido.")

        elif not isinstance(fecha_cotizacion, date):
            raise ValueError("La fecha de cotizacion no es válida.")
        self._fecha_cotizacion = fecha_cotizacion
        
    @property
    def fecha_guardado(self):
        return self._fecha_guardado
    @fecha_guardado.setter
    def fecha_guardado(self, fecha_guardado: str | date) -> None:
        if isinstance(fecha_guardado, str):
            if not fecha_guardado.strip():
                raise ValueError("La fecha de guardado no puede estar vacía")
            try:
                fecha_guardado = date.fromisoformat(fecha_guardado)
            except ValueError:
                raise ValueError("El formato de la fecha de guardado no es válido.")
        elif not isinstance(fecha_guardado, date):
            raise ValueError("La fecha de guardado no es válida.")
        self._fecha_guardado = fecha_guardado