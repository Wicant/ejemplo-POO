from services.clima_services import ClimaServices 



class ClimaView:

    @staticmethod
    def consultar_clima(ubicacion: str):
        print("\n--- PRONÓSTICOS OBTENIDOS ---")

        if not ubicacion:
            print("Debe ingresar una ubicación.")
            return

        dias = input("¿Cuántos días de pronóstico desea consultar?: ")

        if not dias.isdigit() or not 1 <= int(dias) <= 14:
            print("Ingrese una cantidad de días entre 1 y 14.")
            return

        print(f"\nConsultando pronóstico para {ubicacion}...")

        pronosticos, mensaje = ClimaServices.obtener_clima(
            ubicacion,
            int(dias)
        )

        print(f"\n{mensaje}")

        if not pronosticos:
            return

        print("\n--- PRONÓSTICOS OBTENIDOS ---")

        for p in pronosticos:
            print(
            f"\n========== PRONÓSTICO DEL {p.fecha_pronostico} ==========\n"
            f"\nUbicación: {p.ubicacion}"
            f"\nCondición: {p.condicion}"
            f"\n\nTemperatura:"
            f"\n  Mínima: {p.temperatura_minima} °C"
            f"\n  Máxima: {p.temperatura_maxima} °C"
            f"\n\nHumedad: {p.humedad}%"
            f"\nProbabilidad de lluvia: {p.probabilidad_lluvia}%"
            f"\n======================================================"
            )