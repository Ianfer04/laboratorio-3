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
        return dict(resumen)

    def ventas_por_provincia(self, nombre):
        nombre = nombre.strip().upper()
        resumen = self.ventas_totales_por_provincia()
        return resumen.get(nombre, 0.0)
    
    def exportaciones_totales_por_mes(self):
        exportaciones = defaultdict(float)
        for fila in self.datos:
            mes = fila['MES']
            try:
                valor = float(fila['EXPORTACIONES'].replace(',', '.'))
            except (ValueError, KeyError):
                valor = 0.0
            exportaciones[mes] += valor
        return dict(exportaciones)

    def porcentaje_ventas_tarifa_cero(self, agrupacion='PROVINCIA'):
        resultados = defaultdict(lambda: {'ventas_0': 0.0, 'total': 0.0})
        
        for fila in self.datos:
            grupo = fila[agrupacion]
            try:
                ventas_0 = float(fila['VENTAS_NETAS_TARIFA_0'].replace(',', '.'))
                ventas_totales = float(fila['TOTAL_VENTAS'].replace(',', '.'))
            except (ValueError, KeyError):
                continue
                
            resultados[grupo]['ventas_0'] += ventas_0
            resultados[grupo]['total'] += ventas_totales
        
        porcentajes = {}
        for grupo, valores in resultados.items():
            if valores['total'] > 0:
                porcentajes[grupo] = (valores['ventas_0'] / valores['total']) * 100
            else:
                porcentajes[grupo] = 0.0
                
        return porcentajes

    def provincia_con_mayor_importacion(self):
        importaciones = defaultdict(float)
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            try:
                valor = float(fila['IMPORTACIONES'].replace(',', '.'))
            except (ValueError, KeyError):
                valor = 0.0
            importaciones[provincia] += valor
            
        return max(importaciones.items(), key=lambda x: x[1])[0] if importaciones else None

    # NUEVA FUNCIÓN
    def promedio_ventas_por_provincia(self):
        """Calcula el promedio de ventas para cada provincia"""
        contador = defaultdict(int)
        totales = defaultdict(float)
        
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            try:
                venta = float(fila['TOTAL_VENTAS'].replace(',', '.'))
            except (ValueError, KeyError):
                venta = 0.0
            
            totales[provincia] += venta
            contador[provincia] += 1
        
        return {prov: totales[prov]/contador[prov] for prov in totales}