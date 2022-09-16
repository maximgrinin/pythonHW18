# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

# Создаем экземпляры схем сериализации для одной и нескольких сущностей
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


# Функции API для режиссеров - /directors/
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        # Если результаты запроса - пустые - говорим что данные не найдены
        if not all_directors:
            return f'Результаты запроса не найдены', 404
        return directors_schema.dump(all_directors), 200


# Функции API для единичного экземпляра - режиссера - /directors/<int:uid>
@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        try:
            director = director_service.get_one(uid)
            return director_schema.dump(director), 200
        except Exception as e:
            return f'Режиссер по указанному id = {uid} не найден - {str(e)}', 404
