import re
from config import Settings
from models.moneda import moneda
monedas = []
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

class MonedaServices:
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

    @staticmethod
    def _manejar_contingencia(termino: str, mensaje: str):
        return [], f"{mensaje} (búsqueda: '{termino}')"

    @classmethod
    def obtener_moneda(cls, termino: str):
        termino_seguro = cls.sanitizar_termino(termino)
        if not REQUESTS_AVAILABLE:
            return cls._manejar_contingencia(
                termino_seguro,
                "Librería 'requests' no instalada en el entorno."
            )

        headers = {
            "Accept": "application/json",
            "User-Agent": "EcoTechApp/1.0"
        }
        params = {
            "key": Settings.API_KEY_MONEDA,
            "q": termino_seguro,
            "lang": "es"
        }

        try:
            # Siempre se define un timeout explícito para que el software no se congele
            response = requests.get(
                Settings.API_MONEDA_URL,
                headers=headers,
                params=params,
                timeout=Settings.REQUEST_TIMEOUT
            )
            if response.status_code == 404:
                return [], f"No se encontró la moneda '{termino_seguro}'."
            if response.status_code == 401:
                return [], f"Error de autenticación con la API de moneda."
            response.raise_for_status()
            data = response.json()
            resultados = data.get("results", [])
            monedas_obtenidas = [moneda(**item) for item in resultados]
            return monedas_obtenidas, f'Se encontraron {len(monedas_obtenidas)} resultados para la moneda "{termino_seguro}".'
        except requests.exceptions.RequestException as e:
            return [], f"Error al obtener datos de la API de moneda: {e}"
        