import csv

class ProvinciaNoEncontrada(Exception):
    """Excepción personalizada para provincias no encontradas en los datos."""
    def __init__(self, nombre_provincia):
        self.nombre_provincia = nombre_provincia
        mensaje = f"No se encontró la provincia '{nombre_provincia}' en el conjunto de datos."
        super().__init__(mensaje)

class EstadisticasComerciales:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.registros = self._cargar_datos()

    def _cargar_datos(self):
        """Carga los datos desde el archivo CSV, omitiendo las provincias 'ND'."""
        registros = []
        with open(self.ruta_csv, mode='r', encoding='ISO-8859-1') as archivo:
            lector = csv.DictReader(archivo)
            for linea in lector:
                if linea.get('PROVINCIA') != 'ND':
                    registros.append(linea)
        return registros

    def calcular_ventas_por_provincia(self):
        """Devuelve un diccionario con la suma de ventas por provincia."""
        resumen_ventas = {}
        for item in self.registros:
            prov = item['PROVINCIA'].strip().upper()
            total = float(item['TOTAL_VENTAS'])
            resumen_ventas[prov] = resumen_ventas.get(prov, 0) + total
        return resumen_ventas

    def obtener_ventas_de_provincia(self, provincia):
        """Devuelve el total de ventas de una provincia específica."""
        ventas = self.calcular_ventas_por_provincia()
        clave = provincia.strip().upper()
        if clave not in ventas:
            raise ProvinciaNoEncontrada(provincia)
        return ventas[clave]

    def resumen_exportaciones_mensuales(self):
        """Devuelve un diccionario con el total de exportaciones por mes."""
        exportaciones = {}
        for item in self.registros:
            mes = item['MES']
            monto = float(item['EXPORTACIONES']) if item['EXPORTACIONES'] else 0.0
            exportaciones[mes] = exportaciones.get(mes, 0) + monto
        return exportaciones

    def mayor_importadora(self):
        """Devuelve la provincia con el mayor total de importaciones."""
        importaciones = {}
        for item in self.registros:
            prov = item['PROVINCIA']
            monto = float(item['IMPORTACIONES']) if item['IMPORTACIONES'] else 0.0
            importaciones[prov] = importaciones.get(prov, 0) + monto

        if not importaciones:
            raise ValueError("No hay registros de importaciones.")

        provincia_top = max(importaciones, key=importaciones.get)
        return provincia_top, importaciones[provincia_top]
