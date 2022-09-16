# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

# Создаем экземпляры схем сериализации для одной и нескольких сущностей
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


# Функции API для жанров - /genres/
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        # Если результаты запроса - пустые - говорим что данные не найдены
        if not all_genres:
            return f'Результаты запроса не найдены', 404
        return genres_schema.dump(all_genres), 200


# Функции API для единичного экземпляра - жанра - /genres/<int:uid>
@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        try:
            genre = genre_service.get_one(uid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return f'Жанр по указанному id = {uid} не найден - {str(e)}', 404
