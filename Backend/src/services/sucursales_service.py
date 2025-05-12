from Backend.src.utils.file_utils import leer_json

RUTA_SUCURSALES = 'src/data/sucursales.json'

def obtener_sucursales():
    sucursales = leer_json(RUTA_SUCURSALES)
    return sucursales