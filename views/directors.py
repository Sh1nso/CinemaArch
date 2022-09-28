from dao.model.directors import DirectorSchema
from implemented import director_service
from flask_restx import Namespace, Resource

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_genres = director_service.get_all()
        if not all_genres:
            return 'Ошибка', 404
        return directors_schema.dump(all_genres), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, gid):
        one_genre_by_id = director_service.get_one(gid)
        if not one_genre_by_id:
            return 'Ошибка', 404
        return director_schema.dump(one_genre_by_id), 200
