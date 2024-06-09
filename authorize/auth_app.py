from auth_actions import *


def unauth_user_action():
    while True:
        print('\nHello guest!')
        print('\nType \n  - "register" to register\n  - "login" to authorize\n  - "exit" to quit\n')
        action = input('Enter your action: ').strip().lower()
        match action:
            case 'register': 
                print("\nRegistering new user")
                register_new_user()
            case 'login': 
                user = authorize_user()
                if user:
                    auth_user_action(user)
            case 'exit':
                exit()
            case _:
                print('Unknown operation')


def auth_user_action(user):
    while True:
        print(f'\nHello {user['email']}!')
        print('\nType\n  - "info" for user info\n  - "age" to set age\n  - "logout" to logout\n  - "exit" to quit\n')
        action = input('Enter your action: ').strip().lower()
        match action:
            case 'exit':
                exit()
            case 'info':
                show_user_info(user) 
            case 'age':
                set_user_age(user)
            case 'logout':
                return  # unauth_user_action()
            case _:
                print('Unknown operation')


def main():
    # passing control to unauth user menu
    unauth_user_action()


if __name__ == '__main__':
    main()
