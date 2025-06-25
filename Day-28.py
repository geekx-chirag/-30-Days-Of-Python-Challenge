def calc(a, b, c):
    if c == 'add':
        return a + b
    elif c == 'sub':
        return a - b
    elif c == 'mul':
        return a * b
    elif c == 'div':
        if b != 0:
            return a / b
        else:
            return 'Error'
    else:
        return 'Invalid operation'


#################################

from enum import Enum
from typing import Union

class Operation(Enum):
    ADD = 'add'
    SUBTRACT = 'sub'
    MULTIPLY = 'mul'
    DIVIDE = 'div'

def calculate(a: float, b: float, operation: Operation) -> Union[float, str]:
    """
    Performs basic arithmetic operations.

    Args:
        a (float): The first operand.
        b (float): The second operand.
        operation (Operation): The operation to perform.

    Returns:
        float: The result of the operation.
        str: Error message if an invalid operation or division by zero occurs.
    """
    if operation == Operation.ADD:
        return a + b
    elif operation == Operation.SUBTRACT:
        return a - b
    elif operation == Operation.MULTIPLY:
        return a * b
    elif operation == Operation.DIVIDE:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError("Invalid operation.")
