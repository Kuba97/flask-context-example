from flask import Flask

APPLICATION_IMPORT_NAME = 'number_threading_service'


def create_app(lifetime_cached_object):
    app = Flask(APPLICATION_IMPORT_NAME)
    app.cache = lifetime_cached_object

    from .routes import access_number, decrement, increment
    app.register_blueprint(access_number.access_blueprint)
    app.register_blueprint(increment.increment_blueprint)
    app.register_blueprint(decrement.decrement_blueprint)

    return app
