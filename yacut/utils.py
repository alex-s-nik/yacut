import random
import string

from .services import short_link_exists

LEN_SHORT_ID = 6
MAX_LEN_SHORT_ID = 16

LOWER_LETTERS_N_DIGITS = frozenset(
    string.ascii_letters + string.digits
)


def get_unique_short_id():
    while True:
        short_link = _make_id()
        if not short_link_exists(short_link):
            return short_link


def _make_id():
    return ''.join(
        random.choice(
            tuple(LOWER_LETTERS_N_DIGITS)
        ) for _ in range(LEN_SHORT_ID)
    )
