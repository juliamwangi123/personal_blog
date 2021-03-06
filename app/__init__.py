from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
from flask_login import LoginManager
# make an instance from flask class
app=Flask(__name__)

app.config.from_object(Config)
#db object that represent database
db=SQLAlchemy(app)
#object representing migration  engine
migrate=Migrate(app, db)

login=LoginManager(app)
login.login_view = 'login'


from app import views,models