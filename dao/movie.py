from dao.model.movies import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_query(self):
        return self.session.query(Movie)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_all_by_genre_id(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_all_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

        return ''
