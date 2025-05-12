from flask import Blueprint, jsonify
from Backend.src.services.empleados_service import obtener_empleados

empleado_bp = Blueprint('empleado_routes', __name__)

@empleado_bp.route('/list/employes', methods=['GET'])
def listar_empleados():
    empleados = obtener_empleados()
    return jsonify(empleados)
