def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad input type")

    if x >= 0:
        return x
    elif x == 0:
        pass
    else:
        return -x


def empty_function():
    pass


print(my_abs(-10))
print(empty_function())