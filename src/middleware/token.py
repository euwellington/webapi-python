from functools import wraps

import jwt
from src.server.instance import server 
from flask import request


def token_required(self, ):
    @wraps(self)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Você precisa primeiro se autenticar!",
                "error": "Não autorizado"
            }, 401

        return self(*args, **kwargs)

    return decorated