import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_numero_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertGreaterEqual(len(resumen), 20)

    def test_valores_numericos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        for total in resumen.values():
            self.assertIsInstance(total, float)
            self.assertGreaterEqual(total, 0)

    def test_retornar_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_provincia_existente(self):
        ventas = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertIsInstance(ventas, float)
        self.assertGreaterEqual(ventas, 0)

    def test_provincia_inexistente(self):
        ventas = self.analizador.ventas_por_provincia("PROVINCIA_INEXISTENTE")
        self.assertEqual(ventas, 0.0)

    def test_exportaciones_por_mes_diccionario(self):
        exportaciones = self.analizador.exportaciones_totales_por_mes()
        self.assertIsInstance(exportaciones, dict)

    def test_exportaciones_por_mes_valores_mayores_0(self):
        exportaciones = self.analizador.exportaciones_totales_por_mes()
        for mes, valor in exportaciones.items():
            self.assertIsInstance(mes, str)
            self.assertIsInstance(valor, float)
            self.assertGreaterEqual(valor, 0)

    def test_provincia_con_mayor_importacion(self):
        provincia = self.analizador.provincia_con_mayor_importacion()
        self.assertIsInstance(provincia, str)
        self.assertGreater(len(provincia), 0)

    # NUEVO TEST
    def test_promedio_ventas_por_provincia(self):
        """Prueba el cálculo del promedio de ventas por provincia"""
        resultado = self.analizador.promedio_ventas_por_provincia()
        
        # Verificación de estructura
        self.assertIsInstance(resultado, dict)
        self.assertGreater(len(resultado), 0)
        
        # Verificación de tipos y valores
        for provincia, promedio in resultado.items():
            self.assertIsInstance(provincia, str)
            self.assertIsInstance(promedio, float)
            self.assertGreaterEqual(promedio, 0)
        
        # Verificación de consistencia con datos brutos
        ventas_totales = self.analizador.ventas_totales_por_provincia()
        for provincia, promedio in resultado.items():
            self.assertLessEqual(promedio, ventas_totales[provincia])

if __name__ == '__main__':
    unittest.main()