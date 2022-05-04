from flask_restx import Api, Resource
from flask import jsonify
import pymysql
from src.server.instance import server
from src.database.config import mysql
from src.repository.script.EventoScript import script

class EventoService(Resource):
 
    def listarTodosEventos():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(script.getAll())
            empRows = cursor.fetchall()
            respone = jsonify(empRows)
            respone.status_code = 200
            return respone
        except Exception as e:
            e
        finally:
            cursor.close() 
            conn.close()
