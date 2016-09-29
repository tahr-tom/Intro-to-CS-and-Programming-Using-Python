# Return Abs
test_list = [1, -4, 8, -9]


def apply_to_each(l, f):
    for i in range(len(l)):
        l[i] = f(l[i])
apply_to_each(test_list, abs)

# Return +1
test_list = [1, -4, 8, -9]


def add_one(x): return x+1
apply_to_each(test_list, add_one)

# Return Square
test_list = [1, -4, 8, -9]


def square(target): return target ** 2
apply_to_each(test_list, square)
