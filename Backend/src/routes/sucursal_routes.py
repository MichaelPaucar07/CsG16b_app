from flask import Blueprint, jsonify
from Backend.src.services.sucursales_service import obtener_sucursales

sucursal_bp = Blueprint('sucursal_routes', __name__)

@sucursal_bp.route('/list/sucursales', methods=['GET'])
def listar_sucursal():
    sucursal_bp = obtener_sucursales()
    return jsonify(sucursal_bp)
