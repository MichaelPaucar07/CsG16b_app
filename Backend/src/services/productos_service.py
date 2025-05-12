from Backend.src.utils.file_utils import leer_json

RUTA_PRODUCTOS = 'src/data/productos.json'

def obtener_productos():
    productos = leer_json(RUTA_PRODUCTOS)
    return productos
