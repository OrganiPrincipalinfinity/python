from flask import Blueprint, request, jsonify, current_app
from auth import token_requerido
import jwt

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/login', methods=['POST'])
def login():
    datos = request.json
    usuario = datos['usuario']
    password = datos['password']

    if usuario !="admin" and password!="123":
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

    token = jwt.encode({
        'usuario': usuario,
        'password': password
    }, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token})

 
@usuarios_bp.route('/', methods=['GET'])
@token_requerido
def listar_usuarios():
    cursor = current_app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify(usuarios)

@usuarios_bp.route('/', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    email = datos.get('email')

    cursor = current_app.mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
    current_app.mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Usuario creado"}), 201
