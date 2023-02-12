from datetime import datetime

from yacut import db


class URLMap(db.Model):
    # поле для ID
    id = db.Column(db.Integer, primary_key=True)
    # поле для оригинальной длинной ссылки
    original = db.Column(db.String(length=256), nullable=False)
    # поле для короткого идентификатора
    short = db.Column(db.String(16), nullable=False, unique=True)
    # поле для временной метки
    timestamp = db.Column(db.DateTime, default=datetime.now)
