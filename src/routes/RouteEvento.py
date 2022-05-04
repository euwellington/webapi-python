from src.setup import app
from src.database.config import mysql
from flask import jsonify, request
from src.controller.EventoController import EventoController

class RouteEvento:
    def getAllEvent():
        @app.get('/evento')
        def getAll():
            return EventoController.getAll()
