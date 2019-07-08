from flask import Blueprint, Response, current_app, jsonify, request

access_blueprint = Blueprint('access', __name__)


@access_blueprint.route('/access', methods=['GET'])
def get_number():
    number = current_app.cache.get_number()
    return jsonify(number=number)


@access_blueprint.route('/set', methods=['POST'])
def set_number():
    current_app.cache.set_number(request.get_json()['number'])
    return Response(status=200)
