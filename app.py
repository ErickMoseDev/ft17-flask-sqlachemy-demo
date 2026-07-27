import os

from dotenv import load_dotenv
from flask import Flask, make_response, request, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from extensions import log
from models import db
from resources.auth import CheckSession, Login, Logout, Register
from resources.books import BookByID
from resources.users import UserByID, Users

# load env vars
load_dotenv()

# create an instance of the flask app
app = Flask(__name__)

# setup an instance of bcrypt
bcrypt = Bcrypt(app=app)

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


app.config["SESSION_COOKIE_SAMESITE"] = os.environ.get("SESSION_COOKIE_SAMESITE")
app.config["SESSION_COOKIE_SECURE"] = os.environ.get("SESSION_COOKIE_SECURE")
app.config["SESSION_COOKIE_HTTPONLY"] = os.environ.get("SESSION_COOKIE_HTTPONLY")


# add flask migrate
migrate = Migrate(app=app, db=db)

# setup cors
CORS_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "").split(",")
CORS(
    app,
    supports_credentials=True,
    origins=[origin.strip() for origin in CORS_ORIGINS if origin.strip()],
)

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


PUBLIC_ENDPOINTS = ["login", "register"]


@app.before_request
def check_if_authenticated():
    if not session.get("user_id") and request.endpoint not in PUBLIC_ENDPOINTS:
        response = {
            "status": 401,
            "message": "Not authenticated. Login to access resource",
        }

        return make_response(response, 401)


# list our resources
# auth resources
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(Logout, "/logout")
api.add_resource(CheckSession, "/check-session")


# user resources
api.add_resource(Users, "/users")
api.add_resource(UserByID, "/users/<int:id>")

# book resources
api.add_resource(BookByID, "/books/<int:id>")
