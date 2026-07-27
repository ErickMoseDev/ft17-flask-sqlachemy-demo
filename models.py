from datetime import datetime

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    # define relationships
    profile = db.relationship(
        "Profile", back_populates="user", cascade="all, delete-orphan", uselist=False
    )

    books = db.relationship(
        "Book", back_populates="author", cascade="all, delete-orphan"
    )

    # set_password
    def set_password(self, user_pass):
        self.password = generate_password_hash(password=user_pass).decode("utf-8")

    # check_password -> return a boolean
    def check_password(self, user_pass):
        return check_password_hash(self.password, user_pass)


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum("male", "female", name="gender_enums"), nullable=False)
    role = db.Column(
        db.Enum("admin", "staff", "user", name="roles_enum"),
        nullable=False,
        default="user",
    )
    bio = db.Column(db.String, nullable=True)

    # fk
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False
    )

    # define the relationship
    user = db.relationship("User", back_populates="profile")


# in practice
# user.profile -> give us more info about the user profile
# profile.user -> will show us the info about the user linked

# one to many
# 1 user has authored many books
# 1 - many relationship
# Foreign key goes to the many side of the relationship
#


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)

    # fk
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # define the relationship
    author = db.relationship("User", back_populates="books")


# in practice
# user.books
# book.author
