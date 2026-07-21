from flask import make_response
from flask_restful import Resource
from models import db, User


# /users route
class Users(Resource):
    def get(self):
        users = User.query.all()

        user_list = []

        for user in users:
            if user.profile:
                profile = {
                    "dob": user.profile.dob,
                    "gender": user.profile.gender,
                    "role": user.profile.role,
                    "bio": user.profile.bio,
                }
            else:
                profile = None

            # list associated books
            book_list = []
            for book in user.books:
                book = {"id": book.id, "title": book.title, "genre": book.genre}

                book_list.append(book)

            user_data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email_address": user.email_address,
                "phone": user.phone,
                "created_at": str(user.created_at),
                "profile": profile,
                "books": book_list,
            }

            user_list.append(user_data)

        return make_response(user_list, 200)


# /users/<int:id>
class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        if user:
            if user.profile:
                profile = {
                    "dob": user.profile.dob,
                    "gender": user.profile.gender,
                    "role": user.profile.role,
                    "bio": user.profile.bio,
                }
            else:
                profile = None

            user_data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email_address": user.email_address,
                "phone": user.phone,
                "created_at": str(user.created_at),
                "profile": profile,
            }

            return make_response(user_data, 200)
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
