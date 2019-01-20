# Copyright (c) 2019 Richie Bendall
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
The Math Ext file
"""

import math
import fractions
from fractions import Fraction
import sys
import string
from numbers import Number


def shapesides(inputtocheck, inputtype='shape'):
    """
    Get the sides of a shape.
    
    :type inputtocheck: string or number
    :param inputtocheck: The amount of sides or the shape to be checked, depending on the value of inputtype.
    
    :type inputtype: string
    :param inputtype: The type of input provided. Can be: 'shape', 'sides'.
    
    >>> shapesides(3, "sides")
    'triangle'
    
    >>> shapesides("n", "sides")
    'ngon'
    
    >>> shapesides("N", "sides")
    'ngon'
    
    >>> shapesides("foo", "sides")
    'ngon'
    
    >>> shapesides("ngon", "shape")
    'n'

    >>> shapesides("triangle", "shape")
    3
    
    >>> shapesides("foo", "shape")
    'n'
    
    >>> shapesides("foo", "foo")
    Traceback (most recent call last):
        ...
    ValueError: Invalid input type.
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
    sidestoshapes = {v: k for k, v in shapestosides.items()}

    # If the lowercase version of the input type is 'shape'
    if inputtype.lower() == 'shape':
        # If the lowercase version of the shape is in the array
        if inputtocheck.lower() in shapestosides:
            # Return the corresponding sides
            return shapestosides[inputtocheck.lower()]

        # Return 'n'
        return shapestosides['ngon']
    if inputtype.lower() == 'sides':
        # If the shape is in the array
        if inputtocheck in sidestoshapes:
            # Return the corresponding sides
            return sidestoshapes[inputtocheck]

        # If the lowercase version of the shape is in the array
        elif inputtocheck.lower() in sidestoshapes:
            # Return the corresponding sides
            return sidestoshapes[inputtocheck.lower()]

        # Return 'ngon'
        return sidestoshapes['n']
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
    
    >>> fracsimplify(2, 4)
    (1, 2)
    """

    frac = Fraction(numerator, denominator)
    return frac.numerator, frac.denominator


def circleconvert(amount, currentformat, newformat):
    """
    Convert a circle measurement.
    
    :type amount: number
    :param amount: The number to convert.
    
    :type currentformat: string
    :param currentformat: The format of the provided value.
    
    :type newformat: string
    :param newformat: The intended format of the value.
    
    >>> circleconvert(45, "radius", "radius")
    45
    
    >>> circleconvert(45, "radius", "diameter")
    90
    
    >>> circleconvert(45, "radius", "circumference")
    282.7433388230814
    
    >>> circleconvert(45, "diameter", "diameter")
    45
    
    >>> circleconvert(45, "diameter", "radius")
    22.5
    
    >>> circleconvert(45, "diameter", "circumference")
    141.3716694115407
    
    >>> circleconvert(45, "circumference", "circumference")
    45
    
    >>> circleconvert(45, "circumference", "radius")
    7.16197243913529
    
    >>> circleconvert(45, "circumference", "diameter")
    14.32394487827058
    
    >>> circleconvert(45, "foo1", "foo2")
    Traceback (most recent call last):
        ...
    ValueError: Invalid old format provided.
    
    >>> circleconvert(45, "radius", "foo")
    Traceback (most recent call last):
        ...
    ValueError: Invalid new format provided.
    
    >>> circleconvert(45, "diameter", "foo")
    Traceback (most recent call last):
        ...
    ValueError: Invalid new format provided.
    
    >>> circleconvert(45, "circumference", "foo")
    Traceback (most recent call last):
        ...
    ValueError: Invalid new format provided.
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

        # Raise a warning
        raise ValueError("Invalid new format provided.")

    # Raise a warning
    raise ValueError("Invalid old format provided.")


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
    
    >>> factorial(4)
    24
    """

    if num == 0:
        return 1
    return num * factorial(num - 1)


def triangular(num):
    """
    Check if a number is triangular
    
    :type num: number
    :param num: The number to check.
    
    >>> triangular(5)
    True
    """

    x = (math.sqrt(8 * num + 1) - 1) / 2
    return bool(x - int(x) > 0)


def square(num):
    """
    Check if a number is square
    
    :type num: number
    :param num: The number to check.
    
    >>> square(4)
    True
    """

    return math.sqrt(num).is_integer()


def cube(num):
    """
    Check if a number is cube
    
    :type num: number
    :param num: The number to check.
    
    >>> cube(8)
    True
    """

    x = num**(1 / 3)
    x = int(round(x))
    return bool(x**3 == num)


def even(num):
    """
    Check if a number is even
    
    :type num: number
    :param num: The number to check.
    
    >>> even(2)
    True
    """

    return num % 2 == 0


def odd(num):
    """
    Check if a number is odd
    
    :type num: number
    :param num: The number to check.
    
    >>> odd(3)
    True
    """

    return num % 2 != 0


def positive(num):
    """
    Check if a number is positive (more than 0)
    
    :type num: number
    :param num: The number to check.
    
    >>> positive(1)
    True
    """

    return num > 0


def negative(num):
    """
    Check if a number is negative (less than 0)
    
    :type num: number
    :param num: The number to check.
    
    >>> negative(-1)
    True
    """

    return num < 0


def zero(num):
    """
    Check if a number is zero
    
    :type num: number
    :param num: The number to check.
    
    >>> zero(0)
    True
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
    
    >>> posneg(2)
    -2
    """

    return -num


def nothing(variable):
    """
    Check if a variable is essentially nothing.
    
    :type variable: variable
    :param variable: The variable to check.
    
    >>> nothing(0)
    True
    """

    # Return the answer
    return math.isnan(variable) or variable in [
        0, 0.0, False, [], {}, "", (), None
    ]


def fib(num):
    """
    Check if a number is in the Fibonacci sequence.
    
    :type num: integer
    :param num: The number to check.
    
    >>> fib(8)
    True
    
    >>> fib(4)
    False
    """

    num1 = 1
    num2 = 1
    while True:
        if num2 < num:
            tempnum = num2
            num2 += num1
            num1 = tempnum
        else:
            return num2 == num


def prime(num):
    """
    Check if a number is a prime number.
    
    :type num: integer
    :param num: The number to check.
    
    >>> prime(7)
    True
    
    >>> prime(1)
    False
    """

    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def getprime(n):
    """
    Get the nth prime number
    
    :type n: integer
    :param n: The number representing n.
    
    >>> getprime(3)
    5
    """

    primes = []
    num = 2
    while len(primes) < n:
        if prime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


def convertbase(num, base=10):
    """
    Convert a number in base 10 to another base
    
    :type num: number
    :param num: The number to convert.
    
    :type base: integer
    :param base: The base to convert to.
    
    >>> convertbase(20, 6)
    '32'
    """

    sign = 1 if num > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    num *= sign
    while num:
        num, mod = divmod(num, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]


def num(value):
    """
    Check if a value is a type of number (decimal or integer).
    
    :type value: object
    :param value: The value to check.
    
    >>> num(1)
    True
    """

    return isinstance(value, Number)


def quadrant(xcoord, ycoord):
    """
    Find the quadrant a pair of coordinates are located in
    
    :type xcoord: integer
    :param xcoord: The x coordinate to find the quadrant for
    
    :type ycoord: integer
    :param ycoord: The y coordinate to find the quadrant for
    
    >>> quadrant(5, 5)
    1
    
    >>> quadrant(-5, 5)
    2
    
    >>> quadrant(-5, -5)
    3
    
    >>> quadrant(5, -5)
    4
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
    
    >>> flipcoords(-5, 5, "y")
    (5, 5)
    
    >>> flipcoords(5, 5, "y")
    (-5, 5)
    
    >>> flipcoords(0, -5, "y")
    (0, -5)
    
    >>> flipcoords(-5, -5, "x")
    (-5, 5)
    
    >>> flipcoords(5, 5, "x")
    (5, -5)
    
    >>> flipcoords(0, -5, "x")
    (0, 5)
    
    >>> flipcoords(-5, 0, "x")
    (-5, 0)
    
    >>> flipcoords(5, 5, "foo")
    Traceback (most recent call last):
        ...
    ValueError: Invalid axis. Neither x nor y was specified.
    """

    axis = axis.lower()
    if axis == 'y':
        if xcoord == 0:
            return xcoord, ycoord
        return -xcoord, ycoord

    elif axis == 'x':
        if ycoord == 0:
            return xcoord, ycoord
        return xcoord, -ycoord

    raise ValueError("Invalid axis. Neither x nor y was specified.")


def hcf(num1, num2):
    """
    Find the highest common factor of 2 numbers.
    
    :type num1: number
    :param num1: The first number to find the hcf for
    
    :type num2: number
    :param num2: The second number to find the hcf for
    
    >>> hcf(5, 10)
    5
    """

    if sys.version_info[0] >= 3 and sys.version_info[1] >= 5:
        return math.gcd(num1, num2)
    return fractions.gcd(num1, num2)


def lcm(num1, num2):
    """
    Find the lowest common multiple of 2 numbers
    
    :type num1: number
    :param num1: The first number to find the lcm for
    
    :type num2: number
    :param num2: The second number to find the lcm for
    
    >>> lcm(4, 8)
    8
    
    >>> lcm(0, 0)
    0
    """

    if num1 == num2 == 0:
        return 0
    return abs(num1 * num2) // hcf(num1, num2)


def pyth(first, second):
    """
    Calculate the area of a right angled trangle based on Pythagoras' Theorem.
    
    :type first: number
    :param first: The length of the first axis (x or y)
    
    :type second: number
    :param second: The length of the second axis (x or y)
    
    >>> pyth(3, 5)
    7.5
    """

    return (first * second) / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
