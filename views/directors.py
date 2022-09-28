from setup_db import db
from flask_restx import Namespace, Resource

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return '', 200


@director_ns.route('<int:did>')
class DirectorsView(Resource):
    def get(self, id):
        return '', 200
