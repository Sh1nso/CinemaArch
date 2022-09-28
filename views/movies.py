from flask import request
from flask_restx import Namespace, Resource
from dao.model.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        data = movie_service.get_query()
        if director_id is not None:
            data = movie_service.get_all_by_director_id(director_id)
        if genre_id is not None:
            data = movie_service.get_all_by_genre_id(genre_id)
        if year is not None:
            data = movie_service.get_all_by_year(year)
        all_movies = data.all()
        if not all_movies:
            return 'Ошибка', 404
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return movie_schema.dump(movie), 201


@movie_ns.route('<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one_by_id(mid)
        if not movie:
            return 'Ошибка', 404
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update(req_json)
        if not movie:
            return 'Ошибка', 404
        return movie_schema.dump(movie), 204

    def delete(self, mid: int):
        if not movie_service.get_one_by_id(mid):
            return 'Ошибка', 404
        movie_service.delete(mid)
        return '', 204
