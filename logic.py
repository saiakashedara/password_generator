import random
import string


def generate_password(length, use_numbers=True, use_symbols=True):

    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    password = "".join(random.choice(characters) for _ in range(length))

    return password