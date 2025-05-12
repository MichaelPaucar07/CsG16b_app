from flask import Blueprint, jsonify
from Backend.src.services.productos_service import obtener_productos

producto_bp = Blueprint('producto_routes', __name__)

@producto_bp.route('/list/products', methods=['GET'])
def listar_productos():
    promocion_bp = obtener_productos()
    return jsonify(promocion_bp)
