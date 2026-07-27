# Flask Notes

- `Flask-SQLAlchemy` is an extension for Flask that simplifies the integration of SQLAlchemy with Flask applications. It handles common tasks like setting up the database engine and session, making it easier to define models and perform database operations.
- `MetaData` is a core SQLAlchemy construct that acts as a container for information about your database schema (tables, columns, constraints, etc.). It's essentially a catalog of your database's structure.
- `metadata = MetaData():`
    - This line creates an instance of the MetaData object. This specific MetaData instance will be used to store the definitions of the tables that your SQLAlchemy models will represent.
- `db = SQLAlchemy(metadata=metadata):` - This is where Flask-SQLAlchemy is initialized. - SQLAlchemy() creates an instance of the Flask-SQLAlchemy extension. - The metadata=metadata argument tells Flask-SQLAlchemy to use the MetaData object we just created (metadata) to store the table definitions for all models associated with this db instance. If you don't pass a metadata object, Flask-SQLAlchemy will create one for you by default.

    ```py
      naming_convention = {
      "ix": "ix_%(column_0_label)s",
      "uq": "uq_%(table_name)s_%(column_0_name)s",
      "ck": "ck_%(table_name)s_%(constraint_name)s",
      "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
      "pk": "pk_%(table_name)s",
    }
    ```

### `SQLAlchemy` Object (`db`) Initialization and Configuration

The `db` object (typically an instance of `SQLAlchemy`) is the central entry point for database operations.

- **`db = SQLAlchemy(app=None, model_class=Base, metadata)`**: The constructor for the `SQLAlchemy` extension.
    - `app`: You can pass your Flask application instance directly here, or initialize it later using `db.init_app(app)`.
    - `model_class`: In SQLAlchemy 2.0 style, you define a base class for your models (e.g., `class Base(DeclarativeBase): pass`) and pass it here. This helps with automatic table name generation and other declarative features.
- **`db.init_app(app)`**: Connects the SQLAlchemy extension to your Flask application. This is typically used in the "app factory" pattern.
- **Configuration Keys**: Flask-SQLAlchemy relies on Flask's configuration. Common keys include:
    - `SQLALCHEMY_DATABASE_URI`: The connection string to your database (e.g., `sqlite:///site.db`, `postgresql://user:pass@host:port/db_name`).
    - `SQLALCHEMY_TRACK_MODIFICATIONS`: Set to `False` to disable the event system that tracks changes, often improving performance for simple apps if you don't need signals.
    - `SQLALCHEMY_ECHO`: Set to `True` to log all SQL statements to the console.
    - `SQLALCHEMY_BINDS`: For managing multiple databases in one application.
- **`db.create_all()`**: Creates all database tables defined by your models. **Important:** This should be called within a Flask application context (e.g., `with app.app_context(): db.create_all()`).
- **`db.drop_all()`**: Drops all database tables defined by your models. Use with extreme caution, as it deletes data. Also needs an application context.
- **`db.engine`**: Provides direct access to the underlying SQLAlchemy Engine object, which manages database connections.
- **`db.metadata`**: Provides access to the SQLAlchemy `MetaData` object, which contains information about your tables.

Context Management

Flask-SQLAlchemy handles `db.session` within the request context automatically. However, when working outside a request (e.g., in a custom Flask CLI command or tests), you need to manually establish an application context:

- **`with app.app_context():`**: Ensures that `db.session` and other Flask-related context locals are available.

### Migrations (via Flask-Migrate or Flask-Alembic)

While not strictly part of Flask-SQLAlchemy itself, database migrations are a crucial functionality for managing schema changes. Flask-SQLAlchemy highly recommends using `Flask-Migrate` (which wraps Alembic) for this.

- **`flask db init`**: Initializes the migration repository.
- **`flask db migrate -m "message"`**: Autogenerates a migration script based on changes in your models.
- **`flask db upgrade`**: Applies pending migrations to the database.
- **`flask db downgrade`**: Reverts applied migrations.

This covers the primary methods and functionalities offered by Flask-SQLAlchemy. Remember that because it's a wrapper around SQLAlchemy, deeper dives into specific query methods or ORM patterns will often lead you to the core SQLAlchemy documentation.

## Cookie Security

[reference material](https://blog.miguelgrinberg.com/post/cookie-security-for-flask-applications)

## Deployment

- install psycopg2-binary gunicorn
-
