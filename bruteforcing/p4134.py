def sosu(x):
    if x >= 2:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


n = int(input())

for _ in range(n):
    a = int(input())

    while True:
        if sosu(a):
            print(a)
            break
        else:
            a += 1
