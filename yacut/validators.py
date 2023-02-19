from utils import LOWER_LETTERS_N_DIGITS


def is_not_letters_and_digits(s: str) -> bool:
    return all(char in LOWER_LETTERS_N_DIGITS for char in s)


def is_len_greater(s: str, max_length: int):
    return len(s) > max_length
