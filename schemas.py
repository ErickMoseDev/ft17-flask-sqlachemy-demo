from marshmallow import Schema, ValidationError, fields, validate, validates_schema


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
    id = fields.Int(dump_only=True)  # output only / serialization
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email_address = fields.Email(required=True)
    phone = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # relationships
    profile = fields.Nested(ProfileSchema)
    books = fields.List(fields.Nested(BookSchema))

    # validations

    # @validates("phone")
    # def validate_phone(self, data, **kwargs):
    #     if len(data) < 10 and len(data) > 10:
    #         raise ValidationError("phone number must be 10 characters")

    @validates_schema
    def validate_schema(self, data, **kwargs):
        errors = {}
        if all(key in data for key in ["first_name", "last_name", "phone"]):
            if len(data["first_name"]) < 1:
                errors["first_name"] = ["Firstname is required"]
            if len(data["last_name"]) < 1:
                errors["last_name"] = ["Lastname is required"]
            if len(data["phone"]) != 10:
                errors["phone"] = ["phone number must be 10 characters"]
        if errors:
            raise ValidationError(errors)


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class RegisterSchema(Schema):
    id = fields.Int(dump_only=True)  # output only / serialization
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email_address = fields.Email(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(
        load_only=True, validate=validate.Length(min=5)
    )  # input only / deserialization
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates_schema
    def validate_schema(self, data, **kwargs):
        errors = {}
        if all(key in data for key in ["first_name", "last_name", "phone"]):
            if len(data["first_name"]) < 1:
                errors["first_name"] = ["Firstname is required"]
            if len(data["last_name"]) < 1:
                errors["last_name"] = ["Lastname is required"]
            if len(data["phone"]) != 10:
                errors["phone"] = ["phone number must be 10 characters"]
        if errors:
            raise ValidationError(errors)


register_schema = RegisterSchema()


class LoginSchema(Schema):
    email_address = fields.Email(required=True)
    password = fields.Str(load_only=True)  # input only / deserialization


login_schema = LoginSchema()
