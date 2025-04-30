import unittest
from src.procesador import EstadisticasComerciales, ProvinciaNoEncontrada

class TestEstadisticasComerciales(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.estadisticas = EstadisticasComerciales("data/sri_ventas_2024.csv")
    
    def test_calcular_ventas_retornan_diccionario(self):
        resultado = cls.estadisticas.calcular_ventas_por_provincia()
        self.assertIsInstance(resultado, dict)

    def test_total_provincias_sin_nd(self):
        resumen = cls.estadisticas.calcular_ventas_por_provincia()
        self.assertEqual(len(resumen), 24)  # Suponiendo que hay 24 provincias válidas

    def test_ventas_mayores_a_5000(self):
        resumen = cls.estadisticas.calcular_ventas_por_provincia()
        self.assertTrue(all(float(valor) > 5000 for valor in resumen.values()))

    def test_provincia_inexistente_lanza_excepcion(self):
        with self.assertRaises(ProvinciaNoEncontrada):
            cls.estadisticas.obtener_ventas_de_provincia("Narnia")

    def test_ventas_provincia_case_insensitive(self):
        mayus = cls.estadisticas.obtener_ventas_de_provincia("PICHINCHA")
        minus = cls.estadisticas.obtener_ventas_de_provincia("pichincha")
        self.assertEqual(mayus, minus)

    def test_exportaciones_formato_valido(self):
        exportaciones = cls.estadisticas.resumen_exportaciones_mensuales()
        self.assertIsInstance(exportaciones, dict)
        self.assertTrue(all(float(valor) >= 0 for valor in exportaciones.values()))

    def test_provincia_mayor_importacion_valida(self):
        provincia, monto = cls.estadisticas.mayor_importadora()
        self.assertIsInstance(provincia, str)
        self.assertIsInstance(monto, float)
        self.assertGreater(monto, 0)
