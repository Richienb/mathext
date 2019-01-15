"""
The Math Ext file
"""

def isfib(number):
    """
    Check if a number is in the Fibonacci sequence.
    :type number: integer
    :param number: Number to check
    """

    num1 = 1
    num2 = 1
    while True:
        if num2 < number:
            tempnum = num2
            num2 += num1
            num1 = tempnum
        elif num2 == number:
            return True
        else:
            return False


def isprime(number):
    """
    Check if a number is a prime number
    :type number: integer
    :param number: The number to check
    """

    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def convertbase(number, base=10):
    """
    Convert a number in base 10 to another base
    :type number: number
    :param number: The number to convert
    :type base: integer
    :param base: The base to convert to.
    """

    integer = number
    if not integer:
        return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
        integer, mod = divmod(integer, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]


def isnum(value):
    """
    Check if a value is a type of number (decimal or integer).
    :type value: object
    :param value: The value to check.
    """

    try:
        return bool(isinstance(value, (float, int)))
    except RuntimeError:
        return False
