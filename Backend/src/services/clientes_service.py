from Backend.src.utils.file_utils import leer_json

RUTA_CLIENTES = 'src/data/clientes.json'

def obtener_clients():
    clientes = leer_json(RUTA_CLIENTES)
    return clientes
