from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
import threading

db = SQLAlchemy()

ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    ma.init_app(app)
    
    return app


lock = threading.Lock()


app = create_app()
app.app_context().push()

socketio = SocketIO(app, cors_allowed_origins="*")

from src.routes import inital_routes, korisnik_routes, narudzbina_routes, stavka_narudzbine_routes, lek_routes, zapakovan_lek_routes
from src import video_communication