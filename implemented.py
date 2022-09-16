# Файл для создания DAO и сервисов, чтобы импортировать их везде
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

# Создаем DAO и сервисы для сущности фильма
movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

# Создаем DAO и сервисы для сущности режиссера
director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

# Создаем DAO и сервисы для сущности жанра
genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
