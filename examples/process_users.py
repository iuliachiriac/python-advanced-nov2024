import json
from pathlib import Path


def get_users(filename, age_min=0, age_max=100):
    try:
        with open(filename) as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []
    return [user for user in users if age_min < user["age"] < age_max]


def get_name_age(user):
    match user:
        case {"name": name}:
            name = name
        case {"first_name": first_name, "last_name": last_name}:
            name = f"{first_name} {last_name}"
        case _:
            name = None

    if not name:
        raise ValueError("Name not found")

    return name, user["age"]


if __name__ == "__main__":
    users_path = Path.cwd().parent / "docs" / "users.json"
    user_list = get_users(str(users_path))
    for user in user_list:
        try:
            name, age = get_name_age(user)
        except ValueError as ex:
            print(ex, user)
        else:
            print(name, age)
