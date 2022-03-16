n = int(input())

print(1 if n == 0 else 2 ** (n - 1).bit_length())
