import pandas as pd
import requests
import io

# Configuración de Ciencia Abierta: Carga desde Zenodo (DOI: 10.5281/zenodo.18911986)
print("Accediendo al repositorio de datos en Zenodo...")
url = "https://zenodo.org/records/18911986/files/datos_raw.csv?download=1"

try:
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))
    print("Datos cargados exitosamente desde la nube.")
    print(f"Resumen del dataset: {df.shape[0]} filas y {df.shape[1]} columnas.")
    print(df.head())
except Exception as e:
    print(f"Error al conectar con Zenodo: {e}")
