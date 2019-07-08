from flask import Blueprint, Response, current_app

increment_blueprint = Blueprint('increment', __name__)


@increment_blueprint.route('/increment', methods=['POST'])
def increment_number():
    current_app.cache.increment_number()
    return Response(status=200)
