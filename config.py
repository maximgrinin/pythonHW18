# Это файл конфигурации приложения, здесь может храниться путь к бд, ключ шифрования, что-то еще.

# Класс с параметрами конфигурации приложения
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
