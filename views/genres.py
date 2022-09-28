from dao.model.genres import GenreSchema
from implemented import genre_service
from flask_restx import Namespace, Resource

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        if not all_genres:
            return 'Ошибка', 404
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did):
        one_genre_by_id = genre_service.get_one(did)
        if not one_genre_by_id:
            return 'Ошибка', 404
        return genres_schema.dump(one_genre_by_id), 200
