# ------- validators -----------
def email_validator(user_email_candidate):
    if '@' not in user_email_candidate:
        print("Email doesn't contain @")
        return
    ...  # some more email format check
    return user_email_candidate


def password_validator(user_password_candidate):
    if len(user_password_candidate) < 5:
        print('Password is too short')
        return
    ...  # some more password format checks
    return user_password_candidate


def age_validator(user_age_candidate):
    if user_age_candidate < 18:
        print('Error - user must be adult')
        return
    ...  # some more age verifications
    return user_age_candidate
