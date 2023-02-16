import string

def is_not_letters_and_digits(s: str) -> bool:
    return any(char not in (string.ascii_letters + string.digits) for char in s)


def is_len_greater(s: str, max_length: int):
    return len(s) > max_length
