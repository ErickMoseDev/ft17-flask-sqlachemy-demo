from flask import make_response
from flask_restful import Resource
from models import db, Book


class BooksResource(Resource):
    pass


class BookByID(Resource):
    def delete(self, id):
        book = Book.query.filter_by(id=id).first()

        if book:
            db.session.delete(book)
            db.session.commit()

            response = {"message": "book deleted successfully"}

            return make_response(response, 200)

        else:
            response = {"status": 404, "message": "book not found"}

            return make_response(response, 404)
