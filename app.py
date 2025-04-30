from src.procesador import EstadisticasComerciales, ProvinciaNoEncontrada

def main():
    archivo = "data/sri_ventas_2024.csv"
    estadisticas = EstadisticasComerciales(archivo)
    
    # Ventas totales por provincia
    print("Ventas totales por provincia:")
    ventas = estadisticas.calcular_ventas_por_provincia()
    for provincia, total in ventas.items():
        print(f"\t{provincia}: ${total:,.2f}")

    # Ventas de una provincia específica
    print("\nConsulta de ventas para una provincia:")
    provincia_input = input("\tIngrese el nombre de una provincia: ")
    try:
        total_ventas = estadisticas.obtener_ventas_de_provincia(provincia_input)
        print(f"\tVentas en {provincia_input}: ${total_ventas:,.2f}")
    except ProvinciaNoEncontrada as e:
        print(f"\t{e}")

    # Exportaciones totales por mes
    print("\nExportaciones totales por mes:")
    exportaciones = estadisticas.resumen_exportaciones_mensuales()
    for mes, total in exportaciones.items():
        print(f"\t{mes}: ${total:,.2f}")

    # Provincia con mayor importación
    print("\nProvincia con mayor volumen de importaciones:")
    provincia_max, total_importado = estadisticas.mayor_importadora()
    print(f"\tProvincia: {provincia_max} con ${total_importado:,.2f} en importaciones")

if __name__ == "__main__":
    main()
