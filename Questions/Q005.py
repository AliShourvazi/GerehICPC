from math import prod


angles = list(map(int, input().split()))

if prod(angles) != 0 and sum(angles) == 180:
    print("Yes")
else:
    print("No")
