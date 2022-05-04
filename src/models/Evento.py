from flask_restx import fields
from src.server.instance import server

eventos = server.api.models('Evento', {
    'id': fields.String(description='Id od registro'),
    'equipamento': fields.String()
})