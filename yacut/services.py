from . import db
from .models import URLMap


def create_new_link(original, short):
    new_link = URLMap(
        original=original,
        short=short
    )
    db.session.add(new_link)
    db.session.commit()
    return new_link

def create_new_link_from_json(data):
    new_link = URLMap()
    new_link.from_dict(data)
    db.session.add(new_link)
    db.session.commit()
    return new_link.to_dict()


def short_link_exists(link_id):
    return db.session.query(db.exists().where(URLMap.short == link_id)).scalar()


def get_original_link_by_short(short_link_id):
    return URLMap.query.filter_by(short=short_link_id).first_or_404().original
