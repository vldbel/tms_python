# THE GUESS GAME v2.1 :)
from random import randint


def start_game() -> None:
    while True:
        print('\nWelcome to the GUESS GAME!\n\nType exit to quit')
        end_of_range = set_range()
        computer_nums = generate_nums(end_of_range)
        print(computer_nums)  # remove this line for real play :)
        tries_count = 0
        while True:
            tries_count += 1
            print(f'Guess try: {tries_count: >3}')
            user_nums = get_user_nums(end_of_range)
            nums_guessed = len(set(computer_nums) & set(user_nums))
            if nums_guessed == 3: 
                print(f'Congratulations! You\'ve won in {tries_count} tries!')
                exit()
            else: 
                print(f'You\'ve guessed {nums_guessed} from 3 numbers. Try again.')


def check_user_input(user_input: str) -> int:
    user_input.lower().strip()
    if user_input == 'exit':
        print('Thank you for playing. Bye!')
        quit()
    if user_input.isdigit():
        return int(user_input)


def set_range() -> int:
    while True:
        range_end = check_user_input(input('Set the range for guessing numbers - from 1 to (5-30): '))
        if range_end and (5 <= range_end <= 30):
            return range_end
        print('Input must be a number in the range 5-30')        


def get_user_nums(range_limit: int) -> set:
    user_nums = set()
    while len(user_nums) < 3:
        num = check_user_input(input(f'Enter number #{len(user_nums) + 1}: '))
        if num and (0 < num <= range_limit):
            user_nums.add(num)
            continue
        print(f'Wrong input. Please enter a number from 1 to {range_limit}')
    return user_nums


def generate_nums(end_of_gen_range: int) -> set:
    generated_numbers = set()
    while len(generated_numbers) < 3:
        generated_numbers.add(randint(1, end_of_gen_range))
    return generated_numbers


if __name__ == "__main__":
    start_game()
