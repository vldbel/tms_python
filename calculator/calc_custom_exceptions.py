class CalculatorInvalidExpressionFormat(Exception):
    def __str__(self):
        return 'Invalid expression format'


class CalculatorNumConversionError(Exception):
    def __str__(self):
        return 'Failed to convert to number'


class CalculatorOperationError(Exception):
    def __str__(self):
        return 'Operation not allowed'
