n, m = map(int, input().split())

if n == 1:
    if m == 2:
        print("B")
    elif m == 3:
        print("A")
elif n == 2:
    if m == 1:
        print("A")
    elif m == 3:
        print("B")
elif n == 3:
    if m == 1:
        print("B")
    elif m == 2:
        print("A")
