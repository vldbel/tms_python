# Calculator v.1.3

from calc_custom_exceptions import *


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def exponentiation(a, b):
    return a ** b


def get_expression():
    user_input = input('Enter expression: ').strip()
    return user_input


def check_exit(user_string):
    if 'exit' in user_string.lower():
        return True


def split_expression(user_expression):
    result = user_expression.split()
    if len(result) != 3:
        raise CalculatorInvalidExpressionFormat(user_expression)
    return result


def convert_to_num(user_num):
    try:
        num = int(user_num)
    except ValueError:
        try:
            num = float(user_num)
        except ValueError:
            raise CalculatorNumConversionError(user_num)
    return num


def check_operation(user_operation):
    if user_operation not in ALLOWED_OPERATIONS:
        raise CalculatorOperationError


def try_convert_float_to_int(user_float):
    if user_float - int(user_float) < 1e-6:
        return int(user_float)
    else:
        return user_float


ALLOWED_OPERATIONS = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '**': exponentiation,
}


def main():
    print("Calculator v1.3")
    print("Type exit to exit the calculator")
    print(f"allowed operations: {', '.join(list(ALLOWED_OPERATIONS.keys()))}")
    print("Please enter expression in the following format: 12 * 3.5. Use space to delimit parts")

    while True:
        expression = get_expression()

        if check_exit(expression):
            print('Exiting...')
            exit()

        try:
            num1, operation, num2 = split_expression(expression)
        except CalculatorInvalidExpressionFormat:
            print('Invalid expression, please try again')
            continue

        try:
            num1 = convert_to_num(num1)
            num2 = convert_to_num(num2)
        except CalculatorNumConversionError:
            print('Invalid number format, please try again')
            continue

        try:
            check_operation(operation)
        except CalculatorOperationError:
            print('Invalid operation, please try again')
            continue

        try:
            result = ALLOWED_OPERATIONS[operation](num1, num2)
        except ZeroDivisionError:
            print('Division by zero error, please change expression')
            continue

        if isinstance(result, float):
            result = try_convert_float_to_int(result)

        print(f'Result: {result}')


if __name__ == "__main__":
    main()
