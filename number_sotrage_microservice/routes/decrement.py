from flask import Blueprint, Response, current_app

decrement_blueprint = Blueprint('decrement', __name__)


@decrement_blueprint.route('/decrement', methods=['POST'])
def increment_number():
    current_app.cache.decrement_number()
    return Response(status=200)
