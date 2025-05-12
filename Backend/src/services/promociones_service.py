from Backend.src.utils.file_utils import leer_json

RUTA_PROMOCIONES = 'src/data/promociones.json'

def obtener_promciones():
    promociones = leer_json(RUTA_PROMOCIONES)
    return promociones
