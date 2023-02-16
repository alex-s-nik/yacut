from http import HTTPStatus

from flask import jsonify, request
from werkzeug import exceptions

from . import app
from .services import create_new_link_from_json, get_original_link_by_short
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_link():
    data = request.get_json()
    if 'short' not in data:
        data['short'] = get_unique_short_id()
    print('short' in data)
    print(data)
    new_link = create_new_link_from_json(data)
    return jsonify(new_link), HTTPStatus.CREATED


@app.route('/api/id/<string:link_id>/', methods=['GET'])
def get_original_link(link_id: str):
    try:
        return jsonify(
            {
                'url': get_original_link_by_short(link_id)
            }
        ), HTTPStatus.OK
    except exceptions.HTTPException:
        return jsonify(
            {
                'message': 'Указанный id не найден'
            }
        ), HTTPStatus.NOT_FOUND
        
