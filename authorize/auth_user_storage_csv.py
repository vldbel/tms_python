from csv import DictReader as csv_DictReader
from csv import DictWriter as csv_DictWriter
from os.path import exists as file_exists


USERS_FILE_CSV = 'users.csv'
ADMIN_USER = {"user": "admin", "password": "password"}


def initialize_user_file(json_file=USERS_FILE_CSV):
    write_users_to_file([ADMIN_USER])
    print(f'Creating new users file: {json_file}')


def check_for_users_file(csv_file=USERS_FILE_CSV):
    if not file_exists(csv_file):
        print(f"Users file {USERS_FILE_CSV} not found.)")
        initialize_user_file()
        print(f'New user file {USERS_FILE_CSV} has been created.')


def prepare_user_data(users_list) -> list:
    for user in users_list:
        # remove empty values
        for key in list(user.keys()):
            if user[key] == "":
                del user[key]
        # try:
        #     user['age'] = int(user['age'])
        # except ValueError:
        #     del user['age']
    return users_list


def read_users_from_file(csv_file=USERS_FILE_CSV) -> list:
    check_for_users_file(csv_file)
    users_list = []
    with open(csv_file, 'r') as csvfile:
        reader = csv_DictReader(csvfile)
        for user in reader:
            users_list.append(user)
    return prepare_user_data(users_list)


def write_users_to_file(users_list, csv_file=USERS_FILE_CSV):
    fieldnames = list(set().union(*users_list))
    with open(csv_file, 'w', newline='') as csvfile:
        csv_DictWriter(csvfile, fieldnames=fieldnames)
        csv_DictWriter(csvfile, fieldnames=fieldnames).writeheader()
        csv_DictWriter(csvfile, fieldnames=fieldnames).writerows(users_list)
