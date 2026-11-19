from config.settings import Settings
from models.moneda import Moneda
from datetime import date, timedelta
from models.cotizacionMonedaDAO import CotizacionMonedaDAO

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

class MonedaServices:
    @classmethod
    def obtener_moneda(cls, codigo: str):
        if not REQUESTS_AVAILABLE:
            return cls._manejar_contingencia(
                codigo,
                "Librería 'requests' no instalada en el entorno."
    )

        headers = {
            "Accept": "application/json",
            "User-Agent": "EcoTechApp/1.0"
            }
        fecha_actual = date.today()
        fecha_inicio = fecha_actual - timedelta(days=10)
        params = {
            "token": Settings.API_KEY_MONEDA,
            "function": "GetSeries",
            "timeseries": codigo,
            "firstdate": fecha_inicio.isoformat(),
            "lastdate": fecha_actual.isoformat()
        }

        try:
            # Siempre se define un timeout explícito para que el software no se congele
            response = requests.get(
                Settings.API_MONEDA_URL,
                headers=headers,
                params=params,
                timeout=Settings.REQUEST_TIMEOUT_MONEDA
                )
            if response.status_code == 404:
                return None, "No se encontró la Moneda"
            elif response.status_code == 401:
                return cls._manejar_contingencia(
                    codigo,
                    "Error 401: Acceso no autorizado a la API externa."
                )

            elif response.status_code == 429:
                return cls._manejar_contingencia(
                    codigo,
                    "Error 429: Límite de consultas a la API excedido."
                )

            response.raise_for_status()
                
            data = response.json()
            series = data.get("Series", {})
            resultado = series.get("Obs",[])
            if not resultado:
                return None, "No se encontraron datos para la moneda solicitada."
            
            for item in resultado:
                valor = item.get("value")
                fecha = item.get("indexDateString")
            valor = float(valor)
            if codigo == "F073.TCO.PRE.Z.D":
                nombre = "Dólar estadounidense"
                simbolo = "USD"

            elif codigo == "F072.CLP.EUR.N.O.D":
                nombre = "Euro"
                simbolo = "EUR"

            else:
                return None, "Código de moneda no reconocido."
                
            moneda = Moneda(
                nombre = nombre,
                codigo = codigo,
                simbolo = simbolo,
                valor = valor,
                fecha = fecha
            )
            return moneda, None
        except requests.exceptions.Timeout:
            return cls._manejar_contingencia(
                codigo,
                f"El servicio tardó más de {Settings.REQUEST_TIMEOUT_MONEDA}s en responder (Timeout)."
            )

        except requests.exceptions.ConnectionError:
            return cls._manejar_contingencia(
                codigo,
                "No hay conexión a internet o el servidor del Banco Central está caído."
            )

        except requests.exceptions.RequestException as e:
            return cls._manejar_contingencia(
                codigo,
                f"Falla en la petición: {str(e)}"
            )

    @classmethod
    def _manejar_contingencia(cls, codigo: str, causa_error: str):
        if not Settings.ENABLE_OFFLINE_FALLBACK:
            return None, f"{causa_error} (El modo offline está deshabilitado)."

        if codigo == "F073.TCO.PRE.Z.D":
            simbolo = "USD"
            nombre = "Dólar estadounidense"

        elif codigo == "F072.CLP.EUR.N.O.D":
            simbolo = "EUR"
            nombre = "Euro"

        else:
            return None, "Código de moneda no reconocido."

        cotizaciones = CotizacionMonedaDAO.obtener_por_moneda(simbolo)

        if not cotizaciones:
            return None, (
                f"{causa_error}\n"
                "No existen cotizaciones guardadas para utilizar como respaldo."
            )

        ultima = cotizaciones[0]

        moneda = Moneda(
            nombre=nombre,
            codigo=codigo,
            simbolo=simbolo,
            valor=ultima.valor,
            fecha=ultima.fecha_cotizacion.isoformat()
        )

        mensaje = (
            f"[MODO CONTINGENCIA] {causa_error}\n"
            f"Se utilizó la última cotización guardada: "
            f"{ultima.fecha_cotizacion}."
        )

        return moneda, mensaje