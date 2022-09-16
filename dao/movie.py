# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным.
# Здесь в методах можно построить сложные запросы к БД.
from sqlalchemy import sql
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_all(self, args=None):
        if args is None:
            args = {}
        where_clause = []
        for key, value in args.items():
            where_clause.append(f'movie.{key} = {value}')
        if where_clause:
            query = sql.text("%s" % " and ".join(where_clause))
            return self.session.query(Movie).filter(query).all()
        return self.session.query(Movie).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
