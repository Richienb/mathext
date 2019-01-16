"""
The Math Ext file
"""

import math

def shapesides(inputtocheck, inputtype='shape'):
    """
    Get the sides of a shape.
    
    :type inputtocheck: string or number
    :param inputtocheck: The amount of sides or the shape to be checked, depending on the value of inputtype.
    
    :type inputtype: string
    :param inputtype: The type of input provided. Can be: 'shape', 'sides'.
    """

    # Define the array of sides to a shape
    shapestosides = {
        'triangle': 3,
        'square': 4,
        'pentagon': 5,
        'hexagon': 6,
        'heptagon': 7,
        'octagon': 8,
        'nonagon': 9,
        'decagon': 10,
        'hendecagon': 11,
        'dodecagon': 12,
        'triskaidecagon': 13,
        'tetrakaidecagon': 14,
        'pentadecagon': 15,
        'hexakaidecagon': 16,
        'heptadecagon': 17,
        'octakaidecagon': 18,
        'enneadecagon': 19,
        'icosagon': 20,
        'triacontagon': 30,
        'tetracontagon': 40,
        'pentacontagon': 50,
        'hexacontagon': 60,
        'heptacontagon': 70,
        'octacontagon': 80,
        'enneacontagon': 90,
        'hectagon': 100,
        'chiliagon': 1000,
        'myriagon': 10000,
        'megagon': 1000000,
        'googolgon': pow(10, 100),
        'ngon': 'n'
    }

    # Define an array with the flipped version of the sides to a shape
    sidestoshapes = dictflip(shapestosides)

    # If the lowercase version of the input type is 'shape'
    if inputtype.lower() == 'shape':
        # If the lowercase version of the shape is in the array
        if inputtocheck.lower() in shapestosides:
            # Return the corresponding sides
            return shapestosides[inputtocheck.lower()]

        # Return 'n'
        return shapestosides['n']

    if inputtype.lower() == 'sides':
        # If the lowercase version of the shape is in the array
        if inputtocheck.lower() in sidestoshapes:
            # Return the corresponding sides
            return sidestoshapes[inputtocheck.lower()]

        # Return 'ngon'
        return sidestoshapes['ngon']

    # Raise a warning
    raise ValueError("Invalid input type.")

def fracsimplify(numerator, denominator):
    """
    Simplify a fraction.
    :type numerator: integer
    :param numerator: The numerator of the fraction to simplify
    :type denominator: integer
    :param denominator: The denominator of the fraction to simplify
    :return: The simplified fraction
    :rtype: list
    """

    # If the numerator is the same as the denominator
    if numerator == denominator:
        # Return the most simplified fraction
        return '1/1'

    # If the numerator is larger than the denominator
    elif int(numerator) > int(denominator):
        # Set the limit to half of the numerator
        limit = int(numerator / 2)

    elif int(numerator) < int(denominator):

        # Set the limit to half of the denominator
        limit = int(denominator / 2)

    # For each item in range from 2 to the limit
    for i in range(2, limit):
        # Set the number to check as the limit minus i
        checknum = limit - i
        # If the number is divisible by the numerator and denominator
        if numerator % checknum == 0 and denominator % checknum == 0:
            # Set the numerator to half of the number
            numerator = numerator / checknum
            # Set the denominator to half of the number
            denominator = denominator / checknum

    # Return the integer version of the numerator and denominator
    return [int(numerator), int(denominator)]


