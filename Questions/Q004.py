def fact(n):
    sum = 1
    for m in range(1, n + 1):
        sum *= m
    return sum


def main():
    num = int(input())
    print(fact(num))


if __name__ == "__main__":
    main()
