r, c = map(int, input().split())

gotoRight = True if c <= 10 else False
fromUp = 11 - r
goInside = c if gotoRight else 21 - c

print("Right" if gotoRight else "Left", fromUp, goInside)
