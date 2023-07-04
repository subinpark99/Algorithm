# 1
t = int(input())

for _ in range(t):
    n = int(input())
    d = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            d[i] = 1
        elif i == 2:
            d[i] = 2
        elif i == 3:
            d[i] = 4
        else:
            d[i] = d[i - 3] + d[i - 2] + d[i - 1]

    print(d[n])

# 2

t = int(input())


def sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    else:
        return sum(n - 1) + sum(n - 2) + sum(n - 3)


for _ in range(t):
    n = int(input())
    print(sum(n))
