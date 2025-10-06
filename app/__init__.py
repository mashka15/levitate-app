from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Секретный ключ для сессий и безопасности
    app.config['SECRET_KEY'] = '9148ea4ea6b1abf7811b49ea49fdb08d'

    # Строка подключения к базе данных PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql+psycopg2://mashakarpova1511:marukarp123@localhost:5432/levitate'
    )

    # Отключение слежения за изменениями для экономии ресурсов
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений базы данных и миграций
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрируем основные маршруты из блюпринта
    from .routes import main
    app.register_blueprint(main)

    return app
