from flask import Flask, request
from models import db
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_restful import Api
from extensions import log

from resources.users import Users, UserByID
from resources.books import BookByID

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

api = Api(app=app)


# configure my logger to run before requests
@app.before_request
def log_request():
    log.info(
        "request",
        method=request.method,
        content_type=request.headers.get("Content-Type"),
    )


# list our resources
# user resources
api.add_resource(Users, "/users")
api.add_resource(UserByID, "/users/<int:id>")

# book resources
api.add_resource(BookByID, "/books/<int:id>")
