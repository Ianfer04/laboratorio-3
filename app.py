import os
from src.procesador import Analizador

def main():
    ruta_actual = os.path.dirname(__file__)
    archivo = os.path.join(ruta_actual, "datos", "sri_ventas_2024.csv")

    try:
        analizador = Analizador(archivo)

        print("\nVentas totales por provincia:")
        for prov, total in analizador.ventas_totales_por_provincia().items():
            print(f"  {prov}: ${total:,.2f}")

        print("\nPromedio de ventas por provincia:")
        for prov, promedio in analizador.promedio_ventas_por_provincia().items():
            print(f"  {prov}: ${promedio:,.2f} (promedio)")

        print("\nProvincia con mayor importación:")
        print(f"  {analizador.provincia_con_mayor_importacion()}")

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en {archivo}")
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()