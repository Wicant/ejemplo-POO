import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path, override=True)
    print("Ruta del .env:", env_path)
    print("¿Existe el .env?:", env_path.exists())
    print("¿Se cargó API_CLIMA_URL?:", bool(os.getenv("API_CLIMA_URL")))
    print("¿Se cargó API_KEY_CLIMA?:", bool(os.getenv("API_KEY_CLIMA")))
except ImportError:
    pass

class Settings:
    """
    Centraliza las variables de configuración del sistema.
    Evita exponer credenciales hardcodeadas en el código fuente.
    """
    API_CLIMA_URL: str = os.getenv("API_CLIMA_URL", "https://api.weatherapi.com/v1/forecast.json")
    API_KEY_CLIMA: str = os.getenv("API_KEY_CLIMA", "")
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "5"))
    ENABLE_OFFLINE_FALLBACK: bool = os.getenv("ENABLE_OFFLINE_FALLBACK", "True").lower() in ("true", "1", "yes")
    
    # Parámetros para inicio de sesión y semilla de usuario administrador
    ADMIN_INITIAL_USER: str = os.getenv("ADMIN_INITIAL_USER", "")
    ADMIN_INITIAL_CLAVE: str = os.getenv("ADMIN_INITIAL_CLAVE", "")
    MAX_LOGIN_ATTEMPTS: int = int(os.getenv("MAX_LOGIN_ATTEMPTS", "3"))
    # Datos del empleado administrador inicial
    ADMIN_INITIAL_RUT: str = os.getenv("ADMIN_INITIAL_RUT", "")
    ADMIN_INITIAL_NOMBRE: str = os.getenv("ADMIN_INITIAL_NOMBRE", "")
    ADMIN_INITIAL_DIRECCION: str = os.getenv("ADMIN_INITIAL_DIRECCION", "")
    ADMIN_INITIAL_TELEFONO: str = os.getenv("ADMIN_INITIAL_TELEFONO", "")
    ADMIN_INITIAL_CORREO: str = os.getenv("ADMIN_INITIAL_CORREO", "")

print("URL desde Settings:", Settings.API_CLIMA_URL)
print("¿Clave desde Settings?:", bool(Settings.API_KEY_CLIMA))