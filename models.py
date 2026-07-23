from datetime import datetime

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
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    # define relationships
    profile = db.relationship(
        "Profile", back_populates="user", cascade="all, delete-orphan", uselist=False
    )

    books = db.relationship(
        "Book", back_populates="author", cascade="all, delete-orphan"
    )


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum("male", "female"), nullable=False)
    role = db.Column(db.Enum("admin", "staff", "user"), nullable=False, default="user")
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
