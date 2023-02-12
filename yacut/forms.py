import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, ValidationError


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
            Length(min=1, max=16, message='Максимальная длина короткой ссылки - 16 символов'),
            Optional()
        ]
    )
    submit = SubmitField(label='Создать')

    def validate_custom_id(form, field):
        if any(char not in (string.ascii_letters + string.digits) for char in field.data):
            raise ValidationError(
                ('Короткая ссылка может состоять только из больших латинских букв, '
                 'маленьких латинских букв и цифр в диапазоне от 0 до 9')
            )
