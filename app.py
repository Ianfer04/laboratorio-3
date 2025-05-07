import os
from src.procesador import Analizador

def main():
    # Construye la ruta completa al archivo CSV sin importar desde dónde se ejecute
    ruta_actual = os.path.dirname(__file__)
    archivo = os.path.join(ruta_actual, "datos", "sri_ventas_2024.csv")

    try:
        analizador = Analizador(archivo)

        print("\nVentas totales por provincia:")
        resumen = analizador.ventas_totales_por_provincia()
        for prov, total in sorted(resumen.items(), key=lambda x: x[1], reverse=True):
            print(f"\t{prov}: ${total:,.2f}")

        print("\nVentas para una provincia:")
        provincia = input("\tIngrese el nombre de una provincia: ").strip()
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"\tVentas en {provincia.upper()}: ${ventas:,.2f}")

        print("\nExportaciones totales por mes:")
        exportaciones = analizador.exportaciones_totales_por_mes()
        for mes, total in exportaciones.items():
            print(f"\t{mes}: ${total:,.2f}")

        # Mostrar provincia con mayor importación (nueva funcionalidad)
        mayor_import = analizador.provincia_con_mayor_importacion()
        print(f"\nProvincia con mayor importación: {mayor_import}")

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en la ruta {archivo}")
    except Exception as e:
        print(f"❌ Se produjo un error inesperado: {str(e)}")

if __name__ == "__main__":
    main()