
import requests

API_CLIMA_URL = "https://api.weatherapi.com/v1/forecast.json"
API_KEY_CLIMA = "8e58a40b39b74d2aa36152341260911"
REQUEST_TIMEOUT = 5

params = {
    "key": API_KEY_CLIMA,
    "q": "Concepcion,Chile",
    "days": 14,
    "lang": "es"
}

try:
    respuesta = requests.get(
        API_CLIMA_URL,
        params=params,
        timeout=REQUEST_TIMEOUT
    )

    respuesta.raise_for_status()
    datos = respuesta.json()

    pronosticos = datos["forecast"]["forecastday"]

    print("\n===== PRONÓSTICO DE 14 DÍAS =====")
    print(f"Ciudad: {datos['location']['name']}")
    print(f"Días recibidos: {len(pronosticos)}")

    for dia in pronosticos:
        clima = dia["day"]

        print(f"\nFecha: {dia['date']}")
        print(f"Temperatura máxima: {clima['maxtemp_c']} °C")
        print(f"Temperatura mínima: {clima['mintemp_c']} °C")
        print(f"Temperatura promedio: {clima['avgtemp_c']} °C")
        print(f"Humedad: {clima['avghumidity']}%")
        print(f"Condición: {clima['condition']['text']}")
        print(f"Probabilidad de lluvia: {clima['daily_chance_of_rain']}%")
        print("-" * 40)

    if len(pronosticos) == 14:
        print("\n¡ÉXITO! Se recibieron los 14 días.")
    else:
        print(f"\nSe recibieron {len(pronosticos)} días, no 14.")

except requests.exceptions.HTTPError:
    print("Error HTTP:", respuesta.status_code)
    print(respuesta.text)

except requests.exceptions.Timeout:
    print("La solicitud superó el tiempo de espera.")

except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)

except (KeyError, ValueError) as e:
    print("Error procesando los datos:", e)
