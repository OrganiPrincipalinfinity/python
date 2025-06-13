from .usuarios import usuarios_bp
from .productos import productos_bp
from .documentacion import documentacion_bp

def registrar_rutas(app):
    app.register_blueprint(usuarios_bp, url_prefix  ='/usuarios')
    app.register_blueprint(productos_bp, url_prefix ='/productos')
    app.register_blueprint(documentacion_bp, url_prefix ='/documentacion')
