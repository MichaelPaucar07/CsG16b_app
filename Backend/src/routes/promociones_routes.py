from flask import Blueprint, jsonify
from Backend.src.services.promociones_service import obtener_promciones

promocion_bp = Blueprint('promocion_routes', __name__)

@promocion_bp.route('/list/promociones', methods=['GET'])
def listar_promociones():
    promocion_bp = obtener_promciones()
    return jsonify(promocion_bp)
