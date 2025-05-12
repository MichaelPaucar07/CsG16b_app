from Backend.src.utils.file_utils import leer_json

RUTA_EMPLEADOS = 'src/data/empleados.json'

def obtener_empleados():
    empleados = leer_json(RUTA_EMPLEADOS)
    return empleados
