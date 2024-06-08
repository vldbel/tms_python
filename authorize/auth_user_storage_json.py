from json import dump as json_dump
from json import load as json_load
from os.path import exists as file_exists


USERS_FILE_JSON = 'users.json'
ADMIN_USER = {"user": "admin", "password": "password"}


def initialize_user_file(json_file=USERS_FILE_JSON):
    write_users_to_file([ADMIN_USER])
    print(f'Creating new users file: {json_file}')


def check_for_users_file(json_file=USERS_FILE_JSON):
    if not file_exists(json_file):
        print(f"Users file {json_file} not found.)")
        initialize_user_file()
        print(f'New user file {json_file} has been created.')


def read_users_from_file(json_file=USERS_FILE_JSON) -> list:
    check_for_users_file(json_file)
    with open(json_file, 'r') as json_file:
        users_list = json_load(json_file)
    return users_list


def write_users_to_file(users_list, json_file=USERS_FILE_JSON):
    with open(json_file, 'w') as json_file:
        json_dump(users_list, json_file, indent=4)
