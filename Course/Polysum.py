import math


def polysum(n, s):
    """
    :param n: number of sides of a regular polygon, int
    :param s: length of each slide
    :return: area of that polygon
    """
    return round(((0.25 * n * s ** 2) / (math.tan(math.pi/n))) + (s * n) ** 2, 4)
print(polysum(78, 40))