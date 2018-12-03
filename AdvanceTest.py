rangeA = ["v1", "v2", "v3", "v4", "v5"]

for i in range(3):
    print(i, rangeA[i])

print(rangeA[0:3])

LA = [x * x for x in range(3) if x % 2 == 0]
print(LA)
