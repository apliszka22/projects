import string
import secrets
import random


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4")

    new_password = ''

    # Ensure at least one symbol
    if symbols:
        new_password += secrets.choice(string.punctuation)
    else:
        new_password += secrets.choice(string.ascii_lowercase)

    # Ensure at least one uppercase letter
    if uppercase:
        new_password += secrets.choice(string.ascii_uppercase)
    else:
        new_password += secrets.choice(string.ascii_lowercase)

    # Fill the rest of the password with random lower case and digits
    rest_length = length - 2
    lower_and_digits_chars = string.digits + string.ascii_lowercase
    new_password += ''.join(secrets.choice(lower_and_digits_chars) for _ in range(rest_length))

    # Shuffle the password to make the order random
    new_password = ''.join(random.sample(new_password, len(new_password)))

    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(length=8, symbols=False, uppercase=False)
        specs: str = f'U: {contains_upper(new_pass)} S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')