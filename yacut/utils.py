import random
import string

LEN_SHORT_ID = 6


def get_unique_short_id():
    return ''.join(
        random.choice(
            string.ascii_letters + string.digits
        ) for _ in range(LEN_SHORT_ID)
    )
