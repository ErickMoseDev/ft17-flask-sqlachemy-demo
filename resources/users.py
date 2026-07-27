from flask import make_response, request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from extensions import log
from models import User, db
from schemas import user_schema, users_schema


# /users route
class Users(Resource):
    def get(self):
        users = User.query.all()

        log.info("get_all_users", request_data=users_schema.dump(users))
        return make_response(users_schema.dump(users), 200)

    def post(self):
        # if you are going to mutate your db, wrap your code in a try/except block

        try:
            data = request.get_json()

            # validate and deserialize input
            validated_data = user_schema.load(data)

            # check for duplicates of email and phone before inserting
            # if User.query.filter_by(
            #     email_address=validated_data["email_address"]
            # ).first():
            #     return make_response(
            #         {"status": 409, "message": "Email address already taken"}, 409
            #     )
            # if User.query.filter_by(phone=validated_data["phone"]).first():
            #     return make_response(
            #         {"status": 409, "message": "Phone number already taken"}, 409
            #     )

            # create user instance
            user = User(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email_address=validated_data["email_address"],
                phone=validated_data["phone"],
            )

            db.session.add(user)
            db.session.commit()

            return make_response(user_schema.dump(user), 201)

        except ValidationError as err:
            log.error("validation_error", errors=err.messages)
            response = {
                "status": 400,
                "message": "Validation error(s) occured",
                "errors": {**err.messages},
            }

            return make_response(response, 400)

        except IntegrityError as ie:
            db.session.rollback()  # rollback the db to the previous state incase of an integrity error
            log.error(
                "integrity_error", error=str(ie)
            )  # this displays the stack error messagges server side and does not expose the error to the client side
            response = {
                "status": 409,
                "message": "A user with that email address or phone already exists",
            }

            return make_response(response, 409)

        except Exception as e:
            db.session.rollback()
            log.error("unexpected_error", error=str(e))
            response = {
                "status": 500,
                "message": "An error error occurred",
            }

            return make_response(response, 500)


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
