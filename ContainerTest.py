from collections import Iterable

mates = [1, 3, 4]
mates.append(9)
print(mates, len(mates), mates[2])

for one in mates:
    print(one)

map = {"key1": 100, "key2": 200}
map["key3"] = 300
print(map, map["key2"], map.get("key4", "empty"))

print(isinstance(map,Iterable))
for key in map:
    print(key)

for value in map.values():
    print(value)

for key, value in map.items():
    print(key, value)

a = [1, 2, 2, 2, 4, 5, 5]
setA = set(a)
print(a, setA)

setB = set([4, 5, 6, 7])
print(setB)
print(setA - setB, setA | setB, setA & setB)
