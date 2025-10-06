from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Конфигурация приложения для подключения к Postgres
    app.config['SECRET_KEY'] = '9148ea4ea6b1abf7811b49ea49fdb08d'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://username:password@amvera-karpova-masha1-cnpg-levitat-rw:5432/levitate'
    print("DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Конфигурация сессий
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True

    # Инициализация расширений с приложением
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)

    # Импорт моделей для создания таблиц
    with app.app_context():

        db.create_all()  # Создает таблицы (если их еще нет)

    # Импорт и регистрация blueprint'ов
    from app.routes import main
    app.register_blueprint(main)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
