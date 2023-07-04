from sys import stdin

for i in range(3):
    n = int(stdin.readline())
    s = sum([int(stdin.readline()) for _ in range(n)])

    if s == 0:
        print(0)
    elif s < 0:
        print("-")
    elif s > 0:
        print("+")
