import math


def polysum(n, s):
    """
    :param n: number of sides of a regular polygon, int
    :param s: length of each slide, int
    :return: sum of the area and square of the regular polygon's perimeter
    """
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    perimeter = (s * n) ** 2
    ans = round(area + perimeter, 4)
    return ans