import random
import string


def generate_str(length=10) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_post(user_id: int, title: str = None, body: str = None) -> dict:
    if title is None:
        title = generate_str(10)

    if body is None:
        body = generate_str(100)

    return {
        "userId": user_id,
        "title": title,
        "body": body}


def generate_album(user_id: int, title: str = None) -> dict:
    if title is None:
        title = generate_str(10)

    return {
        "userId": user_id,
        "title": title}
