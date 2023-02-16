from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional,
                                ValidationError)

from .utils import MAX_LEN_SHORT_ID
from .validators import is_not_letters_and_digits


class URLMapForm(FlaskForm):
    original_link = URLField(
        label='Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(min=1, max=256, message='Слишком длинная ссылка, допускается до 256 символов'),
            URL(require_tld=True, message='Неверный формат ссылки')
        ]
    )
    custom_id = StringField(
        label='Ваш вариант короткой ссылки',
        validators=[
            Length(
                min=1,
                max=MAX_LEN_SHORT_ID,
                message=f'Максимальная длина короткой ссылки - {MAX_LEN_SHORT_ID} символов'
            ),
            Optional()
        ]
    )
    submit = SubmitField(label='Создать')

    def validate_custom_id(form, field):
        if is_not_letters_and_digits(field.data):
            raise ValidationError(
                ('Короткая ссылка может состоять только из больших латинских букв, '
                 'маленьких латинских букв и цифр в диапазоне от 0 до 9')
            )
