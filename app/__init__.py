from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
# make an instance from flask class
app=Flask(__name__)

app.config.from_object(Config)
#db object that represent database
db=SQLAlchemy(app)
#object representing migration  engine
migrate=Migrate(app, db)

from app import views