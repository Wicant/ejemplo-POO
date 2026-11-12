import re
from typing import List, Tuple
from models.climaDAO import ClimaDAO
from datetime import datetime
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

from config.settings import Settings
from models.clima import clima

class ClimaServices:
    
    
    @staticmethod
    def sanitizar_termino(termino: str) -> str:
        """Valida que la entrada del usuario no contenga caracteres maliciosos."""
        if not termino or not isinstance(termino, str):
            raise ValueError("El término de búsqueda debe ser un texto válido.")
        
        limpio = termino.strip()
        if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ]+$", limpio):
            raise ValueError("El término contiene caracteres no permitidos.")
        
        if len(limpio) < 2:
            raise ValueError("Ingrese al menos 2 caracteres para la búsqueda.")    
        return limpio
    
    @classmethod
    def obtener_clima(cls, termino: str, dias : int) -> Tuple[List[clima], str]:
        termino_seguro = cls.sanitizar_termino(termino)
        if not isinstance(dias, int) or not 1 <= dias <= 14:
            return [], "La cantidad de días debe estar entre 1 y 14."
        if not REQUESTS_AVAILABLE:
            return cls._manejar_contingencia(
                termino_seguro, 
                "Librería 'requests' no instalada en el entorno."
            )
        headers = {
            "Accept": "application/json",
            "User-Agent": "EcoTechApp/1.0"}
        params = {
            "key": Settings.API_KEY_CLIMA,
            "q": termino_seguro,
            "days": dias,
            "lang": "es"}
        try:
            # Siempre se define un timeout explícito para que el software no se congele
            response = requests.get(
                Settings.API_CLIMA_URL,
                headers=headers,
                params=params,
                timeout=Settings.REQUEST_TIMEOUT
            )
            if response.status_code == 404:
                return ([], f"No se encontró la ubicación '{termino_seguro}'.")
            elif response.status_code == 401:
                return ([], "Error 401: Acceso no autorizado a la API externa.")
            elif response.status_code == 429:
                return ([], "Error 429: Límite de consultas a la API excedido.")
            
            response.raise_for_status()
            
            data = response.json()
            pronostico = data.get("forecast", {})
            resultado = pronostico.get("forecastday", [])
            pronosticos: List[clima] = []
            fecha_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for item in resultado:
                fecha = item.get("date","")
                dia = item.get("day",{})
                temperatura_max = dia.get("maxtemp_c")
                temperatura_min = dia.get("mintemp_c")
                humedad = dia.get("avghumidity")
                probabilidad_lluvia = dia.get("daily_chance_of_rain")
                condicion = dia.get("condition", {}).get("text", "")
                
                pronosticos.append(clima(
                    ubicacion= termino_seguro,
                    temperatura_minima=temperatura_min,
                    temperatura_maxima=temperatura_max,
                    humedad=humedad,
                    condicion=condicion,
                    probabilidad_lluvia=probabilidad_lluvia,
                    fecha_consulta=fecha_consulta,
                    fecha_pronostico=fecha
                ))
            return (pronosticos, f"Se obtuvieron {len(pronosticos)} pronósticos correctamente.")
        except requests.exceptions.Timeout:
            return cls._manejar_contingencia(
                termino_seguro, 
                f"El servicio tardó más de {Settings.REQUEST_TIMEOUT}s en responder (Timeout)."
            )
        except requests.exceptions.ConnectionError:
            return cls._manejar_contingencia(
                termino_seguro, 
                "No hay conexión a internet o el servidor externo está caído."
            )
        except requests.exceptions.RequestException as e:
            return cls._manejar_contingencia(termino_seguro, f"Falla en la petición: {str(e)}")
    
    @classmethod
    def _manejar_contingencia(cls, termino: str, causa_error: str) -> Tuple[List[clima], str]:
        """Gestiona los errores de conexión con el servicio meteorológico."""

        if not Settings.ENABLE_OFFLINE_FALLBACK:
            return ([], f"{causa_error} (El modo offline está deshabilitado).")

        return ([], f"{causa_error} No hay pronósticos locales disponibles.")
    
    @classmethod
    def probar_conectividad(cls) -> Tuple[bool, str]:
        """Verifica si la API externa está accesible."""
        if not REQUESTS_AVAILABLE:
            return (False, "Librería 'requests' no instalada. Ejecute 'pip install requests'.")
        
        try:
            resp = requests.get(
                Settings.API_CLIMA_URL,
                params={
                "key": Settings.API_KEY_CLIMA,
                "q": "Santiago",
                "days": 1
            },
                timeout=Settings.REQUEST_TIMEOUT
            )
            if resp.status_code in (200, 404):
                return (True, f"Conexión exitosa con {Settings.API_CLIMA_URL} (Código HTTP: {resp.status_code})")
            return (False, f"El servidor respondió con código HTTP: {resp.status_code}")
        except requests.exceptions.Timeout:
            return (False, "Timeout al contactar el servicio.")
        except requests.exceptions.ConnectionError:
             return (False, "Sin conexión de red hacia el servidor.")
        except Exception as e:
            return (False, f"Error de red: {str(e)}")