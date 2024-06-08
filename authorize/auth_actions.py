from auth_validators import *
from auth_getters import *
# from auth_user_storage_json import *
from auth_user_storage_csv import *


def authenticate_user(auth_email, auth_password) -> dict:
    users = read_users_from_file()
    for user in users:
        if user['email'] == auth_email and user['password'] == auth_password:
            return user


def authorize_user():
    email = get_email()
    password = get_password()
    current_user = authenticate_user(email, password)
    if current_user:
        print(f'User {current_user['email']} has been authorized\n')
        return current_user
    else:
        print('User name not found or password missmatch\n')


def set_user_age(current_user):
    user_age = get_age(age_validator)
    current_user['age'] = user_age
    users = read_users_from_file()
    users_to_write = []
    for user in users:
        if user['email'] == current_user['email']:
            user.update(current_user)
        users_to_write.append(user)
    write_users_to_file(users)
    print('User age has been updated')


def show_user_info(current_user):
    print("\nHere is current user info:")
    for key, value in current_user.items():
        print(f'   {key}: {value}')


def register_new_user():
    # collect new user data
    new_user_email = get_email(email_validator)
    if not new_user_email:
        return

    new_user_password = get_password(password_validator)
    if not new_user_password:
        return

    # check if user already exists
    users = read_users_from_file()
    if any(new_user_email == user["email"] for user in users):
        print(f'User with email {new_user_email} already exists\n')
        return

    # write new user to file
    user = {'email': new_user_email, 'password': new_user_password}
    users.append(user)
    write_users_to_file(users)
    print(f'New user {user} has been registered\n')
