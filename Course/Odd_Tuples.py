def odd_tuples(a_tup):
    """"
    a_tup: a tuple
    return: tuple, every other element of a_tup
    """
    n = 0
    answer_tup = ()
    length = 0
    if len(a_tup) % 2 != 0:
        length = len(a_tup) + 1
    else:
        length = len(a_tup)
    while n != length:
        answer_tup += a_tup[n],
        n += 2
    return answer_tup


# print(odd_tuples(('I', 'am', 'a', 'test', 'tuple')))
# print(odd_tuples((10, 11, 15, 19, 8, 1, 16, 6, 2, 8)))
# print(odd_tuples(()))
