from flask import make_response
from flask_restful import Resource
from models import db, User
from schemas import users_schema, user_schema


# /users route
class Users(Resource):
    def get(self):
        users = User.query.all()
        return make_response(users_schema.dump(users), 200)


# /users/<int:id>
class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        if user:
            return make_response(user_schema.dump(user), 200)
        else:
            response = {"status": 404, "message": "user not found"}

            return make_response(response, 404)

    def delete(self, id):
        user = User.query.filter_by(id=id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            response = {"message": "user deleted successfully"}

            return make_response(response, 200)

        else:
            response = {"status": 404, "message": "user not found"}

            return make_response(response, 404)


# cascade - all, delete-orphan
