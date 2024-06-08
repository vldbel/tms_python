def get_email(email_validator=None) -> str or None:
    while True:
        user_input = input('Enter user email: ').lower().strip()
        if not user_input:
            continue
        if user_input == 'exit':
            return
        if email_validator:
            if email_validator(user_input):
                return user_input
        else:
            return user_input


def get_password(password_validator=None) -> str or None:
    while True:
        user_input = input('Enter user password: ').strip()
        if not user_input:
            continue
        if user_input == 'exit':
            return
        if password_validator:
            if password_validator(user_input):
                return user_input
        else:
            return user_input


def get_age(age_validator=None) -> int or None:
    while True:
        user_input = input('Input your age: ').strip()
        if not user_input:
            continue

        if user_input == 'exit':
            return

        try:
            age = int(user_input)
        except ValueError:
            print('Age must be an integer')
            continue

        if age_validator:
            if age_validator(age):
                return age
        else:
            return age
