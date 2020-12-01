from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from config import Config

db = SQLAlchemy()

def init_app():
  """Construct the core application."""
  app = Flask(__name__)

  db.init_app(app)

  seeder = FlaskSeeder()
  seeder.init_app(app, db)

  return app