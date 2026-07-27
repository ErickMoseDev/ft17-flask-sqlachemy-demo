from flask import make_response, request, session
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from extensions import log
from models import User, db
from schemas import login_schema, register_schema, user_schema


class Login(Resource):
    def post(self):
        try:
            # check if the user exists and if their password matches
            data = request.get_json()
            validated_data = login_schema.load(data)

            user = User.query.filter_by(
                email_address=validated_data["email_address"]
            ).first()

            if user and user.check_password(user_pass=validated_data["password"]):
                # create a user session
                session["user_id"] = user.id
                response = {
                    "message": "Login Successful",
                    "data": user_schema.dump(user),
                }
                return make_response(response, 200)
            else:
                response = {
                    "status": 401,
                    "message": "An error occurred",
                    "errors": "Invalid email or password",
                }
                return make_response(response, 401)

        except ValidationError as err:
            log.error("validation_error", errors=err.messages)
            response = {
                "status": 400,
                "message": "Validation error(s) occured",
                "errors": {**err.messages},
            }

            return make_response(response, 400)
        except Exception as e:  # noqa: BLE001
            log.error("unexpected_error", error=str(e))
            response = {
                "status": 500,
                "message": "An error error occurred",
            }

            return make_response(response, 500)


class Register(Resource):
    def post(self):
        try:
            data = request.get_json()
            # pass the data through a register schema
            validated_data = register_schema.load(data)

            # check for duplicates of email and phone before inserting
            if User.query.filter_by(
                email_address=validated_data["email_address"]
            ).first():
                return make_response(
                    {"status": 409, "message": "Email address already taken"}, 409
                )
            if User.query.filter_by(phone=validated_data["phone"]).first():
                return make_response(
                    {"status": 409, "message": "Phone number already taken"}, 409
                )
            # create user instance
            user = User(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email_address=validated_data["email_address"],
                phone=validated_data["phone"],
            )

            # set the password hash
            user.set_password(validated_data["password"])

            db.session.add(user)
            db.session.commit()

            # create a session
            session["user_id"] = user.id

            response = {
                "message": "Account created successfully",
                "data": user_schema.dump(user),
            }

            return make_response(response, 201)

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

        except Exception as e:  # noqa: BLE001
            log.error("unexpected_error", error=str(e))
            response = {
                "status": 500,
                "message": "An error error occurred",
            }

            return make_response(response, 500)


class Logout(Resource):
    def delete(self):
        session.clear()
        return {}, 204


class CheckSession(Resource):
    def get(self):
        user_id = session.get("user_id")

        if not user_id:
            response = {
                "status": 401,
                "message": "You are not authenticated",
            }

            return make_response(response, 401)

        user = User.query.get(user_id)
        return make_response(user_schema.dump(user))