def circleconvert(amount, currentformat, newformat):
    """
    Convert a circle measurement.
    
    :type amount: number
    :param amount: The number to convert.
    
    :type currentformat: string
    :param currentformat: The format of the provided value.
    
    :type newformat: string
    :param newformat: The intended format of the value.
    
    >>> circleconvert(45, "radius", "diameter")
    90
    """

    # If the same format was provided
    if currentformat.lower() == newformat.lower():
        # Return the provided value
        return amount

    # If the lowercase version of the current format is 'radius'
    if currentformat.lower() == 'radius':
        # If the lowercase version of the new format is 'diameter'
        if newformat.lower() == 'diameter':
            # Return the converted value
            return amount * 2

        # If the lowercase version of the new format is 'circumference'
        elif newformat.lower() == 'circumference':
            # Return the converted value
            return amount * 2 * math.pi

        # Raise a warning
        raise ValueError("Invalid new format provided.")

    # If the lowercase version of the current format is 'diameter'
    elif currentformat.lower() == 'diameter':
        # If the lowercase version of the new format is 'radius'
        if newformat.lower() == 'radius':
            # Return the converted value
            return amount / 2

        # If the lowercase version of the new format is 'circumference'
        elif newformat.lower() == 'circumference':
            # Return the converted value
            return amount * math.pi

        # Raise a warning
        raise ValueError("Invalid new format provided.")

    # If the lowercase version of the current format is 'circumference'
    elif currentformat.lower() == 'circumference':
        # If the lowercase version of the new format is 'radius'
        if newformat.lower() == 'radius':
            # Return the converted value
            return amount / math.pi / 2

        # If the lowercase version of the new format is 'diameter'
        elif newformat.lower() == 'diameter':
            # Return the converted value
            return amount / math.pi


def amountdiv(num, minnum, maxnum):
    """
    Get the amount of numbers divisable by a number.
    
    :type num: number
    :param number: The number to use.
    
    :type minnum: integer
    :param minnum: The minimum number to check.
    
    :type maxnum: integer
    :param maxnum: The maximum number to check.
    
    >>> amountdiv(20, 1, 15)
    5
    """

    # Set the amount to 0
    amount = 0

    # For each item in range of minimum and maximum
    for i in range(minnum, maxnum + 1):
        # If the remainder of the divided number is 0
        if num % i == 0:
            # Add 1 to the total amount
            amount += 1

    # Return the result
    return amount
    
# Set the value of the golden ratio
phi = (1 + 5**0.5) / 2

def factorial(num):
    """
    Find the factorial of a number
    
    :type num: integer
    :param num: The number to find the factorial for.
    """
    
    if num == 0:
        return 1
    return num * factorial(num - 1)

def triangular(num):
    """
    Check if a number is triangular
    
    :type num: number
    :param num: The number to check.
    """
    
    x = (math.sqrt(8 * num + 1) - 1) / 2
    return bool(x - int(x) > 0)

def square(num):
    """
    Check if a number is square
    
    :type num: number
    :param num: The number to check.
    """
    
    return math.sqrt(num).is_integer()

def cube(num):
    """
    Check if a number is cube
    
    :type num: number
    :param num: The number to check.
    """
    
    x = num**(1 / 3)
    x = int(round(x))
    return bool(x**3 == num)

def even(num):
    """
    Check if a number is even
    
    :type num: number
    :param num: The number to check.
    """
    
    return num % 2 == 0

def odd(num):
    """
    Check if a number is odd
    
    :type num: number
    :param num: The number to check.
    """
    
    return num % 2 != 0

def positive(num):
    """
    Check if a number is positive (more than 0)
    
    :type num: number
    :param num: The number to check.
    """
    
    return num > 0

def negative(num):
    """
    Check if a number is negative (less than 0)
    
    :type num: number
    :param num: The number to check.
    """
    
    return num < 0

def zero(num):
    """
    Check if a number is zero
    
    :type num: number
    :param num: The number to check.
    """
    
    return num == 0

def sigmoid(num):
    """
    Find the sigmoid of a number.
    :type number: number
    :param number: The number to find the sigmoid of
    :return: The result of the sigmoid
    :rtype: number
    >>> sigmoid(1)
    0.7310585786300049
    """

    # Return the calculated value
    return 1 / (1 + math.exp(-num))

def posneg(num):
    """
    Toggle a number between positive and negative.
    
    The converter works as follows:
    - 1 > -1
    - -1 > 1
    - 0 > 0
    
    :type num: number
    :param num: The number to toggle.
    """
    if bool(num > 0):
        return num - num * 2
    elif bool(num < 0):
        return num + abs(num) * 2
    elif bool(num == 0):
        return num
    
