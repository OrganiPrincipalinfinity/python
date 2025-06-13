from flask import Blueprint, request, jsonify, current_app

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def listar_productos():
    cursor = current_app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    return jsonify(productos)

@productos_bp.route('/', methods=['POST'])
def crear_producto():
    datos = request.get_json()
    nombre = datos.get('nombre')
    precio = datos.get('precio')

    cursor = current_app.mysql.connection.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
    current_app.mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Producto creado"}), 201
