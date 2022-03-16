n = input()

def main(num):
    if len(num) == 1:
        return num
    return main(str(sum([int(x) for x in num])))

print(main(n))
