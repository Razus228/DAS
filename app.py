from flask import Flask
from modules.database import db
from modules.User import User
from modules.message import message
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    # Configure SQLAlchemy to use SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    import routes
    app.run(host='127.0.0.2')
