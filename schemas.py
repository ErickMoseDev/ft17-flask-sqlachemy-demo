from marshmallow import Schema, fields


class ProfileSchema(Schema):
    dob = fields.Date(required=True)
    gender = fields.Str(required=True)
    role = fields.Str(required=True)
    bio = fields.Str(required=True)
    user = fields.Nested("UserSchema", exclude=("profile", "books"))


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    genre = fields.Str(required=True)

    author = fields.Nested("UserSchema", exclude=("books",))


book_schema = BookSchema()


class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # output only
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email_address = fields.Email(required=True)
    phone = fields.Str()
    password = fields.Str(load_only=True)  # input only
    created_at = fields.DateTime(dump_only=True)

    profile = fields.Nested(ProfileSchema)
    books = fields.List(fields.Nested(BookSchema))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
