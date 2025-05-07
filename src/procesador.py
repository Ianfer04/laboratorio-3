import csv
from collections import defaultdict

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        datos = []
        with open(self.archivo_csv, newline='', encoding='latin1') as csvfile:
            lector = csv.DictReader(csvfile, delimiter=';')
            print("Columnas encontradas:", lector.fieldnames)
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        resumen = defaultdict(float)
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            try:
                ventas = float(fila['TOTAL_VENTAS'].replace(',', '.'))
            except (ValueError, KeyError):
                ventas = 0.0
            resumen[provincia] += ventas
        return resumen

    def ventas_por_provincia(self, nombre):
        nombre = nombre.strip().upper()
        resumen = self.ventas_totales_por_provincia()
        return resumen.get(nombre, 0.0)
    
    def exportaciones_totales_por_mes(self):
        exportaciones_por_mes = defaultdict(float)
        
        for fila in self.datos:
            mes = fila['MES']
            valor_str = fila.get('EXPORTACIONES', '0').strip()

            try:
                exportacion = float(valor_str.replace(',', '.'))
            except ValueError:
                exportacion = 0.0

            exportaciones_por_mes[mes] += exportacion
            
        return exportaciones_por_mes

    def provincia_con_mayor_importacion(self):
        importaciones_por_provincia = defaultdict(float)
        
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            valor_str = fila.get('IMPORTACIONES', '0').strip()

            try:
                importacion = float(valor_str.replace(',', '.'))
            except ValueError:
                importacion = 0.0

            importaciones_por_provincia[provincia] += importacion
        
        if not importaciones_por_provincia:
            return ""
            
        return max(importaciones_por_provincia.items(), key=lambda x: x[1])[0]