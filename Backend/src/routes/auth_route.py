from flask import Blueprint, request, jsonify

login_bp = Blueprint('login_routes', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if usuario == 'unemi' and contrasena == 'web2025':
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401