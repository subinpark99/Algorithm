n = int(input())

for i in range(1, n + 1):
    m = sum(map(int, str(i)))

    if i + m == n:
        print(i)
        break
    elif i == n:
        print(0)
