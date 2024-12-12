from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# PEERUBAHAN NAMA DARI models.py menjadi modelele.py & todo.py menjadi todos_modelele.py
from app import routes
from app.modelele import model, todos_modelele