def nothing(variable):
    """
    Check if a variable is essentially nothing.
    
    :type variable: variable
    :param variable: The variable to check.
    """

    # Return the answer
    return variable in [0, 0.0, False, [], {}, math.nan, "", (), None]
    
def fib(num):
    """
    Check if a number is in the Fibonacci sequence.
    
    :type number: integer
    :param number: The number to check.
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


def prime(num):
    """
    Check if a number is a prime number.
    
    :type num: integer
    :param num: The number to check.
    """

    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def convertbase(num, base=10):
    """
    Convert a number in base 10 to another base
    
    :type num: number
    :param num: The number to convert.
    
    :type base: integer
    :param base: The base to convert to.
    """

    integer = num
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


def num(value):
    """
    Check if a value is a type of number (decimal or integer).
    
    :type value: object
    :param value: The value to check.
    """

    try:
        return bool(isinstance(value, (float, int)))
    except RuntimeError:
        return False
    
def quadrant(xcoord, ycoord):
    """
    Find the quadrant a pair of coordinates are located in
    
    :type xcoord: integer
    :param xcoord: The x coordinate to find the quadrant for
    
    :type ycoord: integer
    :param ycoord: The y coordinate to find the quadrant for
    """

    xneg = bool(xcoord < 0)
    yneg = bool(ycoord < 0)
    if xneg is True:
        if yneg is False:
            return 2
        return 3
    if yneg is False:
        return 1
    return 4


def flipcoords(xcoord, ycoord, axis):
    """
    Flip the coordinates over a specific axis, to a different quadrant
    
    :type xcoord: integer
    :param xcoord: The x coordinate to flip
    
    :type ycoord: integer
    :param ycoord: The y coordinate to flip
    
    :type axis: string
    :param axis: The axis to flip across. Could be 'x' or 'y'
    """

    axis = axis.lower()
    if axis == 'y':
        if xcoord > 0:
            return str(xcoord - xcoord - xcoord) + ', ' + str(ycoord)
        elif xcoord < 0:
            return str(xcoord + abs(xcoord) * 2) + ', ' + str(ycoord)
        elif xcoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise ValueError(
            "The X coordinate is neither larger, smaller or the same as 0.")

    elif axis == 'x':
        if ycoord > 0:
            return str(xcoord) + ', ' + str(ycoord - ycoord - ycoord)
        elif ycoord < 0:
            return str(ycoord + abs(ycoord) * 2) + ', ' + str(xcoord)
        elif ycoord == 0:
            return str(xcoord) + ', ' + str(ycoord)
        raise ValueError(
            "The Y coordinate is neither larger, smaller or the same as 0.")
    raise ValueError("Invalid axis. Neither x nor y was specified.")


def lcm(num1, num2):
    """
    Find the lowest common multiple of 2 numbers
    
    :type num1: number
    :param num1: The first number to find the lcm for
    
    :type num2: number
    :param num2: The second number to find the lcm for
    """

    if num1 > num2:
        bigger = num1
    else:
        bigger = num2
    while True:
        if bigger % num1 == 0 and bigger % num2 == 0:
            return bigger
        bigger += 1


def hcf(num1, num2):
    """
    Find the highest common factor of 2 numbers.
    
    :type num1: number
    :param num1: The first number to find the hcf for
    
    :type num2: number
    :param num2: The second number to find the hcf for
    """

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            return i


def pyth(first, second):
    """
    Calculate the area of a right angled trangle based on Pythagoras' Theorem.
    
    :type first: number
    :param first: The length of the first axis (x or y)
    
    :type second: number
    :param second: The length of the second axis (x or y)
    """

    return (first * second) / 2

# About information in a constant
about = """You are using Mathext
Mathext is licensed under the MIT License"""
    
# Set a constant which can be checked to verify if Mathext is ready.
ready = True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
