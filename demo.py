from numpy import *

print("Hello World")

# name = input()
# print(name)

mates = [1, 3, 4]
mates.append(9)
print(mates, mates[2])
if (len(mates) > 0):
    print(">0")
elif len(mates) == 0:
    print("==0")
else:
    print("<0")

for one in mates:
    print(one)

map = {"key1": 100, "key2": 200}
map["key3"] = 300;
print(map, map["key2"], map.get("key4", "empty"))


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

# print(mat(random.rand(4, 4)).I)
