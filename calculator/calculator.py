class UnsupportedOperationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UnknownOperatorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def calculator(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            raise UnsupportedOperationException("Division by zero not allowed")
        return x / y
    elif op == '^':
        if x == y and x == 0:
            raise UnsupportedOperationException("Zero raised to power zero has no sense")
        return x ** y
    else:
        raise UnknownOperatorException(op + " is an unknown operator. The operators allowed are +, -, *, / and ^")


x = int(input("x = "))
y = int(input("y = "))
op = str(input("op = "))
print(calculator(x, y, op))
