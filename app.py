from flask import Flask
from models import db
from flask_migrate import Migrate
from dotenv import load_dotenv

# load env vars
load_dotenv()

# create an instance of the flask app
app = Flask(__name__)

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"

# add flask migrate

migrate = Migrate(app=app, db=db)

# initialize app to use sqlalchemy
db.init_app(app=app)
