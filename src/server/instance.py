import os
from flask import Flask
from flask_restx import Api

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
port = int(os.environ.get("PORT", 5000))
class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='WEB API',
            description='TESTE API',
            security='Bearer Auth',
            authorizations=authorizations
            # doc='/docs'
        )

    def run(self):
        self.app.run(
            debug=True,
            host='0.0.0.0',
            port=port
        )

server = Server()