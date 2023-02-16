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

    def from_dict(self, data):
        for field in ['id', 'original', 'short', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])
                
    def to_dict(self):
        return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp
        )