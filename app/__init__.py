from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9148ea4ea6b1abf7811b49ea49fdb08d'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:marukarp123@amvera-karpova-masha1-cnpg-levitat-rw:5432/levitate'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)

    return app
