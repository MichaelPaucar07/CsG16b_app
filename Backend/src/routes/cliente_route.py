from flask import Blueprint, jsonify
from Backend.src.services.clientes_service import obtener_clients

cliente_routes = Blueprint('cliente_routes', __name__)

@cliente_routes.route('/list/clients', methods=['GET'])
def listar_clientes():
    clientes = obtener_clients()
    return jsonify(clientes)
