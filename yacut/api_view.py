from http import HTTPStatus

from flask import jsonify, request, url_for
from werkzeug import exceptions

from . import app
from .error_handlers import InvalidAPIUsage
from .services import create_new_link_from_json, get_original_link_by_short, short_link_exists
from .utils import get_unique_short_id, MAX_LEN_SHORT_ID
from .validators import is_len_greater, is_not_letters_and_digits


@app.route('/api/id/', methods=['POST'])
def create_link():
    new_data = {}
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    new_data['original'] = data['url']

    if 'custom_id' not in data or not data['custom_id']:
        new_data['short'] = get_unique_short_id()
    else:
        if short_link_exists(data['custom_id']):
            raise InvalidAPIUsage(f'Имя \"{data["custom_id"]}\" уже занято.')
        if is_not_letters_and_digits(data['custom_id']):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if is_len_greater(data['custom_id'], MAX_LEN_SHORT_ID):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        new_data['short'] = data['custom_id']

    new_link = create_new_link_from_json(new_data)
    new_link['short_link'] = url_for('redirect_view', short_link_id=new_link['short_link'], _external=True)
    print(new_link)

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
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
