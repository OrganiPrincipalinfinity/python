import jwt
from flask import request, jsonify, current_app
from functools import wraps

def token_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            partes = request.headers['Authorization'].split()
            if len(partes) == 2 and partes[0] == 'Bearer':
                token = partes[1]

        if not token:
            return jsonify({'mensaje': 'Token requerido'}), 401

        try:
            datos = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            request.user = datos
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorador
