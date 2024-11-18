def area(a):
    '''Принимает число  a, возвращает квадрат числа a'''
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает число a умноженное на 4.'''
    if not isinstance(a, (int, float)):
        raise TypeError("Argument 'a' must be a number.")
    return 4 * a
