# Analizador de Datos SRI 2024

Este proyecto permite analizar datos de ventas, exportaciones e importaciones por provincia y mes a partir de un archivo CSV del SRI (Ecuador).

## Estructura del Proyecto

```
📦 LABORATORIO-3/
├── datos/
│   └── sri_ventas_2024.csv
├── src/
│   └── procesador.py
├── tests/
│   └── test_analizador.py
├── venv/
│   └── ... (entorno virtual)
├── app.py
└── .gitignore
```

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://tu-repo.git
   cd LABORATORIO-3
   ```

2. Activa el entorno virtual si lo estás usando:
   ```bash
   # En Windows
   venv\Scripts\activate

   # En macOS/Linux
   source venv/bin/activate
   ```

3. Asegúrate de tener el archivo `sri_ventas_2024.csv` en la carpeta `datos`.

## Uso

Ejecuta la aplicación desde la terminal:

```bash
python app.py
```

## Pruebas

Para correr los tests:

```bash
python -m unittest tests/test_analizador.py
```

## Funcionalidades

- Mostrar ventas totales por provincia
- Consultar ventas de una provincia específica
- Ver exportaciones totales por mes
- Identificar la provincia con mayor importación

## Autor

Ian Dueñas
