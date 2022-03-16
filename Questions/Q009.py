k = int(input())

n = 1

while True:
    if n >= k:
        break
    else:
        n += 1

if n % 2 != 0:
    print("Payin Barare")
else:
    print("Bala Barare")
