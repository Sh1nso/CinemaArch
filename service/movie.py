from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_query(self):
        return self.dao.get_query()

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, mid):
        return self.dao.get_one_by_id(mid)

    def get_all_by_director_id(self, did):
        return self.dao.get_all_by_director_id(did)

    def get_all_by_genre_id(self, gid):
        return self.dao.get_all_by_genre_id(gid)

    def get_all_by_year(self, year):
        return self.dao.get_all_by_year(year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one_by_id(mid)
        movie.year = data.get('year')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, mid):
        movie = self.get_one_by_id(mid)
        self.dao.delete(movie)
