test_list = [1, -4, 8, -9]
def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
apply_to_each(test_list, abs)


test_list = [1, -4, 8, -9]
def add_one(target):
    return target + 1
apply_to_each(test_list, add_one)


test_list = [1, -4, 8, -9]
def square(target):
    return target ** 2
apply_to_each(test_list, square)
