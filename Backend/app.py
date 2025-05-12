from flask import Flask
from flask_cors import CORS
from Backend.src.routes.empleado_routes import empleado_bp
from Backend.src.routes.cliente_route import cliente_routes
from Backend.src.routes.promociones_routes import promocion_bp
from Backend.src.routes.producto_routes import producto_bp
from Backend.src.routes.sucursal_routes import sucursal_bp
from Backend.src.routes.auth_route import login_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(empleado_bp,url_prefix='/api')
app.register_blueprint(cliente_routes,url_prefix='/api')
app.register_blueprint(promocion_bp,url_prefix='/api')
app.register_blueprint(producto_bp,url_prefix='/api')
app.register_blueprint(sucursal_bp,url_prefix='/api')
app.register_blueprint(login_bp,url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)