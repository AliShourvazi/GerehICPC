a, b, l = map(int, input().split())
c1, c2 = 0, 0
lastTime = 0

for i in range(1, l + 1):
    if i & 1:
        c1 += 1
    else:
        c2 += 1
    lastTime = a * c1 + b * c2

print(lastTime)
