def square(x):
    """
    x: int or float.
    """
    return x * x


def fourthpower(x):
    """
    :param x: one number
    :return: one number
    """
    return square(x) * square(x)


def iterpower(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: base^exp, int or float
    """
    ans = 1
    while exp > 0:
        ans *= base
        exp -= 1
    return ans


def recurpower(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: base^exp, int or float
    """
    if exp == 0:
        return 1
    else:
        return base * recurpower(base, exp - 1)


def gcditer(a, b):
    """
    :param a: positive int
    :param b: positive int
    :return: positive int, the greatest common divisor of a & b
    """
    if a > b:
        divisor = b
    elif a < b:
        divisor = a
    else:
        return a
    while a % divisor != 0 or b % divisor != 0:
        divisor -= 1
    return divisor


def gcdrecur(a, b):
    """
    :param a: positive int
    :param b: positive int
    :return: positive int, the greatest common divisor of a & b
    """
    if b == 0:
        return a
    else:
        return gcdrecur(b, a % b)

def isin(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr, False otherwise
    """
    if len(aStr) <= 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        leng = len(aStr)
        temp = leng // 2
        if char > aStr[temp - 1:]:
            aStr = aStr[temp:]
            return isin(char, aStr)
        else:
            aStr = aStr[:temp]
            return isin(char, aStr)
