from flask_restx import Namespace, Resource
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('')
class MoviesView(Resource):
    def get(self):
        return '', 200

    def post(self):
        return '', 200

    def put(self):
        return '', 200

    def patch(self):
        return '', 200


@movie_ns.route('<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return '', 200
