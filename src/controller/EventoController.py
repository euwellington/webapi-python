from distutils.command.config import config
from flask import jsonify, request
from flask_cors import cross_origin
from flask_restx import Api, Resource
from src.middleware.token import token_required
from src.server.instance import server
from src.services.EventoService import EventoService
# from src.models.Evento import eventos


app, api = server.app, server.api

@api.route('/eventos')
class EventoController(Resource):
    # @api.marshal_list_with(eventos)
    @token_required
    def get(self, ):
        try:
            res = EventoService.listarTodosEventos()
            return res
            
        except Exception as e:
            return e
